'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = 5
i = 1
for i in range(n+1):
    print("*" * i)
    i += 1
