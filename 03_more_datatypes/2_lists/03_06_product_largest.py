'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
numbers_list = []
for numbers in range(10):
    numbers = int(input("Please enter a number: "))
    numbers_list.append(numbers)
    numbers += 1
numbers_list.sort()
print(numbers_list[-1])

result = 1
for i in numbers_list:
    result = result * i
print(result)
