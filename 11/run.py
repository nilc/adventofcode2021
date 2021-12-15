from functools import reduce
from typing import Iterable


def readfile():
    f = open("11/input.txt","r")
    lines = f.readlines()
    sum=0
    matrice=[]
    for line in lines:
        newmatriceline=[]
        for stage in list(line.strip()):
            newmatriceline.append(int(stage))
        matrice.append(newmatriceline)    

    count=0
    print("Before any steps:")
    print(printMatrice(matrice))
    
    for step in range(1,1000+1):
        flashed=stageUp(matrice)
        for (x,y) in flashed:
            matrice[y][x]=0
            count+=1
        print("After step:{} flashed:{}".format(step,len(list(flashed))))
        print(printMatrice(matrice))
        if (len(flashed))==100:
            print("All flashed")
            return step
    return count
def printMatrice(matrice):
    output=""
    for l in matrice:
        output+="".join(map(lambda i:str(i),l))+"\n"
    return output

def allAbove9(matrice):
    above9=set()
    for y in range(0,len(matrice)):
        for x in range(0,len(matrice[y])):
            if (matrice[y][x]>9):
                above9.add((x,y))
    return above9
def stageUp(matrice):
    
    flashed=set()
    for y in range(0,len(matrice)):
        for x in range(0,len(matrice[y])):
            matrice[y][x] = matrice[y][x]+1
            
    newflash=allAbove9(matrice)
    
    while len(newflash)>0:
        print(newflash)
        #print(printMatrice(matrice))
        oldflash=allAbove9(matrice)
        for (flashx,flashy) in newflash:
            adjacentPositions = getAdjacentPos(flashx,flashy,matrice)
            for (x,y) in adjacentPositions:
                matrice[y][x] = matrice[y][x]+1
        
        flashednow=allAbove9(matrice)
        newflash=flashednow.difference(oldflash)       
    return allAbove9(matrice)


def getValue(matrice,x,y):
    if x<0 or y<0 or y>=len(matrice):
        return None
    if x>=len(matrice[y]):
        return None
    return matrice[y][x]


def getAdjacentPos(x, y, matrice):
    cordstotest=[
            (x-1,y),
            (x+1,y),
            (x,y-1),
            (x,y+1),
            (x+1,y+1),
            (x-1,y+1),
            (x+1,y-1),
            (x-1,y-1)
            ]
    cordstotest=filter(lambda xy: getValue(matrice,xy[0],xy[1])!=None,cordstotest)
    return list(cordstotest)


t=readfile()
print(t)