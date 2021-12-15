from functools import reduce
from typing import Iterable
from copy import deepcopy

class pos:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class matrice:

    def __init__(self):
        self.dots=[]


    def adddot(self,x,y):
        self.dots.append(pos( int(x),int(y)))
    
    def countDots(self):
        count=0
        for l in self.matrice:
            for d in l:
                if d=="#": count+=1
        return count


    def creatematrice(self):
        maxy=max(map(lambda d: d.y,self.dots))
        maxx=max(map(lambda d: d.x,self.dots))
#        print("maxx:{},maxy:{}".format(maxx,maxy))
        self.matrice=[]
        for i in range(maxy+1):
            line=[]
            for x in range(maxx+1):
                line.append(".")
            self.matrice.append(line)
        for dot in self.dots:
 #           print("x:{},y:{}".format(dot.x,dot.y))
            self.matrice[dot.y][dot.x]="#"

    def foldx(self,x):

        print("foldx:{}".format(x))
        t=len(self.matrice[0])    
        
        tobefolded=filter(lambda d: d.x>x,self.dots)
        for dot in list(tobefolded):
            dot.x=x-(dot.x-x)
        self.creatematrice()
        

    # 1=14-7-6

    # y+foldy=
    # 2+y=

    def foldy(self,y):
        print("foldy:{}".format(y))
        t=len(self.matrice)    
        tobefolded=filter(lambda d: d.y>y,self.dots)
        for dot in list(tobefolded):
            dot.y=y-(dot.y-y)
        self.creatematrice()

    def __str__(self) -> str:
        linesstring = list(map(lambda line:"".join(str(line)).replace(", ","").replace("'",""),self.matrice))
        return "\n".join(linesstring)


def readfile():
    f = open("13/input.txt","r")
    lines = f.readlines()
    amatrice=matrice()
    folds=[]
    for line in lines:
        line = line.strip()
        if (len(line)>0):
            if line.startswith("fold"):
                foldinstructions=line.split("along ")[1]
                folds.append(foldinstructions)
            else:    
                [x,y]=line.split(",")
                amatrice.adddot(x,y)
    
    amatrice.creatematrice()
    #print(amatrice)
    for fold in folds:
        fold=fold.split("=")
        if fold[0]=="x":
            amatrice.foldx(int(fold[1]))
        if fold[0]=="y":
            amatrice.foldy(int(fold[1]))
        #print(amatrice)
        print(amatrice.countDots())
    print(amatrice)
t=readfile()
print(t)