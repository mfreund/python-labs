'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

number = int(input("Enter a number: "))

def double(number):
    return number*2

def square(number):
    return double(number)**2

def divide3(number):
    return square(number)/3

print(double(number))
print(square(number))
print(divide3(number))


