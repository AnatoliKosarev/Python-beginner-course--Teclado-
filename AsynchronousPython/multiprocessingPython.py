import time
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor

"""
each process can have at least 1 thread, running separately from another process's threads
for IO + CPU -  use multi threading, because process might not have the desired IO resource
for CPU tasks - use multi processes, because threads will do concurrently, processes will do simultaneously in each core
each process has its own GIL (global interpreter lock) 
"""


def ask_user():
    start_time = time.time()
    name = input("Enter your name: ")
    greet = f"Hello, {name}"
    print(greet)
    print(f"ask_user: {time.time() - start_time}")


def complex_calculation():
    start_time = time.time()
    print("Starting calculating...")
    [x ** 2 for x in range(20000000)]
    print(f"complex_calculation: {time.time() - start_time}")


process1 = Process(target=complex_calculation)
process2 = Process(target=complex_calculation)
process3 = Process(target=complex_calculation)

if __name__ == "__main__":  # for windows OS only (no forking in Windows)
    process1.start()
    process2.start()
    process3.start()

    start = time.time()

    process1.join()
    process2.join()
    process3.join()

    print(f"three processes: {time.time() - start}")
