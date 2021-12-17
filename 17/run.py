from os import read
import re
from typing import Literal



def runsimulation(xv,yv,targetarea):
    proj=Projectile(xv,yv)
    hieghest=0
    haspassed=False
    while haspassed==False:
        if (hieghest<proj.pos[1]):
            hieghest=proj.pos[1]
        if targetarea.hit(proj):
            print("Hit:{}".format(proj.pos))
            return (True,hieghest)
        lastpos=proj.pos
        proj.step()
        haspassed=hasPassed(proj,targetarea)
        if (haspassed):
            #print("Has passed:{}".format(proj.pos))
            return (False,hieghest)

def hasPassed(proj, targetarea):
    if proj.yv>0 and proj.pos[0]<targetarea.xmax:
            return False
    if proj.pos[0] > targetarea.xmax:
        return True
    if proj.pos[1] < targetarea.ymin:
        return True
    return False


class Projectile:
    
    def __init__(self,xv,yv) -> None:
        self.xv=xv
        self.yv=yv
        self.pos=(0,0)
    
    def step(self):
        self.pos=(self.pos[0]+self.xv,self.pos[1]+self.yv)
        if (self.xv!=0):
            self.xv+=-1
        self.yv+=-1

class TargetArea:

    def __init__(self,xmin,xmax,ymin,ymax) -> None:
        self.xmin=xmin
        self.xmax=xmax
        self.ymin=ymin
        self.ymax=ymax
        self.targetarea=set()
        for x in range(xmin,xmax+1):
            for y in range(ymin,ymax+1):
                self.targetarea.add((x,y))

    def hit(self,proj):
        return proj.pos in self.targetarea 

def findHeighest(targetArea):
    allworking=[]
    count=0
    hieghest=0
    bestv=None
    for y in range(-200,200):
        for x in range(int(0),targetArea.xmax*3): 
            count+=1
            (hit,heigth)=runsimulation(x,y,targetArea)
            if hit: 
                allworking.append((x,y))
                if heigth>hieghest:
                    hieghest=heigth
                    bestv=(x,y)
            if (count%10000==0): print("Count:{} bestv:{} height:{} allworking:{}".format(count,bestv,hieghest,len(allworking)))

    print("hieghest:{} v:{} allworking:{}".format(hieghest,bestv,len(allworking)))
    t=0
    for pos in allworking:
        print(pos)
        t+=1

input="x=269..292, y=-68..-44"
inputtest="x=20..30, y=-10..-5"

target=TargetArea(20,30,-10,-5)
targetReal=TargetArea(269,292,-68,-44)
assert runsimulation(20,-10,target)[0]==True
assert runsimulation(6,3,target)[0]==True

assert runsimulation(9,0,target)[0]==True
assert runsimulation(17,-4,target)[0]==False
assert runsimulation(6,9,target)==(True,45)

findHeighest(targetReal)
