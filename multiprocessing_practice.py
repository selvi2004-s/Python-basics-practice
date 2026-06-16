# ================================================
# (ep 49) MULTIPROCESSING - for CPU-heavy work
# Spawns separate Python processes (bypasses the GIL)
# ================================================
from multiprocessing import Process


def cpu_heavy(n):
    """Pretend this is real heavy work."""
    total = 0
    for i in range(n):
        total += i ** 2
    print(f"Done: total = {total}")


# IMPORTANT on Windows/macOS - must wrap in if __name__ == '__main__'
# Otherwise multiprocessing can spawn infinite processes
if __name__ == "__main__":
    print("\n--- Multiprocessing ---")
    
    p = Process(target=cpu_heavy, args=(1_000_000,))
    p.start()
    p.join()
    
    
    # ================================================
    # (ep 50) Multiple processes - same idea as threads
    # ================================================
    print("\n--- Multiple processes ---")
    processes = []
    for n in [500_000, 800_000, 1_200_000]:
        p = Process(target=cpu_heavy, args=(n,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    print("All processes done")
