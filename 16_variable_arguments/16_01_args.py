'''
Write a script with a function that demonstrates the use of *args.

'''


def print_weather(*args):
    for i in args:
        print(i)


print_weather('sunny', 'cloudy', 'windy', 'rainy')
