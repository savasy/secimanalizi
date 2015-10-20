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

 def loadfile(self,afile):
  text=[]
  with open(afile) as f:
   for line in f:
    line=self.lowerTR(line)
    line=self.npbuild(line.strip()) 
    text =text+ nltk.word_tokenize(line.strip())
  return text
 
 def lowerTR(self,line):
  line = line.replace("I","ı")
  line = line.replace("İ","i")
  return line.lower()

 def elim(self): 
  self.text= [w for w in self.text if w not in self.stop]
 
 def npbuild(self, aline):
  for np in self.nplist:
   npOrigin=np.replace("_"," ")
   if(npOrigin in aline):
    aline=aline.replace(npOrigin, np)
  return aline

  
  
 
