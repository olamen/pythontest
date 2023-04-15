import numpy as np
a = [2,4,6,3,5,6,2,4]

def uniquelist(list1):
    list2 = set(list1)
    list3 = list(list2)
    for x in list3 :
        print(x)
uniquelist(a)


