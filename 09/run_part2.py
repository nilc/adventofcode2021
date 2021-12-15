from functools import reduce
from os import X_OK
from typing import Iterable


def readfile():
    heigthmap = getHeightMap()
    lowestpoints=[]
    for y in range(0,len(heigthmap)):
        line=heigthmap[y]
        for x in range(0,len(line)):
            islowest=findLowestPoint(heigthmap, y, x)
            if (islowest):lowestpoints.append([x,y])                
    basinsizes=[]
    for [x,y] in lowestpoints:
        score=findBasinSize(heigthmap, y, x)
        basinsizes.append(score)
    basinsizes.sort(reverse=True)
    return basinsizes
    

def getHeightMap():
    f = open("09/input.txt","r")
    lines = f.readlines()
    
    heigthmap=[]
    for line in lines:
        line=line.strip()
        ls=list(map(lambda l:int(l),list(line)))
        heigthmap.append(ls)
    print(heigthmap)
    
    return heigthmap

def findBasinSize(heigthmap, y1, x1):
    print("testing x:{} y:{}".format(x1,y1))
    basinsize=1
    copyheightmap=[]
    for line in heigthmap:
        copyline=[]
        copyheightmap.append(copyline)
        for l in line:
            copyline.append(l)

    #copyheightmap[y1][x1]=None
    foundNew=True
    newcordstotest=[]
    basincords=set([Pos(x1,y1,copyheightmap[y1][x1])])
    cordstotest = getAdjacentPos(y1, x1, copyheightmap)
    while foundNew:
        foundNew=False
        for pos in newcordstotest:
            newpos = getAdjacentPos(pos.y,pos.x,copyheightmap)
            for pos in newpos:
                cordstotest.append(pos)
        newcordstotest=set()
        print("corsttotest:{}".format(cordstotest))
        for [x,y] in cordstotest:
            if copyheightmap[y][x]!=9:
                
                newTest = Pos(x,y,copyheightmap[y][x])
                if (newTest not in basincords): 
                    newcordstotest.add(newTest)
                    basincords.add(Pos(x,y,copyheightmap[y][x]))
                    foundNew=True
        cordstotest=[]
        
    print("done x:{} y:{} basinsize:{} basincord:{}".format(x1,y1,len(basincords),list(map(lambda t:str(t),basincords))))
    return len(basincords)

def getAdjacentPos(y, x, copyheightmap):
    cordstotest=[
            [x-1,y],
            [x+1,y],
            [x,y-1],
            [x,y+1]]
    cordstotest=filter(lambda arrpos: getValue(copyheightmap,arrpos[0],arrpos[1])!=None,cordstotest)
    return list(cordstotest)

class HeigthMap:

    def __init__(self,lines) -> None:
        self.pos=[]
        for y in range(0,len(lines)):
            for x in range(0,len(lines[y])):
                self.pos.append(Pos(x,y,lines[y][x]))    
    
    def visualize(self):
        for row in self.pos:
            for val in row:
                print('{:4}'.format(val))
        print


class Pos:

    def __init__(self,x,y,value):
        self.x=x
        self.y=y
        self.value=value

    def markInBasin(self):
        self.inbasin=True

    def __eq__(self, __o: object) -> bool:
        return self.x==__o.x and self.y==__o.y

    def __hash__(self) -> int:
        return hash((self.x,self.y))

    def __str__(self) -> str:
        return "x:{} y:{} v:{}".format(self.x,self.y,self.value)

def findLowestPoint(heigthmap, y, x):
    height=heigthmap[y][x]
    if (height==9):
        return False
    values=[]
    values.append(getValue(heigthmap,x-1,y))
    values.append(getValue(heigthmap,x,y-1))
    values.append(getValue(heigthmap,x+1,y))
    values.append(getValue(heigthmap,x,y+1))
        
    values = list(filter(lambda f: f!=None,values))
    if len(values)==0:
        return False
    lowestAdjecent=min(values)
    if lowestAdjecent>height:
        print("lowest x:{},y:{} value:{}".format(x,y,height))
        return True
    return False

def getValue(heightmap,x,y):
    if x<0 or y<0 or y>=len(heightmap):
        return None
    if x>=len(heightmap[y]):
        return None
    return heightmap[y][x]

m=getHeightMap()

poses=getAdjacentPos(0,9,m)
print(poses)

t=readfile()
print(t)
print(t[0]*t[1]*t[2])