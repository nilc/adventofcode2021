def countOnesAndZeros(lines,column):
    nozero=0
    noone=0
    for sline in lines:
        value=sline[column]
        if value=="0":
            nozero+=1
        if value=="1":
            noone+=1
    if (noone!=0 or nozero!=0):
        if (nozero>noone):
            return "morezeros"    
        if (noone>nozero):
            return "moreones"
        else:
            return "equal"

def readfile():
    f = open("03/input.txt","r")
    new_var = f.readlines()
    lines = list(filter(lambda l:len(l)>0,new_var))
    columns=len(lines[0])
    column=0
    oxygen_lines=lines
    co2_lines=lines
    oxy=None
    co2=None
    while column < columns:
        oxy_res=countOnesAndZeros(oxygen_lines,column)
        co2_res=countOnesAndZeros(co2_lines,column)
        if (oxy_res=="moreones" or oxy_res=="equal"):
            oxygen_lines=filter(lambda o: o[column]=="1",oxygen_lines)
        else:
            oxygen_lines=filter(lambda o: o[column]=="0",oxygen_lines)
        if (co2_res=="morezeros"):
            co2_lines=filter(lambda o: o[column]=="1",co2_lines)
        else:
            co2_lines=filter(lambda o: o[column]=="0",co2_lines)
        oxygen_lines=list(oxygen_lines)
        co2_lines=list(co2_lines)
        print("co2:"+str(co2_lines))
        print("oxy:"+str(oxygen_lines))
        
        if len(oxygen_lines)==1:
            print("oxy:"+oxygen_lines[0])
            oxy=oxygen_lines[0]
        if len(list(co2_lines))==1:
            print("co2:"+co2_lines[0])
            co2=co2_lines[0]    
        column+=1
    return [co2,oxy]

t=readfile()
co2 = int(t[1],base=2)
oxy = int(t[0],base=2)
print("oxy:"+str(oxy)+" co2:"+str(co2)+" tot:"+str(co2*oxy))