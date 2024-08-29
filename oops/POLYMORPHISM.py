"""Yourself is best example of polymorphism.In front of Your parents You will have one type of
behaviour and with friends another type of behaviour.Same person but different behaviours at
different places,which is nothing but polymorphism."""

#operator

# a=10
# b=20
# print(a+b) #arithematic operation

# a='helo'
# b='haai'
# print(a+b) #string concantiation






#functions

# x=[1,2,3,4,5,6]

# y={"a":10, True:3 , "c":30, "g":45}

# z={1,2,3,4,5} 

# print(len(x),len(y),len(z))    # here len function performed differently for different datatype    







#class 






# method over riding

# class A:
#     def m1(slef):
#         print("m1 method form A class")

# class B(A):
#     def m1(slef):
#         print("m1 method form B class")


# obj=B()
# obj.m1()








# method overloading

# class A():
    
#     def m1(self,a,b):
#         return a+b
        
#     def m1(self,a): #this will exicute 
#         return a

# obj=A()

# print(obj.m1(10,20)) # this will show an error





# constructor overloading

# class A():
    
#     def __init__(self,a,b,c):
#         print(a,b,c)
        
    
        
# class B(A):
    
#     def __init__(self,d,e,f):
        
#         super().__init__(d,e,f) #calling constructor fro
        
# obj=B(1,2,3)




# duck typing

# class A():
#     def m1(self):
#         print("heyyyyyyyyyyyyy")

# class B():
#     def m1(self):
#         print("helooooooooooooooo")


# def f(clss):
#     clss.m1()


# obj1=A()
# obj2=B()


# f(obj1)
# f(obj2)