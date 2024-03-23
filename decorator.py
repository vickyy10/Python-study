def upper_decor(fun):
    def wrapper(x):
        result = fun(x)
        return result.upper()
    return wrapper

@upper_decor
def hello_name(name):
    return 'hello'+name



print(hello_name("mishal"))