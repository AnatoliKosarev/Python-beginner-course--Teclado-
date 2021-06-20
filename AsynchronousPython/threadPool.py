import time
from concurrent.futures import ThreadPoolExecutor


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

# start = time.time()
# pool = ThreadPoolExecutor(max_workers=2)
# pool.submit(complex_calculation)
# pool.submit(ask_user)
# pool.shutdown()
# print(f"Two threads total time: {time.time() - start}")

start = time.time()
with ThreadPoolExecutor(max_workers=2) as pool:  # no need to pool.shutdown() with context manager (like with files <with open("file.txt", "r") as file:>)
    pool.submit(complex_calculation)
    pool.submit(ask_user)
print(f"Two threads total time: {time.time() - start}")
