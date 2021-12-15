from typing import Iterable


def readfile():
    f = open("06/input.txt","r")
    lines = f.readlines()
    initialstate=lines[0].split(",")
    lanternfish=list(map(lambda t:int(t),initialstate))
    
    lanternfishstates={8:0,7:0,6:0,5:0,4:0,3:0,2:0,1:0,0:0}
    for fish in lanternfish:
        lanternfishstates[fish]+=1
    print("initial state:{}".format(str(lanternfishstates)))    
    for day in range(1,256+1):
        newstate={8:0,7:0,6:0,5:0,4:0,3:0,2:0,1:0,0:0}
        for fishstate in lanternfishstates:
            if fishstate==0:
                newstate[8]=newstate[8]+lanternfishstates[0]
                newstate[6]=newstate[6]+lanternfishstates[0]
            else:
                newstage=fishstate-1
                newstate[newstage]=newstate[newstage]+lanternfishstates[fishstate]
        lanternfishstates=newstate
        sum = countfishes(lanternfishstates)
        print("After {} days:{}".format(day,sum))
    return countfishes(lanternfishstates) 

def countfishes(lanternfishstates):
    sum=0
    for fishstate in lanternfishstates:
       sum+=lanternfishstates[fishstate]
    return sum   
t=readfile()
print(t)