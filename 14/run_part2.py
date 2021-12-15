from functools import reduce
from typing import Iterable
from copy import deepcopy
from enum import Enum

def readfile():
    f = open("14/input.txt","r")
    lines = f.readlines()
    
    starting=None
    rules={}
    achain=None
    for line in lines:
        
        line = line.strip()
        if (len(line)>0):
            if "->" in line:
                rule=line.split("->")
                rules[rule[0].strip()]=rule[1].strip()
            else:    
                achain=list(line)
    
    lastchar=achain[len(achain)-1]
    counter={}
    for k in rules.keys(): counter[k]=0        
    for l in range(0,len(achain)-1):
        poly = achain[l]+achain[l+1]
        counter[poly]=counter[poly]+1
    print(achain)
    
    print("Template:\t {}".format(achain))
    for i in range(1,41):
        thiscounter={}
        for k in rules.keys(): thiscounter[k]=0
        for poly in counter.keys():
            numberofpolys = counter[poly]
            if numberofpolys>0:
                middle=rules[poly]
                chars = list(poly)
                newpoly = middle+chars[1]
                newpoly1 = chars[0]+middle
                thiscounter[newpoly]=thiscounter[newpoly]+numberofpolys
                thiscounter[newpoly1]=thiscounter[newpoly1]+counter[poly]
        counter=thiscounter
        print("After step {} counter:{}".format(i,counter))
    count={}
    print(counter)
    for k in counter.keys():
        c=list(k)[0]
        if (c not in count):
            count[c]=0
        count[c]=count[c]+counter[k]
    
    count[lastchar]=count[lastchar]+1

    maxoc=max(count.values())
    minoc=min(count.values())
    return maxoc-minoc
        

def dorule(rules, index, poly):
    middle=rules[poly.combo]
    if index==0:
        return poly.p1+middle+poly.p2
    else:
        return middle+poly.p2
t=readfile()
print(t)