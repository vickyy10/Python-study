# map function here the function will perform each element in the itrable
from functools import reduce



# map
def square(x):
    return x**2

list1=[1,2,3,4,5,6]
x=map(square,list1)
print(list(x))




# filter 
def even(x):
    return x % 2 == 0
list2=list(range(1,20))

z=filter(lambda x: x%2 == 0,list2)
print(list(z))


# reduce

num=[1,2,3,4,5,6,7,8,9,10]

def sum_num(x,y):
    return x+y

sum_numm=reduce(sum_num,num)
print(sum_numm)
