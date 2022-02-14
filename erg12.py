#askisi 12
from re import X
from urllib.request import Request, urlopen

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()


#listdata=list(data)
data2=str(data)                         #metatrepw se string 
randomness=data2.split(',')
round1=randomness[0].replace("round","")
round1=round1.replace("b'{","")             #afairw osous xarakthres den xreiazomai apo to round
round1=round1.replace('"":',"")
round1=int(round1)
final=randomness[1].replace("randomness","")
final=final.replace(":","")
final=final.replace('"',"")                             #afairw osous xarakthres den xreiazomai apo to randomness
binum = ''.join(format(ord(i), 'b') for i in final)
b01=binum                                               #krataw tous arithmous 

for i in range (1,100):
    round1=round1-1
    req = Request('https://drand.cloudflare.com/public/'+str(round1), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    data2=str(data)
    randomness=data2.split(',')
    final=randomness[1].replace("randomness","")
    final=final.replace(":","")
    final=final.replace('"',"")
    binum = ''.join(format(ord(i), 'b') for i in final)     #metatrepw se binary
    b01+=binum
b01=list(b01)                   #vazw 3exwrista kathe stoixeio 01 se mia lista gia na mporw na ta metrhsw 

pl0=[0]
j=0
for i in range (len(b01)):
    if b01[i]!='1':                             #vriskw to plhthos 
        pl0[j]+=1
    else:
        pl0.append(0)
        j+=1
print("To mhkos ths megaluterhs akolouthias me sunexomena 0 einai: ",max(pl0))

pl1=[0]
j=0
for i in range (len(b01)):
    if b01[i]!='0':
        pl1[j]+=1
    else:
        pl1.append(0)
        j+=1
print("To mhkos ths megaluterhs akolouthias me sunexomena 1 einai: ",max(pl1))