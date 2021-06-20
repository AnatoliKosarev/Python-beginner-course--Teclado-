import time
from threading import Thread


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

####### SINGLE THREAD
# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print(f"Single thread total time: {time.time() - start}")


####### TWO THREADS


# With two threads, we can do them both at once...
thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()
thread1.start()
thread2.start()
thread1.join()  # main thread waits for thread1 to finish
thread2.join()  # main thread waits for thread2 to finish
print(f"Two threads total time: {time.time() - start}")