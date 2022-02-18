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
finaltext = finaltext.replace(',','')   #αφαιρώ όλα τα στοιχεία εκτός από το κενό 
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

word=finaltext.split(" ")               #τα χωρίζω με βάση τα κενά 

word = list(filter(('').__ne__, word))  #αφαιρώ όλα τα κενά 

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
while i < (y-1):                                    #όταν βρει λέξεις που το αθροισμά τους να είναι 20 τις αφαιρεί
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
    if maxl<len(word[i]):                 #βλέπω ποια λέξη έχει τα περισσότερα γράμματα και βάζω την τιμή της σε max 
        maxl=len(word[i])


for i in range (maxl):
    pl.append(0)                #δημιουργώ λίστα με μηδενικά πλήθη όσες είναι και οι λέξεις 

for i in range (y):
    for j in range (maxl):
        x=list(word[i])
        if len(x)==j+1:            #για i από 0 μέχρι max να βγάζει τα στατιστικά των λέξεων 
            pl[j]+=1

for i in range (maxl):
    if i==0:
        print("Words with " ,(i+1), " letter:")
        print(pl[i])
    else:
        print("Words with " ,(i+1), " letters:")
        print(pl[i])
