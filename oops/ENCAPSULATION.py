class encap:
    __a=20 #private variable

    def display(self):
        print("welcome")
        print(self.__a) #we can only acsess private variable inside the class 


obj=encap()
obj.display()

# print(obj.a) here we cant acsess the a variable beacuse a is private