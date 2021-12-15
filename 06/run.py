from typing import Iterable


def readfile():
    f = open("06/test.txt","r")
    lines = f.readlines()
    initialstate=lines[0].split(",")
    lanternfish=list(map(lambda t:int(t),initialstate))
    
    for day in range(1,256+1):
        newfishes=[]
        newstate=[]
        for fish in lanternfish:
            if fish==0:
                newfishes.append(8)
                newstate.append(6)
            else:
                newstate.append(fish-1)
        lanternfish=newstate        
        lanternfish.extend(newfishes)
        print("After {} days:{}".format(day,len(lanternfish)))
    return len(lanternfish)    
t=readfile()
print(t)