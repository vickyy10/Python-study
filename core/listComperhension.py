# list_1=['he',10,20,40,'hello','ooi']

# new_list1=[item for item in list_1 if isinstance(item, int)]

# print(new_list1)

num_list=[1,2,3]
s="abc"

tup_list=[(i,j) for i in num_list for j in s]

print(tup_list)