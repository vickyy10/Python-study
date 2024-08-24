class outer:
    def __init__(self):
        print("hi im outer class object creation")

    class inner:
        def __init__(self):
            print("hi im inner class object creation")

        def m1(self):
            print("hi im inner class")

O=outer()
i=O.inner()
i.m1()
