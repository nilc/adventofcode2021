from typing import Iterable


def readfile():
    f = open("07/input.txt","r")
    lines = f.readlines()
    initialstate=lines[0].split(",")
    crabs=list(map(lambda t:int(t),initialstate))
    endpos=max(crabs)
    startpos=min(crabs)
    minfuel=999999999999
    bestpos=None
    for pos in range(startpos,endpos+1):
        sum=0
        for crabpos in crabs:
            sum+=abs(pos-crabpos)
        if (sum<minfuel):
            print("better sum on pos: {} fuel:{}".format(pos,sum))
            minfuel=sum
            bestpos=pos    
    return [bestpos,minfuel] 
t=readfile()
print(t)