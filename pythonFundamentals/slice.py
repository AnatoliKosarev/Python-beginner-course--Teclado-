# slicing
original_string = "Python"
sliced_string = original_string[0:3]
print(sliced_string)  # Pyt
sliced_string2 = original_string[:3]
print(sliced_string2)  # Pyt
sliced_string3 = original_string[3:]
print(sliced_string3)
sliced_string4 = original_string[3:-1]  # except the last one
print(sliced_string4)

s = slice(1, 4)
t = (1, 2, 3, 4, 5)  # tuple
l = [1, 2, 3, 4, 5]  # list
c = "12345"  # string
print(t[s])  # (2, 3, 4)
print(l[s])  # [2, 3, 4]
print(c[s])  # 234

# allows us to skip over values by providing a step greater than 1
t = (1, 2, 3, 4, 5)
print(t[1:4:2])  # (2, 4)
t = (1, 2, 3, 4, 5)
print(t[4:2:-1])  # (5, 4)


# we can use syntax like this to check if a sequence is a palindrome, for example:
def palindrome_check(word):
    if word == word[::-1]:  # check against full sequence in reverse order
        return True
    return False
print(palindrome_check("kayak"))  # True
print(palindrome_check("lemon"))  # False


# assigning values with slice()
numbers = [1, 3, 3]
numbers[1:2] = [2]
print(numbers)  # [1, 2, 3]
# However, assigning an integer would have raised a TypeError.

numbers = [1, 3, 5]
numbers[1:3] = [2, 3]
print(numbers)  # [1, 2, 3]

numbers = [1, 3, 5]
numbers[1:3] = [2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]

numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print(numbers)  # [1, 2, 3, 4, 5]
# Remember that a slice like [1:1] is totally valid, but completely empty. It starts at index 1, and ends at index 1,
# but the stop value is not inclusive, so the value at index 1 is not part of the slice.
# A slice like this therefore allows us to insert values at a given index without removing any values in the sequence.

numbers = [1, 3, 3, 5, 5]
numbers[1:4:2] = [2, 4]
print(numbers)  # [1, 2, 3, 4, 5]
# we assign 2 to index 1, and 4 to index 3

