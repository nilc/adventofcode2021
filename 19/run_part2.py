import re
import json

# This is using the logging output from part1..
def readOut():

    f = open("19/alladdv.txt","r")
    lines = f.readlines()
    biggestManhattan=0
    vectors=[]
    for line in lines:
        pattern=re.compile(".*addv:(.*).* switchflip:(.*)")
        m=pattern.match(line)
        
        new_var = m.group(1)
        addv=json.loads(new_var)
        vectors.append(addv)
        #switchflip=m.group[1]
    for v2 in range(len(vectors)):
        for v1 in range(len(vectors)):
            if (v1!=v2):
                manhattan=sum(map(lambda i:vectors[v1][i]-vectors[v2][i],range(3)))
                if (manhattan>biggestManhattan):
                    biggestManhattan=manhattan
    print(biggestManhattan)

readOut()