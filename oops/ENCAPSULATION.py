class encap:
    __a=20 #private variable

    def display(self):
        print("welcome")
        print(self.__a) #we can only acsess private variable inside the class 


obj=encap()
obj.display()

# print(obj.a) here we cant acsess the a variable beacuse a is private
# we can acsess private variable outside by getter and setter method or name mangling method

print(obj._encap__a) #name mangling


# -----------------------------------------------------------------------------------------



class A:
    def __init__(self):
        self._protected_var = 10  # Protected attribute

class B(A):
    def display_protected_var(self):
        print(self._protected_var)  # Accessing protected attribute from subclass

obj = B()
obj.display_protected_var()  # Accessing protected attribute through subclass
