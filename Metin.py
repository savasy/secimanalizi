import os, csv, nltk, sys, math

class Metin:
 'Verilen Herhangi bir metin, yazı, haber vesaire'
 def __init__(self, afile, stop=[], nplist=[]):
  'stop: stop word list'
  'nplist: kelime obekleri noun phrase olabilir, ["istanbul ili"  , "turkiye cumhuriyeti gibi"]'
  self.stop=stop
  self.nplist=nplist
  self.text=self.loadfile(afile)
  self.elim()
 
 ## line icinde - ve _ hariç tüm karakterleri siler
 def cleanPunc(self,aline):
  return ''.join(ch for ch in aline if ch.isalnum() or ch =='-' or ch=='_')
 
 # input: afile.txt
 # çıktı: a list of words, nplist ile
 # NP ler etiketleniyor

 def loadfile(self,afile):
  text=[]
  with open(afile) as f:
   topla="" 
   for line in f:
    line=self.lowerTR(line.strip())
    topla= topla+" "+line
  
  topla=nltk.word_tokenize(self.npbuild(topla))
  text= [self.cleanPunc(w) for w in topla]
  return text
 
 # türkçe için lower 
 # çünkü büyük İ ve I sorun çıkartıyor
 def lowerTR(self,line):
  line = line.replace("I","ı")
  line = line.replace("İ","i")
  return line.lower()

# eğer stop word verilmişse eliminasyon yapıyor
 def elim(self): 
  self.text= [w for w in self.text if w not in self.stop]
 
 # verilen npliste göre gelen bir aline'daki np leri n_n şeklinde 
 # etiketliyor
 # örnek : "bir genel müdür geldi" ->
 # "bir genel_müdür geldi"

 def npbuild(self, aline):
  for np in self.nplist:
   npOrigin=np.replace("_"," ")
   if(npOrigin in aline):
    aline=aline.replace(npOrigin, np)
  return aline

  
  
 
