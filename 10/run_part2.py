from functools import reduce
from typing import Iterable


def readfile():
    f = open("10/input.txt","r")
    lines = f.readlines()
    sums=[]
    for line in lines:
        errorsum = calculateError(line)
        if (errorsum!=None):
            sums.append(errorsum)
            
    sums.sort()
    middle=int((len(sums)-1)/2)
    print(sums)
    return sums[middle]
    
def calculateError(line):
    chars=list(line)
    
    chunks=[]
    index=0
    for char in chars:
        
        if char in ['{','[','(','<']:
            chunks.append(Chunk(char))   
        if char in ['}',']',')','>']:
            currentchunk=chunks.pop()
            wantedendchar = currentchunk.wantedendchar
            if (wantedendchar!=char):
                return None
        index+=1
    
    
    if len(chunks)>0:
        score=0
        completionstring=""
        while len(chunks)>0:
            chunk=chunks.pop()
            completionstring+=chunk.wantedendchar
            charscore=getScore(chunk.wantedendchar)
            score=score*5
            score=score+charscore
        print(completionstring+" - {} points".format(score))
        return score

def getScore(char):
    if char==')': return 1
    if char==']': return 2
    if char=='}': return 3
    if char=='>': return 4

class Chunk:

    def __init__(self,char):
        self.char=char
        if char=='{': self.wantedendchar='}'
        if char=='[': self.wantedendchar=']'
        if char=='(':self.wantedendchar=')'
        if char=='<':self.wantedendchar='>'
        
t=readfile()
print(t)