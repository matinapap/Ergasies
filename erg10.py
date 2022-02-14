#askisi 10
import math
from os import removedirs
from random import randrange
from re import X
from sys import flags
from tkinter import Y


file = open('matina.txt') 
text = str(file.read())


char=list(text)

char=list(filter((' ').__ne__, char))

h=len(char)

res = ''.join(format(ord(i), '07b') for i in char) #metatrepoume kathe xarakthra se binary mhkous 7 bit

listres=list(res)



y=len(res)//7   #posa 0 kai 1 twn 7bits uparxoun

bit7=[]
for i in range (y-1):
    ta=listres[0]+listres[1]+listres[2]+listres[3]+listres[4]+listres[5]+listres[6]
    listres.pop(0)
    listres.pop(1)
    listres.pop(2)
    listres.pop(3)
    listres.pop(4)
    listres.pop(5)
    listres.pop(6)
    bit7.append(ta)

missed = ''.join(format(ord(i), '07b') for i in char[h-1])
ta=missed[0]+missed[1]+missed[2]+missed[3]+missed[4]+missed[5]+missed[6]
bit7.append(ta)                                                         #dhmiourgw tis 7 bit akolouthies

for i in range (y):
    m=list(bit7[i])
    m.pop(2)
    m.pop(2)
    m.pop(2)                   #afhnw mono ta 2 mrpostina kai ta duo teleutaia stoixeia 
    bit7[i]=m

bit16=[]

if len(bit7)%4==0:
    for i in range (0,len(bit7),4):
        b=bit7[i]+bit7[i+1]+bit7[i+2]+bit7[i+3]     #dhmiourgw toys 16bit arithmous
        bit16.append(b)
elif (len(bit7)%4)==3:                              #pairnw periptwseis 
    for i in range (0,len(bit7)-3,4):
        b=bit7[i]+bit7[i+1]+bit7[i+2]+bit7[i+3]     #dhmiourgw toys 16bit arithmous
        bit16.append(b)
    b2=["0"*4]
    b=b2+bit7[(len(bit7)-3)]+bit7[(len(bit7)-2)]+bit7[(len(bit7)-1)]  
    bit16.append(b)
elif len(bit7)%4==2:
    for i in range (0,len(bit7)-2,4):
        b=bit7[i]+bit7[i+1]+bit7[i+2]+bit7[i+3]     #dhmiourgw toys 16bit arithmous
        bit16.append(b)
    b2=["0"*8]
    b=b2+bit7[(len(bit7)-2)]+bit7[(len(bit7)-1)]   
    bit16.append(b)
elif len(bit7)%4==1:
    for i in range (0,len(bit7)-1,4):
        b=bit7[i]+bit7[i+1]+bit7[i+2]+bit7[i+3]     #dhmiourgw toys 16bit arithmous
        bit16.append(b)
    b2=["0"*12]
    b=b2+bit7[(len(bit7)-1)]   
    bit16.append(b)

pl1=0
pl=len(bit16)
for i in range (pl):
    if bit16[i][-1]=='0':
        pl1+=1         

print("To pososto twn zugwn arithmwn einai: ")          #vriskw to plithos twn zugwn arithmwn 
print(pl1/pl*100,"%")

for i in range (pl):
    d=''.join(bit16[i])
    bit16[i]=d
    
for i in range (pl):   
    bit16[i]=int(bit16[i],2)                        #metatroph binary se decimal

pl2=0
for i in range (pl):   
    if bit16[i]%3==0:
        pl2+=1
print("To pososto twn arithmwn pou dierountai me to 3 einai: ")          #posoi ari8moi dierountai me to 3
print(pl2/pl*100,"%")

pl3=0
for i in range (pl):   
    if bit16[i]%5==0:
        pl3+=1
print("To pososto twn arithmwn pou dierountai me to 5 einai: ")          #posoi ari8moi dierountai me to 5
print(pl3/pl*100,"%")

pl4=0
for i in range (pl):   
    if bit16[i]%7==0:
        pl4+=1
print("To pososto twn arithmwn pou dierountai me to 7 einai: ")          #posoi ari8moi dierountai me to 7
print(pl4/pl*100,"%")