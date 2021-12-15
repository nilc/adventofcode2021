def readfile():
    f = open("03/input.txt","r")
    lines = f.readlines()
    columns=len(lines[0])
    column=0
    gamma=""
    epsilon=""
    while column < columns:
        nozero=0
        noone=1
        for sline in lines:
            value=sline[column]
            if value=="0":
                nozero+=1
            if value=="1":
                noone+=1
        if (noone!=0 | nozero!=0):
            if (nozero>noone):
                gamma=gamma+"1"
                epsilon+="0"       
            else:
                gamma=gamma+"0"
                epsilon+="1"
        print("eps:"+epsilon+" gamma:"+gamma)       
        column+=1
    return [epsilon,gamma]

t=readfile()
gamma = int(t[1],base=2)
eps = int(t[0],base=2)
print("eps:"+str(eps)+" gamma:"+str(gamma)+" tot:"+str(gamma*eps))