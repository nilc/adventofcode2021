from functools import reduce
from typing import Iterable
from copy import deepcopy

class polymer:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
        self.combo=str(p1+p2)

    def __str__(self) -> str:
        return self.combo

class chain:

    def __init__(self,stringchain):
        self.chain=[]
        self.line=stringchain
        chars=list(stringchain)
        for i in range(len(chars)-1):
            self.addpolymer(chars[i],chars[i+1])


    def addpolymer(self,p1,p2):
        self.chain.append(polymer( p1,p2))

    def __str__(self) -> str:
        return str(list(map(lambda p:str(p),self.chain)))

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
                achain=chain(line)
    
    print(achain)
    
    print("Template:\t {}".format(achain.line))
    for i in range(1,11):
        newchain="".join(map(lambda index_poly:dorule(rules,index_poly[0],index_poly[1]),enumerate(achain.chain)))
        if (i%1==0):
            print("After step {} chainlength:{}".format(i,newchain))
        achain=chain(newchain)
    count={}
    for c in list(achain.line):
        if (c not in count):
            count[c]=0
        count[c]=count[c]+1
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