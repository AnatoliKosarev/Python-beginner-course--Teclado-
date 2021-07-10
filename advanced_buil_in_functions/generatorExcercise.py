def prime_generator(bound):
    for n in range(2, bound):
        for x in range(2, n):
            if n % x == 0:
                break
        # else runs only if no breaks where encountered in for loop
        else:
            yield n


for prime in prime_generator(100):
    print(prime)


def optimized_prime_generator(bound):
    for n in range(2, bound):
        x = 2
        # проверяем до делителя квадрат которого больше проверяемого числа n, т.к.
        # у любого составного числа есть собственный (то есть не равный 1) делитель, не превосходящий квадратный корень из этого составного чила
        while x**2 <= n:
            if n % x == 0:
                break
            x += 1
        # else runs only if no breaks where encountered in while loop and while loop condition is false (x**2 > n)
        else:
            yield n


for opt_prime in optimized_prime_generator(100):
    print(opt_prime)