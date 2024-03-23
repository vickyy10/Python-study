# map function here the function will perform each element in the itrable

def square(x):
    return x**2

list1=[1,2,3,4,5,6]
x=map(square,list1)
print(list(x))

# filter 
def even(x):
    return x % 2 == 0
list2=list(range(1,20))

z=filter(even,list2)
print(list(z))

# reduce


