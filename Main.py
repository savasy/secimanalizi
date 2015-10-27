from Metin import Metin
import os, csv, nltk, sys, math

# noun phrase ler için
def buildNP(afile):
 nplist=[]
 with open(afile) as f:
  for line in f:
   if(len(line))>1:
    w=lowerTR(line.strip())
    w=w.replace(" ","_")
    nplist.append(w)
 return list(set(nplist))

# Türkçe için lower fonksiyonu
def lowerTR(line):
  line = line.replace("I","ı")
  line = line.replace("İ","i")
  return line.lower()

# listedeki birbirine kapsayan kelimeler
# temizleniyor
# örnek araba arabalar -> araba
# output: son listede hiçbir kelime diğer hiçbir kelime ile başlamaz
def simplify(liste):
 liste2=[ inNpListe(x, liste) for x in liste]
 return list(set(liste2))

# listede w ile başlayan ilk kelime döner 
def inNpListe(w, liste):
 for i in liste:
  if w.startswith(i):
   return i
 return ""


# synonym setleri dosyada syn, syn2, syn3 şeklinde tutulur
# bu dicitonary ile kök sinonime ulaşılmaya çalışılır
def loadSyn(afile):
 dicti={}
 with open(afile) as f:
  for line in f:
   liste= line.strip().split(",")
   value= liste[0].strip()
   for item in liste:
    dicti[item.strip()]=value
 return dicti


# dosya formatı, META kavram geliştrimek için
# politika, yasa, koalisyon, 
# spor, futbol, aziz yıldırım, 
#çıktı dictinary -> dicti[spor]=[futbol, ...]

def loadKavram(afile):
 dicti={} 
 with open(afile) as f:
  for line in f:
   liste= line.strip().split(",")
   value= liste[0].strip() # ülke
   dicti[value]=[w.strip() for w in liste if len(w.strip()) >1]
 return dicti

# listeyi kelimelerin boyuna göre sıralar
def sorting(alist):
 nlist=[(w, len(w)) for w in alist]
 nlist2=sorted(nlist, key= lambda x: x[1])
 nlist3 =[w for (w,s) in nlist2]
 return nlist3

# we select and deal with only those words in np.txt
nplist=sorting(buildNP("data/np2.txt"))

# bunlar META kavram analizi için# 
# Örnek futbol, maç gibi kavramların üst sınıf hypernym'i SPOR dur
# bu  lsiteyi dışardan veriyoruz

kavram= loadKavram("data/kavram2.txt")

# stop list kullanmayacaksak bunu boş geçiyoruz
stoplist=[]

akp1=Metin("data/akp7haz.txt",stoplist, nplist)
akp2=Metin("data/akp1kasim.txt",stoplist, nplist)
chp1=Metin("data/chp7haz.txt",stoplist, nplist)
chp2=Metin("data/chp1kasim.txt",stoplist, nplist)
mhp1=Metin("data/mhp7haz.txt",stoplist, nplist)
mhp2=Metin("data/mhp1kasim.txt",stoplist, nplist)
hdp1=Metin("data/hdp7haz.txt",stoplist, nplist)
hdp2=Metin("data/hdp1kasim.txt",stoplist, nplist)



# yukarıdan gelen akp1 gibi Metin objelerindeki textler alınıp ön işlemlerden geçirilyor
# sonunda sadece NP lerle dolu gereksiz tekrarlar atılmış bir liste kalıyor 
a1=[ inNpListe(w, nplist) for w in akp1.text if inNpListe(w, nplist)!=""]
a2=[ inNpListe(w, nplist) for w in akp2.text if inNpListe(w, nplist)!=""]

c1=[ inNpListe(w, nplist) for w in chp1.text if inNpListe(w, nplist)!=""]
c2=[ inNpListe(w, nplist) for w in chp2.text if inNpListe(w, nplist)!=""]

m1=[ inNpListe(w, nplist) for w in mhp1.text if inNpListe(w, nplist)!=""]
m2=[ inNpListe(w, nplist) for w in mhp2.text if inNpListe(w, nplist)!=""]

h1=[ inNpListe(w, nplist) for w in hdp1.text if inNpListe(w, nplist)!=""]
h2=[ inNpListe(w, nplist) for w in hdp2.text if inNpListe(w, nplist)!=""]


# Tüm kelimeler GLOBAL ölçüm için
alle=a1+a2+c1+c2+m1+m2+h1+h2
fall=nltk.FreqDist(alle)

# uniq terimler için
terms= list(set(a1+a2+c1+c2+m1+m2+h1+h2))


fa1= nltk.FreqDist(a1)
fa2= nltk.FreqDist(a2)
fc1= nltk.FreqDist(c1)
fc2= nltk.FreqDist(c2)
fm1= nltk.FreqDist(m1)
fm2= nltk.FreqDist(m2)
fh1= nltk.FreqDist(h1)
fh2= nltk.FreqDist(h2)



# print ALL words
# Tüm Kelimeler ve hangi corpusta(parti) olduğunu çıktılayan bir matris dosysası
# Dikkat burada OUT isimli bir folder olmalı
c=0
out = open("out/allwords.txt", "w")
out.write(",AKP1,AKP2,CHP1,CHP2,MHP1,MHP2,HDP1,HDP2\n")
for t in terms:
 if(fall[t]>3):
  c=c+1
  str1=t+","+str(fa1[t])+","+str(fa2[t])+","+str(fc1[t])+","+str(fc2[t])+","+str(fm1[t])+","+str(fm2[t])+","+str(fh1[t])+","+str(fh2[t])
  out.write(str1+"\n")

out.close()
print(c)



# print each kavram
# her bir KAVRAM - Hypernym için
# ayrı bir seçim yapllıyor
# mesela sadece spor ile ilgili kavrmalar
# ve Parrtiler önce KAVRAM_spor_txt dosyasına yazılıyor
# sonra bu her bir diğer kavramlar için tekrarlanıyor

for k in kavram.keys():
 out = open("out/KAVRAM_"+k+".txt", "w")
 out.write(",AKP1,AKP2,CHP1,CHP2,MHP1,MHP2,HDP1,HDP2\n")
 for t in terms:
  if(fall[t]>3 and t in kavram[k]):
   str1=t+","+str(fa1[t])+","+str(fa2[t])+","+str(fc1[t])+","+str(fc2[t])+","+str(fm1[t])+","+str(fm2[t])+","+str(fh1[t])+","+str(fh2[t])   
   out.write(str1+"\n")

 out.close()



## Kavramların toplamı
# Bu sefer kelimelerin yerine Kavramlarıda dahil ederek çıktılıyoruz
# daha sonra bu AGGREGATION.R dosaysı tarafından kullanılyor
out = open("out/KAVRAM_AGG.txt", "w")
out.write(",AKP1,AKP2,CHP1,CHP2,MHP1,MHP2,HDP1,HDP2\n")

for k in kavram.keys():
 for t in terms:
  if(fall[t]>3 and t in kavram[k]):
   str1=k+","+str(fa1[t])+","+str(fa2[t])+","+str(fc1[t])+","+str(fc2[t])+","+str(fm1[t])+","+str(fm2[t])+","+str(fh1[t])+","+str(fh2[t])
   out.write(str1+"\n")

out.close()
