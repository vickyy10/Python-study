def m(n):
    c=0
    while c<n:
        yield c
        c+=1




g=m(10)


for i in range(20):

    print(next(g))



def all_even():
    n=0
    while True:
        yield n
        n +=2
        
        
for i in all_even():
    print(i)