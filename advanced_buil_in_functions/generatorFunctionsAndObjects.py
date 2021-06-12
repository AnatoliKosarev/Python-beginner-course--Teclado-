def hundred_generator_function():
    number = 0
    while number < 100:
        yield number
        number += 1


# print(hundred_generator_function())
#
# g = hundred_generator_function()
# print(next(g))
# print(next(g))
#
# for n in hundred_generator_function():
#     print(n)


"""
All object with __next__() are called iterators 
All generators are iterators but not all iterators are generators (not all iterators are generating values)
e.g. some iterators can iterate existing list without generating any values, e.g. like listIterator
"""


class ListIterator:
    def __init__(self):
        self.list = [1, 2, 3, 4, 5]
        self.i = 0

    def __next__(self):
        if self.i < len(self.list):
            current = self.list[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration


list_iter = ListIterator()
print(next(list_iter))  # 1
print(next(list_iter))  # 2
print(next(list_iter))  # 3
print(next(list_iter))  # 4
print(next(list_iter))  # 5


class HundredGeneratorClass:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration

    # def __iter__(self):
    #     return self



print(HundredGeneratorClass())

gen_class = HundredGeneratorClass()
print(next(gen_class))
print(next(gen_class))

for n in HundredGeneratorClass():  # TypeError: 'HundredGeneratorClass' object is not iterable
    print(n)
