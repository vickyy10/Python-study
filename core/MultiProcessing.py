from multiprocessing import Process

def print_numbers():
    for  i in [1,2,3,4,5]:
        print(i)



def print_letters():
    for i in ['a','b','c','d','e']:
        print(i)


if __name__ == '__main__':
    p1 = Process(target=print_numbers)
    p2 = Process(target=print_letters)

    p1.start()
    p2.start()