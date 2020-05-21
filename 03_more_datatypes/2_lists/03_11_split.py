'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
from collections import Counter


sentence = input("Please enter a sentence: ")
x = sentence.split()
data = Counter(x)

# all_words = data.most_common()
# second_common = all_words[1]
# second_word = second_common[0]
# print(second_word)

print(data.most_common()[1][0])   # Returns all unique items and their counts
print(data.most_common(1)[0][0])  # Returns the highest occurring item

