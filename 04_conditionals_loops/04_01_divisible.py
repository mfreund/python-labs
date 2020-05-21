'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

number = int(input("Enter a number between 1 and 1,000,000,000: "))
if number % 3 == 0:
    print(str(number) + " is divisible by 3!")
else:
    print(str(number) + " is not divisible by 3!")
