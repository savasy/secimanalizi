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
    line=self.npbuild(line.strip().lower()) 
    text =text+ line.strip().split() 
  return text 
 def elim(self): 
  self.text= [w for w in self.text if w not in self.stop]
 def npbuild(self, aline):
  for np in self.nplist:
   if(np in aline):
    print(np,aline) 
    newnp=np.replace(" ","_") 
    aline=aline.replace(np, newnp)
  return aline

  
  
 
