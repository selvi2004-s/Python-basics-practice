# ================================================
# MULTIPROCESS POOL (ep 51)
# A managed group of worker processes
# Submit tasks, pool handles the rest
# ================================================
from multiprocessing import Pool
import logging
import time
import os


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(processName)-12s | %(message)s',
        datefmt='%H:%M:%S'
    )


# ================================================
# A worker function - takes one input, returns a result
# ================================================
def square(x):
    setup_logging()
    log = logging.getLogger()
    log.info(f"squaring {x} (PID {os.getpid()})")
    time.sleep(0.5)
    return x * x


# ================================================
# Main code
# ================================================
if __name__ == "__main__":
    setup_logging()
    log = logging.getLogger()

    # Create a pool of 4 workers
    # Submit a list of inputs - pool runs them in parallel
    # Get back a list of results in the same order
    with Pool(processes=4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5, 6, 7, 8])

    log.info(f"results: {results}")