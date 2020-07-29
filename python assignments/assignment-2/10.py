import functools
#first decorator
def upper_decorate(func):
    @functools.wraps(func)
    def inner():
        return func().upper()
    return inner
#second decorator
def split_decorate(func):
    @functools.wraps(func)
    def inner():
        return func().split()
    return inner

@split_decorate
@upper_decorate
def print_str():
    return 'hello world'

print(print_str())