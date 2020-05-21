'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''

num = 0
while num <= 1000:
    if num % 5 == 0:
        print(num)
    num += 1