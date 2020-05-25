'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]
new_list = []
for i in list_:
    if i not in new_list:
        new_list.append(i)
print(new_list)

# or

new_list = list(set(list_))
print(new_list)
