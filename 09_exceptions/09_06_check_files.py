'''
Read in the first number from 'integers.txt' and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'

number = int(input("Please enter a number: "))
try:
    with open(file_name, 'r') as integers:
        for integer in integers.readline():
            first = integer[0]
except ValueError as ve:
    print(ve)
except IOError as ioe:
    print(ioe)
else:
    result = first * number
    print(result)
