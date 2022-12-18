#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while(my_list[i]):
            i+=1
    except IndexError:
       pass
    
    try:
        if (x > i or x < i):
            raise IndexError
        else:
            for index in  range(x):
                print("{}".format(my_list[index]),end="")        
        print("\nnb_print: {:d}".format(i))
    except IndexError:
        for index in  range(i):
            print("{}".format(my_list[index]),end="")
        print("\nnb_print: {:d}".format(i))