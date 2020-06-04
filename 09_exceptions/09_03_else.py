'''
Write a script that demonstrates a try/except/else.

'''

sentence = input("Enter a sentence: ")

try:
    first = sentence[0]
    print(f"The first letter is {first}")
except IndexError as ie:
    print(ie)
else:
    print("No error found here")
