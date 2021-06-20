import queue
import time
import random

from concurrent.futures import ThreadPoolExecutor

from threading import Thread

counter = 0
job_queue = queue.Queue()
counter_queue = queue.Queue()


def increment_manager():
    global counter
    while True:
        print(f"{__name__} in increment_manager start")
        time.sleep(random.random())

        increment = counter_queue.get()  # this waits until an item is available and locks the queue
        old_counter = counter
        counter = old_counter + increment
        job_queue.put((f"New counter value: {counter}", "----------------"))  # values should be added as a tuple in queue
        counter_queue.task_done()

        print(f"{__name__} in increment_manager finish")
        time.sleep(random.random())


# printer_manager and increment_manager run continuously because of the `daemon` flag.
Thread(target=increment_manager, daemon=True).start()  # allows program to shutdown when threads marked as daemon are
# alive, otherwise program will still be running as last threads will be waiting for queue values


def printer_manager():
    while True:
        print(f"{__name__} in printer_manager start")
        time.sleep(random.random())

        # print(*job_queue.get(), sep="\n")
        for line in job_queue.get():
            print(line)
        job_queue.task_done()

        print(f"{__name__} in printer_manager finish")
        time.sleep(random.random())


# printer_manager and increment_manager run continuously because of the `daemon` flag.
Thread(target=printer_manager, daemon=True).start()


def increment_counter():
    print(f"{__name__} in increment_counter start")
    time.sleep(random.random())

    counter_queue.put(1)

    print(f"{__name__} in increment_counter finish")
    time.sleep(random.random())


with ThreadPoolExecutor(max_workers=10) as pool:
    [pool.submit(increment_counter) for _ in range(10)]

# worker_threads = [Thread(target=increment_counter) for _ in range(10)]
#
# for thread in worker_threads:
#     thread.start()
#
# for thread in worker_threads:
#     thread.join()

counter_queue.join()  # wait for counter_queue to be empty
job_queue.join()  # wait for job_queue to be empty
