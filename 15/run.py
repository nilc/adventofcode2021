from functools import reduce
from typing import Iterable
from copy import deepcopy
from multiprocessing import Pool

class Path:

    def __init__(self):
        self.chain=set()
        self.risk=0

    def __init__(self,chain,risk):
        self.chain=chain
        self.risk=risk


    def addpath(self,pos,risk):
        self.chain.add(pos)
        self.risk+=risk

    def havevisited(self,pos):
        if (pos in self.chain):
            return True
        return False

    def __str__(self) -> str:
        s = "risk:"+str(self.risk)+" Path:"+str(list(map(lambda p:str(p),self.chain)))
        return s

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
        for pos in [(x,y+1),(x+1,y),(x-1,y),(x,y-1)]:
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

    def isEnd(self,pos):
        return pos==self.endpos

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
    matrice[0][0]=0
    amap=Map(matrice)
    
    print(amap.printMatrice())
    global bestpath
    global testcount
    #print(amap.minCost(amap.matrice,amap.endpos[0],amap.endpos[1]))

    bestpath=testfirst(amap)
    ibest=None
    print("bestpath:{}".format(str(bestpath)))
    ibest=iteratePaths(amap, (0,0), Path(set(),0))
    print("ibestpath:{}".format(str(ibest)))
    print("bestpath:{}".format(str(bestpath)))
    print("testcount:{}".format(testcount))
bestpath=None
testcount=0
throwedaway=0
bestroutepos={}

def iteratePaths(amap, pos, path):
    global bestpath
    global testcount
    global throwedaway
    global bestroutepos
    testcount+=1
    if testcount%1000000==0:
        print("testcount:{} throwedaway:{} bestpath:{}".format(testcount,throwedaway,bestpath))
        print("Pos:{} Path:{}".format(pos,path))
    risk=amap.getValue(pos)
    path.addpath(pos,risk)
    # print("Pos:{} Path:{}".format(pos,path))
    
        
    if (pos not in bestroutepos):
        bestroutepos[pos]=path.risk+1
    if (path.risk<bestroutepos[pos] and path.risk<bestpath.risk):
        bestroutepos[pos]=path.risk
        if amap.isEnd(pos):
            if (path.risk<bestpath.risk):
                bestpath=path
                print("bestpath:{}".format(str(bestpath)))
                return path    
        posToTest = filter(lambda t:path.havevisited(t)==False,amap.getAdjacentPos(pos))
        for newpos in posToTest:
            if path.havevisited(newpos)==False:
                newpath=Path(set(path.chain),path.risk)
                iteratePaths(amap,newpos,newpath)
    else:
        throwedaway+=1

def testfirst(amap):
    path=Path(set(),0)
    isatend=False
    nextpos=(0,0)
    while(isatend==False):
        pos=list(filter(lambda f:path.havevisited(f)==False,amap.getAdjacentPos(nextpos)))
        minrisk=None
        if (len(pos)==0):
            testpos=(nextpos[0],nextpos[1]+1)
            minrisk=amap.getValue(testpos)
            if (minrisk==None):
                testpos=(nextpos[0]+1,nextpos[1])
                minrisk=amap.getValue(testpos)
            nextpos=testpos
        else:
            minrisk=min(map(lambda p:amap.getValue(p),pos))
            
            for p in pos:
                if amap.getValue(p)==minrisk:
                    nextpos=p
        path.addpath(nextpos,minrisk)
        isatend=amap.isEnd(nextpos)
    return path
t=readfile()
print(t)