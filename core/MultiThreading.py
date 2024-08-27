import threading

def print_numbers():
    for  i in [1,2,3,4,5]:
        print(i)



def print_letters():
    for i in ['a','b','c','d','e']:
        print(i)


t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

t1.start()
t2.start()
