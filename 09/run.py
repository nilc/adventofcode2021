from functools import reduce
from typing import Iterable


def readfile():
    f = open("09/inpute.txt","r")
    lines = f.readlines()
    
    heigthmap=[]
    for line in lines:
        line=line.strip()
        ls=list(map(lambda l:int(l),list(line)))
        heigthmap.append(ls)
    print(heigthmap)
    lowestpoint=0
    for y in range(0,len(heigthmap)):
        line=heigthmap[y]
        for x in range(0,len(line)):
            height=heigthmap[y][x]
            values=[]
            values.append(getValue(heigthmap,x-1,y))
            values.append(getValue(heigthmap,x,y-1))
            values.append(getValue(heigthmap,x+1,y))
            values.append(getValue(heigthmap,x,y+1))
            
            lowestAdjecent=min(filter(lambda f: f!=None,values))
            if lowestAdjecent>height:
                print("lowest x:{},y:{} value:{}".format(x,y,height))
                lowestpoint+=height+1
    
    print (lowestpoint)

def getValue(heightmap,x,y):
    if x<0 or y<0 or y>=len(heightmap):
        return None
    if x>=len(heightmap[y]):
        return None
    return heightmap[y][x]
t=readfile()
print(t)