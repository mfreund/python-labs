'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}



result = {}
my_keys = set(dict_1.keys()).union(set(dict_2.keys()))

for key in my_keys:
    value1 = dict_1.get(key,0)
    value2 = dict_2.get(key,0)
    result[key] = value1 + value2
print(result)
