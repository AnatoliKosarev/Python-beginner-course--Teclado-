import time
from concurrent.futures import ProcessPoolExecutor

print(f"{__name__} line4")
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

print(f"{__name__} line19")
if __name__ == "__main__":
    print(f"{__name__} line21")
    with ProcessPoolExecutor(max_workers=3) as pool:
        print(f"{__name__} line23")
        start = time.time()
        print(f"{__name__} line25")
        pool.submit(complex_calculation)
        print(f"{__name__} line27")
        pool.submit(complex_calculation)
        print(f"{__name__} line29")
        pool.submit(complex_calculation)

print(f"{__name__} line32")
if __name__ == "__main__":
    print(f"{__name__} line34")
    print(f"three processes: {time.time() - start}")
print(f"{__name__} line36")
