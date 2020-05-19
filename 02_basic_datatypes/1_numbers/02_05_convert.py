'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

x = 10
x = float(x)
print(x)
x // 2
y = int(input("enter a number: "))
z = int(input("enter another number: "))
w = y * z
print(w)
