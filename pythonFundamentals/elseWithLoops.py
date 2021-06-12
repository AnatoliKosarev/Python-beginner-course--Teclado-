from math import sqrt

dividend = int(input("Please enter a number: "))

# Grab numbers one at a time from the range sequence
for divisor in range(2, dividend):
    # If user's number is divisible by the current divisor, break the loop
    if dividend % divisor == 0:
        print(f"{dividend} is not prime!")
        break
else:
    # This line only runs if no divisors produced integer results
    print(f"{dividend} is prime!")

# In the case of for loops, the else block executes if the main loop wasn't terminated by either a break statement,
# or an exception. For while loops, the else block runs when the loop condition evaluates to False at the start
# of a new iteration. If a break statement is encountered, or an exception occurs, the loop condition doesn't
# get checked again, so both of these cases prevent the else clause from running, just like with for loops.

dividend = int(input("Please enter a number: "))
divisor = 2

# Keep looping until the divisor equals the number we're testing
while divisor < dividend:
    # If user's number is divisible by the curent divisor, break the loop
    if dividend % divisor == 0:
        print(f"{dividend} is not prime!")
        break

    # Increment the divisor for the next iteration
    divisor = divisor + 1
else:
    # This line only runs if no divisors produced integer results
    print(f"{dividend} is prime!")

#--------------------------------------------------------------

"""
Convert the user input to an integer value and check the user's age is
over 18 if the conversion is successful. Otherwise, print an error message.
"""
try:
    age = int(input("Enter your age: "))
except:
    print("Please only enter numerical characters.")

# The else block only runs if no exception gets raised
else:
    if age < 18:
        print("Sorry, you're too young to watch this movie.")
    else:
        print("Enjoy the movie!")

#------------------------------------------------------------------------
for n in range(2, 101):
    x = 2
    # проверяем до делителя квадрат которого больше проверяемого числа n, т.к.
    # у любого составного числа есть собственный (то есть не равный 1) делитель, не превосходящий квадратный корень из этого составного чила
    while x**2 <= n:
        if n % x == 0:
            print(f"{n} equals {x} * {n // x}")
            break
        x += 1
    else:
        print(f"{n} is a prime number")