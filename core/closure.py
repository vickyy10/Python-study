
def outer():
    x=3
    def inner():
        print(x)
    inner()

outer()
