class Metin:
 'Verilen Herhangi bir metin, yazı, haber vesaire'
 def __init__(self, text, stop, nplist):
  'stop: stop word list'
  'nplist: kelime obekleri noun phrase olabilir, istanbul ili   turkiye cumhuriyeti gibi '
  self.text=text
  self.stop=stop
  self.nplist=nplist
  self.di()
 def display(self):
  print("hello")

 def eliminate(self):
  'eliminate stop words'
  print("hmm")

 def repNp(self):
  'make all phrases in nplist adjacent e.g. new_york ' 
  print("hmm")
 def fd(self):
  ' return frequency dist of term'
 def terms(self):
  'return only terms'






 
