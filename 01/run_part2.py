def readfile():
    f = open("01/input.txt","r")
    lines = list(map(lambda s:int(s),filter(lambda l:len(l)>0,f.readlines())))
    
    previous = -1
    count=0
    line=0
    threesums=[]
    lastsum=None
    while(line<len(lines)-2):
        sum1=lines[line]+lines[line+1]+lines[line+2]
        
        if (lastsum==None):
            lastsum=sum1
        else:
            if sum1>lastsum:
                print(str(sum1)+" ls:"+str(lastsum))
                count+=1
            lastsum=sum1    
        line+=1
    return count
count=readfile()
print("count:"+str(count))