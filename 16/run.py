from os import read
import re
from typing import Literal

hextobin={
"0":"0000",
"1":"0001",
"2":"0010",
"3":"0011",
"4":"0100",
"5":"0101",
"6":"0110",
"7":"0111",
"8":"1000",
"9":"1001",
"A":"1010",
"B":"1011",
"C":"1100",
"D":"1101",
"E":"1110",
"F":"1111",
}

def readfile():
    f = open("16/input.txt","r")
    lines = f.readlines()
    bincode_string = toBinary(lines)
    print(bincode_string)
    packet = Packet()
    parsePacket(bincode_string,packet)
    print(versionadd)
    return packet.packets[0]

def toBinary(lines):
    binarycode=[]
    for c in list(lines[0].strip()):
        binarycode.append(hextobin[c])
    bincode_string = "".join(binarycode)
    return bincode_string
    #nonRecursive(bincode_string, standardheaderv)

class Packet:

    def __init__(self) -> None:
        self.packets=[]
        self.version=None
        self.type=None
        self.length=0
        self.literal=None
        self.wantedsubpackets=None
        self.wantedcodelength=None
        self.parent=None

    def isFull(self):
        packet=self
        if (packet.wantedsubpackets!=None and len(packet.packets)<packet.wantedsubpackets):
            print("Wanted number of subpackets:{} is {} packet:{}".format(packet.wantedsubpackets,len(packet.packets),packet))
            return False
        subpacketcodelength = packet.codelength()-packet.length
        if (packet.wantedcodelength!=None and subpacketcodelength<packet.wantedcodelength):
            print("Wanted subpacketcodelength:{} is {} packet:{}".format(packet.wantedcodelength,subpacketcodelength,packet))
            return False
        return True

    def addPacket(self,packet):
        self.packets.append(packet)
        if self.type!=None and self.type in [5,6,7] and len(self.packets)>2:
            print("Too many in packet something wrong with parsing..")


    def doOperator(self):
        if (self.type==4):
            return self.literal
        if (self.type==0):
            return sum(map(lambda p:p.doOperator(),self.packets))
        if (self.type==1):
            multiple=self.packets[0].doOperator()
            for p in self.packets[1:]:
                multiple=multiple*p.doOperator()
            return multiple
        if self.type==2:
            return min(map(lambda p:p.doOperator(),self.packets))
        if self.type==3:
            return max(map(lambda p:p.doOperator(),self.packets))
        if self.type==5:
            p1, p2 = self.getTheTwoSubpackets()
            gt = p1>p2
            if gt: return 1
            return 0
        if self.type==6:
            p1, p2 = self.getTheTwoSubpackets()
            lt = p1<p2
            if lt: return 1
            return 0
        if self.type==7:
            p1, p2 = self.getTheTwoSubpackets()
            eq = p1==p2
            if eq: return 1
            return 0
        else:
            print("Wrong operator:{} packet:{}".format(self.type,packet))

    def getTheTwoSubpackets(self):
        p1=self.packets[0].doOperator()
        p2=self.packets[1].doOperator()
        if (len(self.packets)!=2):
            print("Wrong number of packets!")
        return p1,p2

    def __str__(self) -> str:
        if self.literal!=None:
            return "type:{} version:{} literal:{} packets:{}".format(self.type,self.version,self.literal,"["+"\n\t".join(map(lambda t:str(t),self.packets))+"]")
        else:
            return "type:{} version:{} packets:{}".format(self.type,self.version,"["+"\n\t".join(map(lambda t:str(t),self.packets))+"]")

    def codelength(self) -> int:
            return self.length+sum(map(lambda l:l.codelength(),self.packets))
 

def decodeToInt(bits):
    return int(bits,base=2)
versionadd=0

heap=[]

def parsePacket(packetcode,parentpacket):
    global versionadd
    global heap
    reader=0
    while parentpacket.isFull() and parentpacket.parent!=None:
        print("Switched parent to its parent")
        parentpacket=parentpacket.parent
    print("Len:{} code:{} parent:{}".format(len(packetcode),packetcode,parentpacket))
    if re.search("1",packetcode)==None:
        print("Found end!!")
        return (reader,parentpacket)
    
    packet=Packet()
    packet.version=decodeToInt(packetcode[reader:reader+3])
    packet.type=decodeToInt(packetcode[reader+3:reader+6])
    packet.parent=parentpacket
    parentpacket.addPacket(packet)
    reader+=6
    print("version:{} type:{}".format(packet.version,packet.type))
    versionadd+=packet.version
    if (packet.type==4):
        (readeradd,literal)=getLiteral(packetcode[reader:])
        #print("literal:{} newreaderpos:{}".format(literal,readeradd))
        reader+=readeradd
        packet.literal=literal
        packet.length=reader
        return parsePacket(packetcode[reader:],parentpacket)
    else:
        # operator
        typeid=packetcode[reader:reader+1]
        reader+=1
        if typeid=="0":
            subpacketlength=decodeToInt(packetcode[reader:reader+15])
            reader=reader+15
            packet.wantedcodelength=subpacketlength
        else:
            subpacketlength=decodeToInt(packetcode[reader:reader+11])
            reader+=11
            packet.wantedsubpackets=subpacketlength

        packet.length=reader    
        return parsePacket(packetcode[reader:],packet)

def getLiteral(subpacket):
    groups=[]
    foundend=False
    readerpos=0
    while foundend==False:
        readerendpos = readerpos+5
        group=subpacket[readerpos:readerendpos]
        groups.append(group[1:5])
        startbit = group[0:1]
        if startbit=="0":
            foundend=True
        readerpos=readerendpos
    literal=decodeToInt("".join(groups))
    return (readerpos,literal)


#parsePacket("00111000000000000110111101000101001010010001001000000000",Packet())
packet = Packet()
heap.append(packet)
#parsePacket(toBinary(["38006F45291200"]),packet)
#print(packet)
#t=parsePacket(toBinary(["8A004A801A8002F478"]),packet)
#t=parsePacket(toBinary(["620080001611562C8802118E34"]),Packet())
#t=parsePacket(toBinary(["A0016C880162017C3686B18A3D4780"]),Packet())
#t=parsePacket(toBinary(["C0015000016115A2E0802F182340"]),Packet())
#print(str(t[1]))
#print(versionadd)
#import json
#jsonStr = json.dumps(t[1].__dict__)
#print(jsonStr)
t=readfile()
print(t)
print(t.doOperator())

lines='''C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
04005AC33890 finds the product of 6 and 9, resulting in the value 54.
880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
D8005AC2A8F0 produces 1, because 5 is less than 15.
F600BC2D8F produces 0, because 5 is not greater than 15.
9C005AC2F8F0 produces 0, because 5 is not equal to 15.
9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.'''
for line in lines.split("\n")[0:8]:
    s=line.split(" ")
    hex=s[0]
    print(hex)
    parent=Packet()
    t=parsePacket(toBinary([hex]),parent)
    
    parent = parent.packets[0]
   # print(parent)
    print("{}={}".format(hex,(parent.doOperator())))