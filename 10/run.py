from functools import reduce
from typing import Iterable


def readfile():
    f = open("10/input.txt","r")
    lines = f.readlines()
    sum=0
    for line in lines:
        errorsum = calculateError(line)
        if (errorsum!=None):
            sum+=errorsum    
    return sum
    
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
                print("Expected: {},  but found {} instead. index:{}".format(wantedendchar,char,index))
                return getScore(char)
        index+=1

def getScore(char):
    if char==')': return 3
    if char==']': return 57
    if char=='}': return 1197
    if char=='>': return 25137

class Chunk:

    def __init__(self,char):
        self.char=char
        if char=='{': self.wantedendchar='}'
        if char=='[': self.wantedendchar=']'
        if char=='(':self.wantedendchar=')'
        if char=='<':self.wantedendchar='>'
        
t=readfile()
print(t)