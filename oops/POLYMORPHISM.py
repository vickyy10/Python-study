"""Yourself is best example of polymorphism.In front of Your parents You will have one type of
behaviour and with friends another type of behaviour.Same person but different behaviours at
different places,which is nothing but polymorphism."""

#operator

a=10
b=20
print(a+b) #arithematic operation

a='helo'
b='haai'
print(a+b) #string concantiation

#functions

x=[1,2,3,4,5,6]

y={"a":10, True:3 , "c":30, "g":45}

z={1,2,3,4,5} 

print(len(x),len(y),len(z))    # here len function performed differently for different datatype    

#class 

class kerala:

    def speak(self):
        print("we speak malayalam")

class tamilnadu:

    def speak(self):
        print("we speak Thamil")

kerala= kerala()

kerala.speak

tamilnadu=tamilnadu()
tamilnadu.speak()


# method over riding

class A:
    def m1(slef):
        print("m1 method form A class")

class B(A):
    def m1(slef):
        print("m1 method form B class")

class C(A):
    def m1(slef):
        print("m1 method form C class")

obj=C()
obj.m1()

