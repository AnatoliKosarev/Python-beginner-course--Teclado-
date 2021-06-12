# Define a PrimeGenerator class
class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop  # stop defines the range (exclusive upper bound) in which we search for the primes
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):  # always search from current start (inclusive) to stop (exclusive)
            x = 2
            while x ** 2 <= n:
                if n % x == 0:  # not prime
                    break
                x += 1
            else:  # n is prime, because we've gone through the entire loop without having a non-prime situation
                self.start = n + 1  # next time we need to start from n + 1, otherwise we will be trapped on n
                return n  # return n for this round
        raise StopIteration  # this is what tells Python we've reached the end of the generator


prime_c = PrimeGenerator(100)

print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
print(next(prime_c))
