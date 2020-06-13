'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''


def my_func(text):
    def inner_func():
        print("<p>" + text + "</p>")
    return inner_func


message = my_func("Hello")
message()
