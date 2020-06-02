'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

word_list = []

with open('words.txt', 'r') as words:
    for word in words.readlines():
        word = word.strip()
        word_list.append(word)

    print(f"The shortest word is {min(word_list, key=len)}")
    print(f"The longest word is {max(word_list, key=len)}")
    print(f"The total amount of words in this file is {len(word_list)}")
