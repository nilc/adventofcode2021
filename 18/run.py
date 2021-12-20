from os import read
import re
from typing import Literal
from dataclasses import dataclass
from typing import Union
import json
import math
import uuid
@dataclass
class SnailfishPair:
    x: any
    y: any
    
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

    def lowest(self):
        return min(filter(lambda k:k!=None,[self.indexx,self.indexy]))

    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
        self.indexx=None
        self.indexy=None
        
    def isRegularNumbers(self):
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
        if type(self.x)==int and self.x>9:
            x=math.floor(self.x/2)
            y=math.ceil(self.x/2)
            self.x=SnailfishPair(x,y)
            self.x.parent=self
        else:
            x=math.floor(self.y/2)
            y=math.ceil(self.y/2)
            self.y=SnailfishPair(x,y)
            self.y.parent=self

    def __str__(self) -> str:
        return "[{},{}]".format(self.x,self.y)

def readfile():
    f = open("18/input.txt","r")
    lines = f.readlines()
    acc=sumLines(lines)
    print("The magnitude is:{}".format(acc.magnitude()))
    getHighestSum(lines)

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
        
    while reducePair(snailfish,allpairs)>0:
        snailfish=toSnailfishPair(str(snailfish))
        allpairs=[]
        iterateSnailfish(snailfish,allpairs)
    return snailfish

def reducePair(snailfish:SnailfishPair,allpairs:list[SnailfishPair]):

    toexplodelist=list(filter(lambda p:p.isRegularNumbers()==True and p.countParent()==4,allpairs))
    toexplodelist.sort(key= lambda p: p.lowest())
    #print(list(map(lambda p:"x:{} y:{} p.countParent():{} id:{} lowest:{}".format(p.x,p.y,p.countParent(),p.index,p.lowest()),toexplodelist)))
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
        tosplitlist.sort(key= lambda p: p.lowest())
        #print(list(map(lambda p:"split x:{} y:{} p.countParent():{} id:{} lowest:{}".format(p.x,p.y,p.countParent(),p.index,p.lowest()),tosplitlist)))
        if len(tosplitlist)>0 and changed==0: 
            tosplit=tosplitlist[0]
            tosplit.split()
            changed+=1
    #    print("after split  :\t{}".format(snailfish))
    return changed

numindex=0
def iterateSnailfish(snailfish,allpairs):
    global numindex
    #snailfish.index=len(allpairs)
    allpairs.append(snailfish)
    x=snailfish.x
    y=snailfish.y
    arr=[x,y]
    count=0
    for s in arr: 
        if type(s)!=int:
            s.parent=snailfish
            iterateSnailfish(s,allpairs)
        else:
            numindex+=1
            if (count==0):
                snailfish.indexx=numindex
            else:
                snailfish.indexy=numindex
        count+=1




def toSnailfishPair(line) -> SnailfishPair: 
    jsonarrs=json.loads(line.strip())
    return toSnailfish(jsonarrs)
index=0    
def toSnailfish(arr) -> SnailfishPair:
    global index
    index+=1
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

#readfile()
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
    reducePair(sp,allpairs)
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
#iterateReduceTest("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
test()
lines='''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]'''.splitlines()
lines2='''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''.splitlines()

#accfish=sumLines(lines2)
#print(accfish.magnitude())
#print(str(accfish))
#sp1=iterateReduceTest("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]")
#sp2=iterateReduceTest("[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]")
#spacc=iterateReduceTest("["+str(sp1)+","+str(sp2)+"]")
readfile()