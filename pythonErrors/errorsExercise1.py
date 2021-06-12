def count_from_zero_to_n(n):
    if n < 0:
        raise ValueError(f"Only positive values are accepted as parameters, you passed {n}")
    for x in range(0, n+1):
        print(x)


n = input()
count_from_zero_to_n(int(n))