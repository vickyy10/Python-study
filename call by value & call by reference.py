# call by value

# a='hellooo'

# def main(x):
#     x='heyyyyy'
#     print(" x from inside" + x)


# main(a)

# print("a from outside" + a)


# call by reffernce

list1=[1,2,3,4,5]
def main2(list1):
    list1.append(100) 
    print(list1)
    
main2(list1)

print(list1)