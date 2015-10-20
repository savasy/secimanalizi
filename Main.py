from Metin import Metin
import os, csv, nltk, sys, math

# noun phrase ler için
def buildNP(afile):
 nplist=[]
 with open(afile) as f:
  for line in f:
   if(len(line))>1:
    w=line.strip().lower()
    w=w.replace(" ","_")
    nplist.append(w)
 return simplify(nplist)

def simplify(liste):
 liste2=[ inNpListe(x, liste) for x in liste]
 return list(set(liste2))

# an of word in liste starts with word w 
def inNpListe(w, liste):
 for i in liste:
  if w.startswith(i):
   return i
 return ""

# we select and deal with only those words in np.txt
nplist=buildNP("data/np.txt")
stoplist=[]

akp1=Metin("data/akp7haz.txt",stoplist, nplist)
akp2=Metin("data/akp1kasim.txt",stoplist, nplist)
chp1=Metin("data/chp7haz.txt",stoplist, nplist)
chp2=Metin("data/chp1kasim.txt",stoplist, nplist)
mhp1=Metin("data/mhp7haz.txt",stoplist, nplist)
mhp2=Metin("data/mhp1kasim.txt",stoplist, nplist)
hdp1=Metin("data/hdp7haz.txt",stoplist, nplist)
hdp2=Metin("data/hdp1kasim.txt",stoplist, nplist)



a1=[ inNpListe(w, nplist) for w in akp1.text if inNpListe(w, nplist)!=""]
a2=[ inNpListe(w, nplist) for w in akp2.text if inNpListe(w, nplist)!=""]

c1=[ inNpListe(w, nplist) for w in chp1.text if inNpListe(w, nplist)!=""]
c2=[ inNpListe(w, nplist) for w in chp2.text if inNpListe(w, nplist)!=""]

m1=[ inNpListe(w, nplist) for w in mhp1.text if inNpListe(w, nplist)!=""]
m2=[ inNpListe(w, nplist) for w in mhp2.text if inNpListe(w, nplist)!=""]

h1=[ inNpListe(w, nplist) for w in hdp1.text if inNpListe(w, nplist)!=""]
h2=[ inNpListe(w, nplist) for w in hdp2.text if inNpListe(w, nplist)!=""]


alle=a1+a2+c1+c2+m1+m2+h1+h2
fall=nltk.FreqDist(alle)

terms= list(set(a1+a2+c1+c2+m1+m2+h1+h2))

fa1= nltk.FreqDist(a1)
fa2= nltk.FreqDist(a2)
fc1= nltk.FreqDist(c1)
fc2= nltk.FreqDist(c2)
fm1= nltk.FreqDist(m1)
fm2= nltk.FreqDist(m2)
fh1= nltk.FreqDist(h1)
fh2= nltk.FreqDist(h2)

c=0
for t in terms:
 if(fall[t]>5):
  c=c+1
  print(t,fa1[t],fa2[t],fc1[t],fc2[t],fm1[t],fm2[t],fh1[t],fh2[t])

print(c)



















