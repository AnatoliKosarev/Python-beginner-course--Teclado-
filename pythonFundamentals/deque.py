from collections import deque

base = deque([1, 2, 3])

x = base.pop()  # 3
base.appendleft(x)  # deque([3, 1, 2])

y = base.popleft()  # 3
base.append(y)  # deque([1, 2, 3])

base = deque([1, 2, 3])
base.rotate()  # deque([3, 1, 2])

base = deque([1, 2, 3, 4, 5])

# rotates base 2 steps to the left
base.rotate(-2)  # deque([3, 4, 5, 1, 2])

# rotates base 3 steps to the right
base.rotate(3)  # deque([5, 1, 2, 3, 4])

print(-12 // 5)  # because of floor division - стремится от нуля для отрицательных чисел, к 0 для положительных
print(-12 % 5)  # (x % y) = x - (x // y) * y: 3 = -12 - (-3) * 5 = - 12 + 15 = 3
