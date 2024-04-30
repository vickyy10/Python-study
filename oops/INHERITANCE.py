# single

# class A:
#     def m1(self):
#         print("m1 from class A")

# class B(A):
#     def m1(self):
#         print("m1 from class B")


# calling super classs

class A():
    def m1(self):
        print("A")
        
class B(A):
    def m1(self):
        print("B")
        
        
class C(B):
    def m1(self):
        print("C")
        
class D(C):
        
    def m1(self):
        super(B,self).m1()
        print("D")
        
        
D().m1()