from functools import reduce
from typing import Iterable
from copy import deepcopy

class graph:

    def __init__(self):
        self.connections={}

    def addConnections(self,start,end):
        
        if start not in self.connections:
            self.connections[start]=set()
        self.connections[start].add(end)
        if (start!="start" and end!="end"):
            if end not in self.connections:
                self.connections[end]=set()
            self.connections[end].add(start)

class Path:
    
    def __init__(self,startstep):
        self.visitedSmall=set()
        self.visited=[startstep]
        self.ended=False
    
    def addStep(self,step):
        if (step=="start"):
            return False
        if step=="end":
            self.visited.append(step)
            self.ended=True
            return True
        else:
            if step.islower():
                if step in self.visitedSmall:
                    return False
                else:
                    self.visitedSmall.add(step)
                    self.visited.append(step)
            else:
                self.visited.append(step)

def readfile():
    f = open("12/input.txt","r")
    lines = f.readlines()
    thegraph=graph()
    for line in lines:
        [start,end]=line.strip().split("-")
        thegraph.addConnections(start,end)
    
    startcon=thegraph.connections["start"]
    paths=[]
    for con in startcon:
        apath = Path("start")
        apath.addStep(con)
        iteratePath(con, paths,apath,thegraph)
    distinctpaths=set()
    for path in paths:
        distinctpaths.add(",".join(path.visited))
    print(distinctpaths)
    print(len(distinctpaths))

def iteratePath(startcon, paths,apath,thegraph):
    conns=thegraph.connections[startcon]
    for con in conns:
        newpath=deepcopy(apath)
        result=newpath.addStep(con)
        if (newpath.ended):
            paths.append(newpath)
        else:
            if result!=False:
                iteratePath(con,paths,newpath,thegraph)

t=readfile()
print(t)