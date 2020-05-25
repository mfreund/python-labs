'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
sentence1 = input("Enter a sentence: ")
sentence2 = input("Enter a sentence: ")
sentence3 = input("Enter a sentence: ")

print(str(len(sentence1)) + ", " + sentence1)
print(str(len(sentence2)) + ", " + sentence2)
print(str(len(sentence3)) + ", " + sentence3)
