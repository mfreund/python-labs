'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
my_list = input("Please enter a list of numbers: ")
my_list = my_list.split()
my_list.sort()
tuple_list = []

if len(my_list) % 2 == 1:
    my_list.append('0')

for item in range(0, len(my_list), 2):
    tuple_list.append((my_list[item], my_list[item+1]))

for tuple in tuple_list:
    print(tuple)
