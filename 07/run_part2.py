from typing import Iterable


def readfile():
    f = open("07/input.txt","r")
    lines = f.readlines()
    initialstate=lines[0].split(",")
    crabs=list(map(lambda t:int(t),initialstate))
    endpos=max(crabs)
    startpos=min(crabs)
    print("spos:{},epos:{}",startpos,endpos)
    minfuel=999999999999
    bestpos=None
    for pos in range(startpos,endpos+1):
        sum=0
        while sum<minfuel:
            for crabpos in crabs:
                fuel_to_walk = calcFuelNeeded(pos, crabpos)
                sum+=fuel_to_walk
            if (sum<minfuel):
                print("better sum on pos: {} fuel:{}".format(pos,sum))
                minfuel=sum
                bestpos=pos    
    return [bestpos,minfuel] 

def calcFuelNeeded(pos, crabpos):
    length_to_walk=abs(pos-crabpos)
    fuel_to_walk=0
    for num in range(0,length_to_walk+1):
        fuel_to_walk+=num
    return fuel_to_walk
t=readfile()
print(t)