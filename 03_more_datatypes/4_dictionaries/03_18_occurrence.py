'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
sentence = input("Please enter a string: ")
counts = {i:0 for i in sentence}
for char in sentence:
    if char in counts:
        counts[char] += 1

result = dict()
for k,v in counts.items():
    result[k] = v

print(result)
