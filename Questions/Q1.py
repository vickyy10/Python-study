# reverse  a list

# list1=[1,2,3,4,5,6,7]
# list2=['hey','helolo','haaai']

# list2.reverse()

# list1.reverse()

# print(list1)
# print(list2)


# acsessiing by index

# list1=[[1,2,3],[["a",'b','c'],1,4,2]] 
# print(list1[1][0][1])

# to count

# list1=[1,2,3,4,5,5,5,5,5,5,6,7,9,]

# y=list1.count(5)
# print(y)


# extend

# list1=[1,2,3,4,5,6,7,8]

# set2={0,"f","g","k"}

# list1.extend(set2)
# print(list1)




# index

# list1=[1,2,3,34,4,5]

# print(list1.index(34))


# insert

# l=[[[[]]]]

# l[0][0][0].insert(0,"sethu")

# print(l)


# pop

# l=["hei","helo","oooi"]

# print(l.pop(2)) #it returs the value

# l.remove("hei")

# print(l)





# sort

# def f(e):
#     return len(e)

# l=["hei","heloooooo","1"]

# l.sort(key=f)

# print(l)













# prime number


# list_1 = list(range(1,50))

# new_list = []

# for i in list_1:
#     list2=[]
    
#     for j in range(1,(i//2)+1):
#         if i%j == 0:
#             list2.append(i)
            
#     if len(list2)<=1:
#         new_list.append(i)
            
# print(new_list)




# palindrome



# s1="malayalam"

# k=s1[::-1]

# if s1== k:
#     print("palindrome")
    
# else:
#     print("its no palindrome")





# anagram



# s1="haayai"

# s2='ayahai'

# if sorted(s1) == sorted(s2):
#     print("it is angaram")



# duplicates in list

# l=[1,2,3,4,5,6,2,3,4]

# for i in l:
#     l.remove(i)
#     if i in l:
#         print(i)







# duplicates in string



# l="abcdecab"

# rslt=set()

# for i in l:
#     if i in rslt:
#         print(i)

#     else:
#         rslt.add(i)



# enumerate

# l=[9,8,7,67,56,5,4,3,2]

# for i,j in enumerate(l):
#     print(f"index:{i} value:{j} ")


# vowels 



l = ["helo", "heeiei", "mishal", "yasin","k"]

s="aeiouAEIOU"



for i in l:
    vow_l=[j for j in i if j in s ]

    if vow_l:
        print(f"vowels in  {i} : {''.join(vow_l)}")

    else:
        print(f"no vowvels in {i}")


# l="jiask"

# for i in l:
#     if i in ("a","e","i","o","u"):

#         print(f"vowels in {l}: {i}")




# fibinocci series



# def fun(limit):

#     rslt=[0,1]

#     while True:
#         num=rslt[-1] + rslt[-2]

#         if num<limit:
#             rslt.append(num)

#         else:
#             break
#     return rslt

    

# limit=100
# print(fun(limit))




# factorial 


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# l=[1,2,3,4,5,6,7]


# print(list(map(factorial,l)))









# star pyramid

num =5
for i in range(1,num+1):
    print(" " * (num-i) + "*" * (2*i-1))





















