# ================================================
# MULTIPROCESS LIFECYCLE (ep 50)
# Starting, monitoring, and stopping processes
# ================================================
import multiprocessing as mp
import logging
import time
import os


# ================================================
# Logging setup - call this in every process
# Each process is a separate Python interpreter
# ================================================
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(processName)-12s | %(message)s',
        datefmt='%H:%M:%S'
    )


# ================================================
# A simple worker
# ================================================
def short_worker():
    setup_logging()
    log = logging.getLogger()
    log.info(f"starting (PID {os.getpid()})")
    time.sleep(1)
    log.info("finishing")


# ================================================
# A worker that runs forever - until told to stop
# ================================================
def long_worker():
    setup_logging()
    log = logging.getLogger()
    log.info("starting forever-loop")
    while True:
        time.sleep(0.5)
        log.info("still working...")


# ================================================
# A cooperative worker - exits when event is set
# ================================================
def cooperative_worker(stop_event):
    setup_logging()
    log = logging.getLogger()
    log.info("starting cooperative work")
    while not stop_event.is_set():
        time.sleep(0.3)
        log.info("working...")
    log.info("stop signal received, exiting cleanly")


# ================================================
# Main code
# ================================================
if __name__ == "__main__":
    setup_logging()
    log = logging.getLogger()


    # ================================================
    # is_alive() - check if process is running
    # ================================================
    log.info("--- is_alive() ---")
    p = mp.Process(target=short_worker, name="Worker1")
    log.info(f"before start: alive={p.is_alive()}")
    p.start()
    log.info(f"after start: alive={p.is_alive()}, PID={p.pid}")
    p.join()
    log.info(f"after join: alive={p.is_alive()}")


    # ================================================
    # exitcode - 0 = success
    # ================================================
    log.info("--- exitcode ---")
    p = mp.Process(target=short_worker, name="Worker2")
    p.start()
    p.join()
    log.info(f"exit code: {p.exitcode}")


    # ================================================
    # join() with timeout - don't wait forever
    # ================================================
    log.info("--- join with timeout ---")
    p = mp.Process(target=long_worker, name="Slowpoke")
    p.start()
    
    log.info("waiting up to 2 seconds")
    p.join(timeout=2)
    
    if p.is_alive():
        log.info("didn't finish in time, terminating")
        p.terminate()
        p.join()


    # ================================================
    # terminate() - force stop (no cleanup)
    # ================================================
    log.info("--- terminate() ---")
    p = mp.Process(target=long_worker, name="Stubborn")
    p.start()
    time.sleep(1)
    log.info("calling terminate()")
    p.terminate()
    p.join()
    log.info(f"exit code: {p.exitcode}")    # negative = killed


    # ================================================
    # Graceful shutdown with Event - the proper way
    # ================================================
    log.info("--- graceful shutdown with Event ---")
    stop_event = mp.Event()
    
    p = mp.Process(target=cooperative_worker, args=(stop_event,), name="Polite")
    p.start()
    
    time.sleep(2)
    log.info("setting stop event")
    stop_event.set()
    p.join()
    log.info(f"exit code: {p.exitcode}")    # 0 = clean