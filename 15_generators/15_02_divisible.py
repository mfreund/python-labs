'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

number_list = (number for number in range(10000))

for number in number_list:
    if number % 1111 == 0:
        print(number)
