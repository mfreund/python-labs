'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

input = input("Please enter a sentence: ")
x = input.split()
result = tuple(x)
result_list = []
for i in result:
    result_list.append(tuple(i))
print(result_list)
