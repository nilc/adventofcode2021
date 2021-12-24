from math import degrees
import numpy as np
from scipy.spatial.transform import Rotation as R
from itertools import permutations,combinations
from os import read

class Scanner:
    beacons:list
    addvector:list
    flip:list
    switch:list
    matched:False
    id:str

    def __init__(self,id) -> None:
        self.beacons=[]
        self.beaconsFromZero=[]
        self.id=id
        self.matched=False    



def readScannerFile(file):
    scanners=[]
    f = open("19/"+file,"r")
    lines = f.readlines()
    matris=None
    for line in lines:
        line=line.strip()
        if line.startswith("--"):
            matris=Scanner(line.replace("-",""))
        elif len(line)==0:
            scanners.append(matris)
            matris=None
        else:
            matris.beacons.append(list(map(lambda p: int(p),line.split(","))))
            
    if (matris!=None):
        scanners.append(matris)
    print(scanners)
    return scanners

def rotateMatrix(matrice,flipaxix,switchaxix): 
    rotated=[]
    for vector in matrice:
        newvector=[vector[0],vector[1],vector[2]]
        for [axix,switch] in switchaxix:
            newvector[axix]=vector[switch]
        for [axix,flip] in flipaxix:
            newvector[axix]=newvector[axix]*flip
        rotated.append(newvector)
    return rotated


def matchMatrice(matriceCompare,matriceToTry):
    unique=set()
    for v in matriceToTry:
        for vCompare in matriceCompare:
            vectorToMatch=[]
            for i in range(3):
                delta=vCompare[i]-v[i]
                vectorToMatch.append(delta)
            #if max(vectorToMatch)<=1000 and min(vectorToMatch)>=-1000:
            unique.add("{},{},{}".format(vectorToMatch[0],vectorToMatch[1],vectorToMatch[2]))
    for u in unique:
        yield list(map(lambda t: int(t),u.split(",")))

def addToMatrice(matriceToAdd,addv):
    
    return list(map(lambda v:[v[0]+addv[0],v[1]+addv[1],v[2]+addv[2]],matriceToAdd))


def flipAndSwitchAxix():
    switching=[
    [0,1,2],
    [1,0,2],
    [1,2,0],
    [2,1,0],
    [0,2,1],
    [2,0,1],
    ]
    flipping=[
    [1,1,1],
    [-1,1,1],
    [1,-1,1],
    [1,1,-1],
    [-1,-1,1],
    [1,-1,-1],
    [-1,1,-1],
    [-1,-1,-1],
    ]
    for [sx,sy,sz] in switching:
        for [fx,fy,fz] in flipping:
            
                    switch = filter(lambda s: s[0]!=s[1],[[0,sx],[1,sy],[2,sz]])
                    flip = filter(lambda s: s[1]==-1,[[0,fx],[1,fy],[2,fz]])
                    
                    #aset.add((switch,flip))
                    
                    yield(list(switch),list(flip))
                        

def compareScanners(wanted,scannertomatch):
    matched=[]
    for wv in wanted:
        for scmv in scannertomatch:
            if (wv==scmv): matched.append(wv)
    return matched


def test():    
    fit = [[686,422,578]]
    fitRotated=rotateMatrix(fit,[[0,-1],[2,-1]],[])
    result=addToMatrice(fitRotated,[68,-1246,-43])
    assert result==[[-618,-824,-621]]
    #assert distanceVector([0,0,0],[1,1,1])==2

scanners=readScannerFile("input.txt")
zeroscanner=scanners[0]
zeroscanner.matched=True
zeroscanner.beaconsFromZero=zeroscanner.beacons
scannertomatch=scanners[1]
matched=False
count=0
test()
# find matrices match with m0
# find 
flipandswitch = list(flipAndSwitchAxix())
unique=[]
for f in flipandswitch:
    if f not in unique: unique.append(f)
print(unique,len(unique))
while len(list(filter(lambda p:p.matched==False,scanners)))>0:
    for matchscanner in filter(lambda p:p.matched==True,scanners):
        print("Matching with:"+matchscanner.id)
        wantedscanner=matchscanner.beacons
        for scannertomatch in filter(lambda p:p.matched==False,scanners):
            print("matching {} with {}".format(scannertomatch.id,matchscanner.id))
            for (switch,flip) in unique:
                rotated=rotateMatrix(scannertomatch.beacons,flip,switch)
                for addVector in matchMatrice(wantedscanner,rotated):
                    count+=1
                    if (count%100000==0): print("count:{}".format(count))
                    matriceWithAdded = addToMatrice(rotated,addVector)
                    matchedVectors=compareScanners(wantedscanner,matriceWithAdded)
                    if len(matchedVectors)>=12:
                        scannertomatch.matched=True
                        scannertomatch.beacons=matriceWithAdded
                        scannertomatch.beaconsFromZero=matriceWithAdded
                        scannertomatch.addVector=addVector
                        scannertomatch.flip=flip
                        scannertomatch.switch=switch
                        print("Found matching {} -> {} addv:{} switchflip:{}".format(scannertomatch.id,matchscanner.id,addVector,(switch,flip)))

allbeacons=set()
for b in scanners:
    for beacon in b.beaconsFromZero:
        allbeacons.add("{}".format(beacon))
print(allbeacons)
print(len(allbeacons))




            