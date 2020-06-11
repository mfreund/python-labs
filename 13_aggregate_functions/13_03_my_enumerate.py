'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''
list = ['Hello', 'Bonjour', 'Hola']

def my_enumerate(list):
    final_list = []
    counter = 0
    for greeting in list:
        final_list.append((counter, greeting))
        counter += 1
    return final_list

print(my_enumerate(list))

# or

def my_enumerate2(list):
    for i in range(len(list)):
        print(f"({i}, {list[i]})")

print(my_enumerate2(list))
