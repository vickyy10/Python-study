list1=[11,2,3,4,5,6,7]

condition= lambda x: x%2 == 0

print(all(condition(x) for x in list1))