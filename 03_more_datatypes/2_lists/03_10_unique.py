'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = []
bad_list = []
for i in list_:
    if i not in unique_list:
        unique_list.append(i)
    else:
        bad_list.append(i)
        unique_list.remove(i)
print(unique_list)
