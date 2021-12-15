def readfile():
    f = open("02/input.txt","r")
    lines = f.readlines()
    ypos = 0
    xpos=0
    aim=0
    for sline in lines:
        commandarr = sline.split(" ")
        command=commandarr[0]
        
        commandamount=int(commandarr[1])
        if command==("forward"):
            xpos+=commandamount
            ypos+=(commandamount*aim)
        if command==("up"):
            aim=aim-commandamount
        if command==("down"):
            aim=aim+commandamount
    return [xpos,ypos]

t=readfile()
print("x:"+str(t[0])+" y:"+str(t[1])+" tot:"+str(t[0]*t[1]))