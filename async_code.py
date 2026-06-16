# ================================================
# ASYNC CODE (ep 52)
# One thread, many concurrent waiting tasks
# ================================================
import asyncio
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(message)s',
    datefmt='%H:%M:%S'
)


def display(msg):
    logging.info(msg)


# ================================================
# A coroutine - defined with `async def`
# Can be paused with `await`
# ================================================
async def work(name):
    display(f"{name} starting")
    await asyncio.sleep(1)        # pause this coroutine, let others run
    display(f"{name} finishing")


# ================================================
# Schedule many coroutines, wait for all
# ================================================
async def run_async(count):
    tasks = []
    for x in range(count):
        name = f"Item {x}"
        tasks.append(asyncio.ensure_future(work(name)))
    
    await asyncio.gather(*tasks)  # wait for all tasks to finish


# ================================================
# Main - run the event loop
# Modern Python (3.7+) uses asyncio.run()
# ================================================
if __name__ == "__main__":
    display("main started")
    asyncio.run(run_async(5))
    display("main ended")