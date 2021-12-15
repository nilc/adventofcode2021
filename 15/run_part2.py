from functools import reduce
from typing import Generator, Iterable, Tuple
from copy import deepcopy
from multiprocessing import Pool
import sys

class Map:

    def __init__(self,matrice) -> None:
        self.matrice=matrice
        wantedy=len(self.matrice)-1
        wantedx=len(self.matrice[wantedy])-1
        self.endpos=(wantedx,wantedy)

    def printMatrice(self):
        output=""
        for l in self.matrice:
            output+="".join(map(lambda i:str(i),l))+"\n"
        return output

    def getAdjacentPos(self, pos):
        x=pos[0]
        y=pos[1]
        totest=[]
        testcands = [(x,y+1),(x+1,y),(x-1,y),(x,y-1)]
        
        if (y==self.endpos[1]):
            testcands=[(x,y+1),(x+1,y)]
        for pos in testcands:
            if (self.getValue(pos)!=None):
                totest.append(pos)
        return totest    
            

    def getValue(self,pos):
        x=pos[0]
        y=pos[1]
        if x<0 or y<0 or y>=self.endpos[1]+1:
            return None
        if x>=self.endpos[0]+1:
            return None
        return self.matrice[y][x]

def readfile():
    f = open("15/input.txt","r")
    lines = f.readlines()
    
    matrice=[]
    for sline in lines:
        line=[]
        matrice.append(line)
        sline = sline.strip()
        if (len(sline)>0):
            for c in list(sline): line.append(int(c))
    
    tc = duplicateMap(matrice)
    amap=Map(tc)
    
    print(amap.printMatrice())
    
    bestpathrisk=nonRecIteratePath(amap)
    print("testcount:{}".format(testcount))
    return bestpathrisk

def duplicateMap(matrice):
    amap=Map(matrice)
    
    orgxlen = len(matrice[0])-1
    orgylen = len(matrice)-1
    tc = [[0 for x in range((orgxlen+1)*5)] for x in range((orgylen+1)*5)]
    for y in range(len(tc)):
        for x in range(len(tc)):
            value=amap.getValue((x,y))
            if (value!=None): tc[y][x]=value
            else:
                if (x>orgxlen and y>orgylen):
                    copivalue = tc[y][x-(orgxlen+1)]+1
                    if (copivalue>9):
                        copivalue=1
                    tc[y][x]=copivalue
                if (x>orgxlen and y<=orgylen):
                    copivalue = tc[y][x-(orgxlen+1)]+1
                    if (copivalue>9):
                        copivalue=1
                    tc[y][x]=copivalue
                if ((x<=orgxlen and y>orgylen)):
                    copivalue = tc[y-(orgylen+1)][x]+1
                    if (copivalue>9):
                        copivalue=1
                    tc[y][x]=copivalue
    return tc

testcount=0

def nonRecIteratePath(amap:Map):
    global testcount
    bestroutepos={}
    start=(0,0)
    frontier=[(0,start)]
    bestroutepos[(0,0)]=0
    while frontier:
        testcount+=1
        if (testcount%10000==0):
            print("testcount:{}".format(testcount))
        _,xy = frontier.pop()
        poses=amap.getAdjacentPos(xy)
        for newpos in poses:
            cost=amap.getValue(newpos)+bestroutepos[xy]
            if newpos not in bestroutepos or cost<bestroutepos[newpos]:
                bestroutepos[newpos]=cost
                frontier.append((cost,newpos))
                frontier.sort(reverse=True)
    return bestroutepos[amap.endpos]     
                
t=readfile()
print(t)