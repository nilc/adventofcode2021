from os import read
import re
from typing import Literal
from dataclasses import dataclass
from typing import Union
import json
import math
@dataclass
class SnailfishPair:
    x:any
    y:any
    
    parent:any = None


    def magnitude(self):
        magnitude=0
        if type(self.x)==int:
            magnitude+=3*self.x
        else:
            magnitude+=3*self.x.magnitude()
        if type(self.y)==int:
            magnitude+=self.y*2
        else:
            magnitude+=2*self.y.magnitude()
        return magnitude

    def lowestIndexInPair(self):
        return min(filter(lambda k:k!=None,[self.indexx,self.indexy]))

    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
        self.indexx=None
        self.indexy=None
        
    def isOnlyRegularNumbers(self):
        return type(self.x)==int and type(self.y)==int

    def countParent(self):
        count=0
        parent=self.parent
        while(parent!=None):
            count+=1
            parent=parent.parent
        return count
    

    
    def explode(self,lp,rp):
        if (lp!=None):
            if lp.indexx==self.indexx-1:
                lp.x=lp.x=lp.x+self.x
            else:
                lp.y=lp.y+self.x    
        if (rp!=None):
            if rp.indexy==self.indexy+1:
                rp.y=rp.y+self.y
            else:
                rp.x=rp.x+self.y
        if (self.parent.x==self):
            self.parent.x=0
        elif self.parent.y==self:
                self.parent.y=0
        else:
            print("Could not find me..")
    
    def split(self):
        toBesplit="x"
        if (type(self.x)!=int or self.x<=9):
            toBesplit="y"
        new_var = getattr(self,toBesplit)
        x=math.floor(new_var/2)
        y=math.ceil(new_var/2)
        splittedPair = SnailfishPair(x,y)
        splittedPair.parent=self
        setattr(self,toBesplit,splittedPair)
        

    def __str__(self) -> str:
        return "[{},{}]".format(self.x,self.y)

def readfile():
    f = open("18/input.txt","r")
    lines = f.readlines()
    acc=sumLines(lines)
    print("The magnitude is:{}".format(acc.magnitude()))
    getHighestSum(lines)

def toSnailfishPair(line) -> SnailfishPair: 
    jsonarrs=json.loads(line.strip())
    return toSnailfish(jsonarrs)

def toSnailfish(arr) -> SnailfishPair:
    [x,y]=arr
    if type(x)==int and type(y)==int:
        return SnailfishPair(x,y)
    else:
        if type(x)==int and type(y)!=int:
            return SnailfishPair(x,toSnailfish(y))
        if type(x)!=int and type(y)==int:
            return SnailfishPair(toSnailfish(x),y)
        if type(x)!=int and type(y)!=int:
            return SnailfishPair(toSnailfish(x),toSnailfish(y))

def sumLines(lines):
    acc=""
    for line in lines:
        snailfish = toSnailfishPair(line)
        iterateReduce(snailfish)
        if len(acc)>0:
            acc="[{},{}]".format(acc,snailfish)
            #print("after addition:\t{}".format(acc))
            acc=str(iterateReduce(toSnailfishPair(acc)))
            #print("summed: {}".format(acc))
        else: acc=str(snailfish)
    return toSnailfishPair(acc)

def getHighestSum(lines):
    magnitudes=[]
    for x in range(len(lines)):
        for y in range(len(lines)):
            if y!=x:
                magnitude = sumLines([lines[x],lines[y]]).magnitude()
                magnitudes.append(magnitude)
    print("max magnitude:{}".format(max(magnitudes)))

def iterateReduce(snailfish):
    allpairs=[]
    iterateSnailfish(snailfish,allpairs)
        
    while reducePair(allpairs)>0:
        allpairs=[]
        iterateSnailfish(snailfish,allpairs)
    return snailfish

def reducePair(allpairs:list[SnailfishPair]):

    toexplodelist=list(filter(lambda p:p.isOnlyRegularNumbers()==True and p.countParent()==4,allpairs))
    toexplodelist.sort(key= lambda p: p.lowestIndexInPair())
    #print(list(map(lambda p:"x:{} y:{} p.countParent():{} lowest:{}".format(p.x,p.y,p.countParent(),p.lowest()),toexplodelist)))
    changed=False
    if len(toexplodelist)>0: 
        toexplode:SnailfishPair=toexplodelist[0]
        lv=next(filter(lambda p:p.indexx==toexplode.indexx-1 or p.indexy==toexplode.indexx-1,allpairs),None)
        rv=next(filter(lambda p:p.indexy==toexplode.indexy+1 or p.indexx==toexplode.indexy+1,allpairs),None)
        toexplode.explode(lv,rv)
        changed+=1
        #print("after explode:\t{}".format(snailfish))
    else:
        tosplitlist=list(filter(lambda p:p.indexx!=None and p.x>=10 or p.indexy!=None and p.y>=10,allpairs))
        tosplitlist.sort(key= lambda p: p.lowestIndexInPair())
        #print(list(map(lambda p:"split x:{} y:{} p.countParent():{} lowest:{}".format(p.x,p.y,p.countParent(),p.lowest()),tosplitlist)))
        if len(tosplitlist)>0 and changed==0: 
            tosplit=tosplitlist[0]
            tosplit.split()
            changed+=1
    #    print("after split  :\t{}".format(snailfish))
    return changed

numindex=0
def iterateSnailfish(snailfish,allpairs):
    global numindex
    allpairs.append(snailfish)
    x=snailfish.x
    y=snailfish.y
    arr=[x,y]
    count=0
    for s in arr: 
        if type(s)!=int:
            s.parent=snailfish
            if (count==0):
                snailfish.indexx=None
            else:
                snailfish.indexy=None
            iterateSnailfish(s,allpairs)
        else:
            numindex+=1
            if (count==0):
                snailfish.indexx=numindex
            else:
                snailfish.indexy=numindex
        count+=1



def test():
    doreduceTest("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]","[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
    doreduceTest("[[6,[5,[4,[3,2]]]],1]","[[6,[5,[7,0]]],3]")
    doreduceTest("[[[[[9,8],1],2],3],4]","[[[[0,9],2],3],4]")
    doreduceTest("[7,[6,[5,[4,[3,2]]]]]","[7,[6,[5,[7,0]]]]")
    doreduceTest("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]","[[3,[2,[8,0]]],[9,[5,[7,0]]]]")
    doreduceTest("[[[[4,0],[5,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]","[[[[4,0],[5,4]],[[0,[7,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]")
    doreduceTest("[[[[4,0],[5,4]],[[7,0],[15,5]]],[10,[[11,0],[[9,3],[8,8]]]]]","[[[[4,0],[5,4]],[[7,0],[15,5]]],[10,[[11,9],[0,[11,8]]]]]")
    iterateReduceTest("[[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]],[7,[5,[[3,8],[1,4]]]]]","[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]")
def doreduceTest(jsonstr,wanted):
    sp=toSnailfishPair(jsonstr)
    allpairs=[]
    iterateSnailfish(sp,allpairs)
    reducePair(allpairs)
    print("{} reduced to:{}".format(jsonstr,sp))
    assert str(sp) == wanted

def iterateReduceTest(jsonstr,wanted=None):
    sp=toSnailfishPair(jsonstr)
    print("after addition: {}".format(sp))
    sp=iterateReduce(sp)
    print(str(sp))
    if (wanted!=None):
        assert str(sp) == wanted
    return sp

test()

readfile()