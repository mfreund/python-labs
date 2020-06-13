'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''


def tags(tag_name):
    def my_func(func):
        def inner_func(name):
            return f"<{tag_name}> {func(name)} </{tag_name}>"
        return inner_func
    return my_func


@tags(input("Enter a tag: "))
def get_text(name):
    return name


print(get_text(input("Enter a text: ")))
