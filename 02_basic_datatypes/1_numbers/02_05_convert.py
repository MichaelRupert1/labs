'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
# Convert int to float
a = 9
print(a)
print(type(a))
a = float(a)
print(a)
print(type(a))
print("\n")
# convert float to an int
a = 420.0
print(a)
print(type(a))
a = int(a)
print(a)
print(type(a))
print('\n')

# Perform floor division using a float and an int.largest whole value/ no decimal
a = 21.//2.2
print(a)
print(type(a))
a = 15//4
print(a)
print(type(a))

# Use two user inputted values to perform multiplication.
a1 = int(input('input a number \n\t--->'))
a2 = int(input('input a number \n\t--->'))
mult = (a1*a2)**3
mult = str(mult)
a1 = str(a1)
a2 = str(a1)
print(f'{a1} times {a2} raised to the cube of 3 is {mult}.')