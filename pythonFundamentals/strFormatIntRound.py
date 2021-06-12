from math import floor, trunc, ceil

test = "HEllo, wOrlD! "
print(test.lower())
print(test.upper())
print(test.capitalize())
print(test.title())
print(test.strip().lower())
print()

name = 'bob'
s = 'hello {name} {surname}'

print(f"hello {name}")
print(s.format(name='bob', surname='coup'))
print(s.format(name='mike', surname='smith'))

name = "Rolf Smith"
street = "123 No Name Road"
postcode = "PY10 1CP"
address = f"""Name: {name}
Street: {street}
Postcode: {postcode}
Country: United Kingdom"""
print(address)

n = 3.01
print(ceil(n)) # to the top, floor() - to the bottom

x = 4863.4255091
print(f'{x:.6}')
print('{:.6}'.format(x))
print(f"{x:.3f}")
print(f"{x:f}") # 6 digits of precision after decimal point by default

x2 = 4862.5
print(round(x2)) # banker's rounding - to closest even number when float with a tie (2.5, 3.5 etc.)

print(f"{x:,}")
print(f"{x:_}")
print(f"{x:_.3f}")

questions = 30
correct_answers = 23
print(f"you got {correct_answers / questions :.2%} questions correct") # format as % number of digits after decimal point

