def countdown(num):
    while num > 0:
        yield num
        num -= 1


"""
next() is cheaper than switching between threads
"""
tasks = [countdown(5), countdown(10), countdown(20)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        print(next(task))
        tasks.append(task)
    except StopIteration:
        print("Task finished")
