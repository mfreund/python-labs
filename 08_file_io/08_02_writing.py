'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

word_list = []
reversed_list = []

with open('words.txt', 'r') as words:
    for word in words.readlines():
        word_list.append(word)

with open('words_reverse.txt', 'w') as reversed_words:
    for word in reversed(word_list):
        reversed_words.write(word)
