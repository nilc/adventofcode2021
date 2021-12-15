from typing import Iterable


def readfile():
    f = open("04/input.txt","r")
    lines = f.readlines()
    inputs=map(lambda d:int(d),lines[0].split(","))
    lines.remove(lines[0])
    lines=filter(lambda l:len(l)>1,lines)
    boards=[]
    boardlines=[]
    for line in filter(lambda d:len(d)>1,lines):
        linessplit = line.split(" ")
        boardline=filter(lambda d:d.strip()!="",linessplit)
        boardline=list(map(lambda d:int(d),boardline))

    
        boardlines.append(boardline)    
        if len(boardlines)==5:
            boards.append(Board(boardlines))
            boardlines=[]    
    [bingoboard,usedinputs,lastinput] = getBestBingoBoard(inputs, boards)
    print(str(bingoboard.sumUnmarked(usedinputs)*lastinput))

def getBestBingoBoard(inputs, boards):
    usedinputs=[]
    for input in inputs:
        usedinputs.append(input)
        for board in boards:
            boardisbingo = board.bingo(usedinputs)
            if boardisbingo:
                print("Found bingoboard"+str(board.boardlines)+" input:"+str(usedinputs))
                return [board,usedinputs,input]
    return None            

class Board:
    def __init__(self,boardlines:Iterable) -> None:
        self.boardlines=list(boardlines)
        columns=len(self.boardlines[0])
        self.columnlines=[]
        for x in range(columns):
            columnline=[]
            for line in self.boardlines:
                columnline.append(line[x])
            self.columnlines.append(columnline)
        

    def bingo(self,inputs) -> bool:
        for line in self.boardlines:
            if (all(item in inputs for item in line)):
                return True
        for line in self.columnlines:
            if (all(item in inputs for item in line)):
                return True 
        return False
    
    def sumUnmarked(self,inputs) -> int:
        unmarked=[]
        for line in self.boardlines:
            copyarray=line
            for i in inputs:
                while i in copyarray:
                    copyarray.remove(i)
            unmarked.extend(copyarray)
        sum=0
        for u in unmarked:
            sum+=u
        print("sum is:{}".format(sum)+" unmarked is;"+str(unmarked))
        return sum
        

                

t=readfile()
print(t)
