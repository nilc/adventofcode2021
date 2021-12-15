from typing import Iterable


def readfile():
    f = open("05/input.txt","r")
    lines = f.readlines()
    lines=filter(lambda l:len(l)>1,lines)
    inputs=list(map(lambda line:handeline(line),lines))
    i=0
    overlap2=0
    overlaps=set()
    points=set()
    for l in inputs:
        for point in l.points:
            if (point in points and point not in overlaps): overlaps.add(point)
            points.add(point)

    print("points:{}".format(len(points)))
    print("overlaps:{}".format(len(overlaps)))
    #comparestupd(inputs, i, overlap2, points)
    #print(overlap2)

def comparestupd(inputs, i, overlap2, points):
    for pos in points:
        if i%1000==0: print("test i:{} of points {}".format(i,len(points)))
        i+=1
        # print(str(pos))
        hits=list(filter(lambda line:line.isOnPos(pos),inputs))
        if (len(hits)>1):
            print(" y hit on pos:"+str(pos))
            overlap2+=1

def handeline(line:str):
    [start,end]=line.split(" -> ")
    [sx,sy]=start.split(",")
    [ex,ey]=end.split(",")
    startPos=Pos(sx,sy)
    endPos=Pos(ex,ey)
    print(line)
    return Line(startPos,endPos)





class Pos:
    def __init__(self,x,y) -> None:
        self.y=int(y)
        self.x=int(x)


    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    

    def __hash__(self) -> int:
        return hash((self.y,self.x))
    
    def __str__(self):
        return "x:{},y:{}".format(self.x,self.y)

def rangeM(s,e) -> range:
    if (s>e): return range(s,e-1,-1) 
    return range(s,e+1)

class Line:
    def __init__(self,start:Pos,end:Pos) -> None:
        self.start=start
        self.end=end
        self.points=[]
        if (self.end.x==self.start.x):
            for y in rangeM(self.start.y,self.end.y):
                self.points.append(Pos(self.start.x,y))

        if (self.end.y==self.start.y):
            for x in rangeM(self.start.x,self.end.x):
                self.points.append(Pos(x,self.start.y))
        
        if (self.points==[]):
            xs=rangeM(self.start.x,self.end.x)
            ys=rangeM(self.start.y,self.end.y)
            
            for index in range(0,len(xs)):
                # print("xlen:{},ylen:{}".format(len(xs),len(ys)))
                x = xs[index]
                y = ys[index]
                self.points.append(Pos(x,y))

        print("s:{},end:{},points:{}".format(self.start,self.end,len(self.points)))


    def __str__(self):
        return "start:{},end:{}".format(self.start,self.end)
    
    def isOnPos(self,pos:Pos) -> bool:
        #for p in self.points:
        #    if (p.x==pos.x and p.y==pos.y):
        #        return True
        if pos in self.points:
            return True
        return False
        
l1=handeline("0,9 -> 2,9")
l2=handeline("1,4 -> 1,9")
pos = Pos(1,9)
r1=l1.isOnPos(pos)
r2=l2.isOnPos(pos)
t=readfile()
print(t)

