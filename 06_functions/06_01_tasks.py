'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
def divide4o7(number):
    if number % 4 == 0 or number % 7 == 0:
        return True
    else:
        return False


# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def divide4a7(number):
    if number % 4 == 0 and number % 7 == 0:
        return True
    else:
        return False


# take in a number from the user between 1 and 1,000,000,000
number = int(input("Please enter a number between 1 and 1,000,000,000: "))

# call your functions, passing in the user input as the arguments, and set their output equal to new variables
result1 = divide4o7(number)
result2 = divide4a7(number)

# print your new variables to display the results
print(result1)
print(result2)