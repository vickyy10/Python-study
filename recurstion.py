def recursion(n):
    if n <= 1:
        return n
    else:
        return n + recursion(n-1)


fuc=recursion(10)
print(fuc)