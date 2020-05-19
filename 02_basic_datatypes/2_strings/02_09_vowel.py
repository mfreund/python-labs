'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

sentence = input("Enter a sentence: ")
vowel = input("Enter a vowel: ")
count = sentence.count(vowel)
print("the number of " + vowel + "'s in the sentence is " + str(count))


counts = {i:0 for i in 'aeiou'}
for char in sentence:
    if char in counts:
        counts[char] += 1

for k,v in counts.items():
    print(k, v)
