from abc import ABC, abstractmethod

# class vehile(ABC):
#     def __init__(self,n):
#         self.no_tyre=n
        
#     @abstractmethod
#     def start(self):
#         pass

# class bike(vehile):
#     def __init__(self):
#         self.no_tyre=2

#     def start(self):
#         print("start with kick")

# class scootye(vehile):
#     def __init__(self):
#         self.no_tyre=2

#     def start(self):
#         print("start with self")

# class car(vehile):
#     def __init__(self):
#         self.no_tyre=4

#     def start(self):
#         print("start with key")


# v=car()

# bike().start()










class A(ABC):

    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(a)

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass


class B(A):


    def m1(self):
        print("eafrwsrf")
    def m2(self):
        print("hello")


obj=B(20,30)

obj.m1()

