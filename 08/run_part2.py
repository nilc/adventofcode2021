from functools import reduce
from typing import Iterable

def readfile():
    f = open("08/input.txt","r")
    lines = f.readlines()
    lineoutputs=[]
    for line in lines:
        linesegments=[]
        for word in line.strip().split(" "):
            correctword=sorted(word)
            linesegments.append(set(correctword))
        lineoutputs.append(linesegments)
    print(lineoutputs)

    
    sum=0
       
    for line in lineoutputs:
        codetable=getCode(line)
        lookuptable={}
        for key in codetable:
            value=str(codetable[key])
            lookuptable[value]=str(key)
        index=line.index(set("|"))
        outputstring=""
        for i in range(index+1,len(line)):
            new_var = line[i]
            new_var="".join(sorted(new_var))
            outputstring+=lookuptable[new_var]
        print(outputstring)
        sum+=int(outputstring)
    print(sum)
    return sum
def getCode(line):
    uniqueCodes=set()
    for word in line:
        joinedstring = "".join(word)
        uniqueCodes.add("".join(sorted(joinedstring)))

    #print(uniqueCodes)
    numberdict={}
    for i in range(0,10):
        numberdict[i]=None


    for output in line:
        if len(output)==3:
            addIfSame(numberdict,7,output)

        if len(output)==2:
            addIfSame(numberdict,1,output)
            
        if len(output)==4:
            addIfSame(numberdict,4,output)
            
        if len(output)==7:
            addIfSame(numberdict,8,output)
                
    for output in line:
        if len(output)==6:
            if output.issuperset(numberdict[4]):
                addIfSame(numberdict,9,output)
            else:
                if output.issuperset(numberdict[1]):
                    addIfSame(numberdict,0,output)
                else:    
                    addIfSame(numberdict,6,output)
    for output in line:
        if len(output)==5:
                lowerpartof1=numberdict[1].intersection(numberdict[6])
                if output.issuperset(numberdict[1])!=True and output.issuperset(lowerpartof1):
                    addIfSame(numberdict,5,output)
                else:
                    if output.issuperset(numberdict[1]):
                        addIfSame(numberdict,3,output)
                    else:
                        addIfSame(numberdict,2,output)          
    print("".join(uniqueCodes))
    print(numberdict)

    for t in numberdict:
        if (numberdict[t]!=None):
            joinedstring = "".join(numberdict[t])
            numberdict[t]="".join(sorted(joinedstring))
    for t in uniqueCodes:
        if t not in numberdict.values() and t != "|":
            print (t+" not in numberdict")
    
    print(numberdict)
    return numberdict

def addIfSame(table,index,value):
    if index in table:
        oldvalue=table[index]
        if oldvalue!=value and oldvalue!=None:
            print("diff values in keylookup: {}, old:{},new:{}".format(index,oldvalue,value))
        table[index]=value
    else: 
        table[index]=value    
t=readfile()
print(t)