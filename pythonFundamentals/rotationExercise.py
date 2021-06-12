from collections import deque

base = [1, 2, 3, 4, 5]
rotations = 3


def rotate(base_list, r):
    base_list = base_list.copy()
    number_of_rotations = abs(r) % len(base_list)

    if r < 0:
        for _ in range(number_of_rotations):
            base_list = base_list + [base_list.pop(0)]
    else:
        for _ in range(number_of_rotations):
            base_list = [base_list.pop()] + base_list

    return base_list


print(rotate(base, rotations))
deque_1 = deque([1, 2, 3, 4, 5])
deque_1.rotate(3)
print(deque_1)

print(rotate(base, -12))
deque_2 = deque([1, 2, 3, 4, 5])
deque_2.rotate(-12)
print(deque_2)
