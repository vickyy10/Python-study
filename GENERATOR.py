def m(n):
    c=0
    while c<5:
        yield c
        c+=1





g=m(5)

for i in range(20):

    print(g)


