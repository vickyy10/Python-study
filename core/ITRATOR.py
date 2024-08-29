#  we can itrate value intividualy from an itrable
# list1=[1,2,3,4,5,6,7]

# n=iter(list1)

# print(next(n))
 

#  creating with class 




class EvenNumber:

    def __init__(self,limit) :
        self.limit=limit
        self.num=0

    def __iter__(self):
        return self
    
    def __next__(self):

        if self.num < self.limit:
            rslt=self.num
            self.num+=2

            return rslt  
        else:
            StopIteration

        
    
obj=EvenNumber(20)

print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())



