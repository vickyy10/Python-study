
str1 = 'malayalam'

strlist = [x for x in str1]

def func():
    new = strlist.copy()
    new.reverse()

    if strlist == new:
        return True
    else:
        return False


print(func())