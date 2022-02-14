# askisi 3
from audioop import maxpp
from operator import truediv
from turtle import clear

print("Dwste onoma arxeiou")
name=input()
file = open(name) 
#file = open('matina.txt') 

finaltext = str(file.read())
finaltext = finaltext.replace('.','')
finaltext = finaltext.replace('\n','')
finaltext = finaltext.replace(',','')
finaltext = finaltext.replace('#','')
finaltext = finaltext.replace('0','')
finaltext = finaltext.replace('1','')
finaltext = finaltext.replace('2','')
finaltext = finaltext.replace('3','')   
finaltext = finaltext.replace('4','')
finaltext = finaltext.replace('5','')
finaltext = finaltext.replace('6','')
finaltext = finaltext.replace('7','')
finaltext = finaltext.replace('8','')
finaltext = finaltext.replace('9','')
finaltext = finaltext.replace(',','')
finaltext = finaltext.replace('*','')
finaltext = finaltext.replace('-','')
finaltext = finaltext.replace(';','')
finaltext = finaltext.replace(',','')   #aferw ola ta stoixeia ektos apo to keno 
finaltext = finaltext.replace(':','')
finaltext = finaltext.replace('+',' ')
finaltext = finaltext.replace('=','')
finaltext = finaltext.replace('"','')
finaltext = finaltext.replace('[','')
finaltext = finaltext.replace(']','')
finaltext = finaltext.replace('!',' ')
finaltext = finaltext.replace('(',' ')
finaltext = finaltext.replace(')',' ')
finaltext = finaltext.replace('_',' ')
finaltext = finaltext.replace("'",' ')
finaltext = finaltext.replace("@",' ')
finaltext = finaltext.replace("#",' ')

word=finaltext.split(" ")               #ta xwrizw me bash ta kena 

word = list(filter(('').__ne__, word))  #afairw ola ta kena 

"""""""""
gia na vgazei mono tis dipla dipla lexeis 
i=0
y=len(word)             
while i< (y-1):
    y1=len(word[i])
    y2=len(word[i+1])
    if (y1+y2)==20:
        x1=word[i]
        x2=word[i+1]
        word.remove(x1)
        word.remove(x2)
    else:
        i+=1
    y=len(word)
"""""""""

i=0
y=len(word)
while i < (y-1):                                    #otan vrei lexis pou to athisma tous na einai 20 tis afairei
    flag=False
    j=i+1
    while j<y:
        if len(word[i])+len(word[j])==20:  
                word.pop(j)
                word.pop(i)
                flag=True
                break
        else:
            j+=1
    if flag==False:
        i+=1
    y=len(word)

pl=[]
#arxikopoiw enan pinaka me polles theseis

y=len(word)
maxl=-1

for i in range (y):
    if maxl<len(word[i]):                 #blepw poia lexi exei ta perissotera grammata kai bazw thn timh ths se max 
        maxl=len(word[i])


for i in range (maxl):
    pl.append(0)                #dhmiourgw lista me mhdenika plthoi oses einai kai oi lexeis 

for i in range (y):
    for j in range (maxl):
        x=list(word[i])
        if len(x)==j+1:            #gia i apo mhden mexri max na bgazei ta statistika twn lexewn 
            pl[j]+=1

for i in range (maxl):
    if i==0:
        print("Words with " ,(i+1), " letter:")
        print(pl[i])
    else:
        print("Words with " ,(i+1), " letters:")
        print(pl[i])