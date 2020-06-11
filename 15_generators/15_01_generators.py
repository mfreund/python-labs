'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

generator = (number for number in range(1,11))

for number in generator:
    print(number)
