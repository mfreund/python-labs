'''
Write a script with a function that demonstrates the use of **kwargs.

'''


def name_age(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


name_age(name='Mikiko', age='23')
