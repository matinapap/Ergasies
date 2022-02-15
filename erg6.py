#askisi 6
from operator import truediv
import random

def print_board(pg,ps,axg,axs,vag,vas):
    skakiera=[["  ","  ","  ","  ","  ","  ","  ","  "],
              ["  ","  ","  ","  ","  ","  ","  ","  "],
              ["  ","  ","  ","  ","  ","  ","  ","  "],
              ["  ","  ","  ","  ","  ","  ","  ","  "],
              ["  ","  ","  ","  ","  ","  ","  ","  "],
              ["  ","  ","  ","  ","  ","  ","  ","  "],
              ["  ","  ","  ","  ","  ","  ","  ","  "],
              ["  ","  ","  ","  ","  ","  ","  ","  "]]
    skakiera[int(pg-1)][int(ps-1)]="lp"                    #leukos purgos
    skakiera[int(axg-1)][int(axs-1)]="la"                   #leukos axiomatikos
    skakiera[int(vag-1)][int(vas-1)]="mv"                   #mavrh vasilissa
    return skakiera

def grammes():
    grammes=[1,2,3,4,5,6,7,8]
    g=random.choice(grammes)
    return g

def sthles():
    sthles=[1,2,3,4,5,6,7,8]
    st=random.choice(sthles)
    return st

def pyrgos(pg,ps,vag,vas):
    if (vag==pg)|(vas==ps):
        kerdise=True
    else:
        kerdise=False
    return kerdise

def axiomatikos(axg,axs,vag,vas):
    kerdise=False
    if ((axs+axg)%2==1)&((vas+vag)%2==1):       #mavra tetragwna
        if ((axs-axg==1)&(vas-vag==1))or((axg-axs==1)&(vag-vas==1))or((axg-axs==3)&(vag-vas==3))or((axs-axg==3)&(vas-vag==3))or((axg-axs==5)&(vag-vas==5))or((axg-axs==5)&(vag-vas==5))or((axs+axg==11)&(vas+vag==11))or((axs+axg==3)&(vas+vag==3))or((axs+axg==5)&(vas+vag==5))or((axs+axg==7)&(vas+vag==7))or((axs+axg==9)&(vas+vag==9))or((axs+axg==13)&(vas+vag==13))or((axs+axg==15)&(vas+vag==15)):
            kerdise=True
    else:                                       #lefka tetragwna
        if ((axs-axg==0)&(vas-vag==0))or((axg-axs==2)&(vag-vas==2))or((axg-axs==4)&(vag-vas==4))or((axg-axs==6)&(vag-vas==6))or((axs-axg==2)&(vas-vag==2))or((axs-axg==4)&(vas-vag==4))or((axs-axg==6)&(vas-vag==6))or((axs+axg==4)&(vas+vag==4))or((axs+axg==6)&(vas+vag==6))or((axs+axg==8)&(vas+vag==8))or((axs+axg==10)&(vas+vag==10))or((axs+axg==12)&(vas+vag==12))or((axs+axg==14)&(vas+vag==14)):
            kerdise=True
    return kerdise

p1=0
p2=0
paizei=True
#prwtos paikths false 
#deuteros paikths true 
for i in range (100):
    if (i+1)%2==0:
        paizei=True
    else:
        paizei=False
    pg=grammes()
    ps=sthles()
    axg=grammes()                           
    axs=sthles()
    while (pg==axg)&(ps==axs):
        axg=grammes()
        axs=sthles()                        #vriskw thn grammh kai thn sthlh pou einai kathe pioni kai kanw elegxw wste na einai diaforetikh h thesh kathe pioniou 
    vag=grammes()
    vas=sthles()
    while ((pg==vag)&(ps==vas))or((axg==vag)&(axs==vas)):
        vag=grammes()
        vas=sthles()
    skakiera=print_board(pg,ps,axg,axs,vag,vas)
    for i in range (8):                         
        print(skakiera[i])                          #ektupwnei kathe fora thn skakiera 
    print(" ")
    if paizei==False:
        kerdise=pyrgos(pg,ps,vag,vas)           #gia ton pirgo 
        if kerdise==True:
            p1+=1
        kerdise=axiomatikos(axg,axs,vag,vas)  #gia ton axiomatiko
        if kerdise==True:
            p1+=1
    else:
        kerdise=pyrgos(pg,ps,vag,vas)           #gia thn vassilisa
        if kerdise==False:
            kerdise=axiomatikos(pg,ps,vag,vas)
        if kerdise==True:
            p2+=1
        kerdise=pyrgos(axg,axs,vag,vas)
        if kerdise==False:
            kerdise=axiomatikos(axg,axs,vag,vas)  
        if kerdise==True:
            p2+=1

print("Vathmos leukou pekth: ",p1)
print("Vathmos mavrou pekth: ",p2)