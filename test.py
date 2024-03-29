# tuple1=(1,2,3,4,5,6)

# tupl2=tuple1[:2]+(10,)+tuple1[3:]
# print(tupl2)

# x={7,3,4,1,9,2,5}

# y={"x":2,True:433,}
# print(y[1])


def m1(n):
    if n<=1:
        return n
    else:
        return n + m1(n-1)

print(m1(10))