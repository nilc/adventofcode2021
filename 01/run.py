def readfile():
    f = open("01/input.txt","r")
    lines = f.readlines()
    previous = -1
    count=0
    for sline in lines:
        if sline.__len__()>0:
            line=int(sline)
            if (line>previous & previous!=-1):
                print(line)
                count=count+1
            previous=line
    return count
count=readfile()
print("count:"+str(count))