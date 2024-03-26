def m(n):
    c=0
    while c<5:
        yield c
        c+=1





g=m(5)

print(next(g))
print(next(g))
print(next(g))