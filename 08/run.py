from functools import reduce
from typing import Iterable


def readfile():
    f = open("08/input.txt","r")
    lines = f.readlines()
    outputs=reduce(list.__add__,map(lambda l:l.split("|")[1].strip().split(" "),lines))
    counts={}
    for i in range(0,10):
        counts[i]=0
    for output in outputs:
        if len(output)==3:
            counts[7]+=1
        if len(output)==2:
            counts[1]+=1
        if len(output)==4:
            counts[4]+=1
        if len(output)==7:
            counts[8]+=1    
    sum=0
    print(counts)
    for key in counts:
        sum+=counts[key]
    return sum
t=readfile()
print(t)