import gensim, os, csv, nltk, sys, math
from gensim import corpora, models, similarities
from nltk.corpus import stopwords
from nltk.collocations import *

trigram_measures = nltk.collocations.TrigramAssocMeasures()
bigram_measures = nltk.collocations.BigramAssocMeasures()



fdGlobal=computeFD(open("global"))


# bir listeyi bir dosyaya kaydeder

def save(liste, filename):
 with open(filename, 'w') as f:
  f.write(str(liste))

# dosyaya kaydolmuş listeyi geri alır

def load(filename):
 with open(filename) as f:
  liste= eval(f.readlines()[0])
 return liste 


# boşlukla ayrılmış kelime çiftlerini kelimeleri "_" ile birleştirir

def rep_coll(text):
 for c in colls:
  w1,w2=c.strip().split()
  text=text.replace(c, w1+"_"+w2)
 return text


	# to convert new york as new_york if NP (new york) exist both in keys(vector) and text
	def mergeNP(text, keys):
	 for k in keys:
	  if ' ' in k and k in text:
	   print(k)
	   w1= k.split()[0]
	   w2= k.split()[1]
	   text=text.replace(k, w1+"_"+w2)
	 return text  
	   


	# Inputs:
	# Fred Dist of words, Freq Dist of Year , Freq Dist of cooccur,
	# particular word and year
	# dice= cooccur(w,y)/(fq(w)+ fq(y))
	def dice(fdW, fdY,fdT,w,y):
	 if (fdT[(w,y)]==0): return 0
	 return math.log(fdT[(w,y)]*fdW.N()/(fdW[w]+ fdY[y]))

	def ig(fdW, fdY,fdT,w,y):
	 n=fdW.N()
	 n11= fdT[(w,y)]
	 n1_=fdW[w]
	 n_1=fdYear[y]
	 n10= n1_ -n11
	 n01= n_1 - n11
	 n0_= n-n1_
	 n_0= n- n_1
	 n00= n- n1_ - n_1 +n11	
	 ig=  n11* log(n*n11 *1.0/ (n1_* n_1)) /n 
	 ig+= n01* log(n*n01 *1.0/ (n0_*n_1) ) /n
	 ig+= n10* log(n*n10 *1.0/ (n1_*n_0) ) /n
	 ig+= n00* log(n*n00 *1.0/ (n0_*n_0) ) /n
	 return ig

	def log(n):
	 if n==0: return 0
	 return math.log(n)

	# take first N important words
	def take(fdWord, fdYear, fdTuple, year, N):
	 wlist=set([w for w,y in tuples if y==year and fdWord[w]>10])
	 scores=[(w, ig(fdWord, fdYear, fdTuple,w,year)) for w in wlist]
	 sorted_scores=sorted(scores, key=lambda scores:scores[1],reverse=True)
	 return sorted_scores[:N]

# her yıla yakın ilk N kelimeyi alıyor
# bir vektör yaratıyor
def wordvec(fdWord, fdYear, fdTuple, N):
 vec=[]
 for y in fdYear.keys():
  taken=take(fdWord, fdYear, fdTuple, y, N) 
  taken=[w for w,s in taken]
  vec+=taken
 return vec

# retrieve the words in wordvec , and tabulate accross year 
def tabulate(tuples, wordvec):
 t2= [(w,y) for (w,y) in tuples if w in wordvec]
 cfd=nltk.ConditionalFreqDist(t2)
 return cfd.tabulate()

# select terms for a given year
def select(tuples, year, fdWord):
 return [w for (w,y) in tuples if y==year and fdWord[w]>3]


def computeFD(file):
 all=[]
 for line in file.readlines():
  line=repSyn(line)
  line = nltk.word_tokenize(line.lower())
  tokens=[wnl.lemmatize(w.strip()) for w in line]
  all+=tokens
 return nltk.FreqDist(all)


def close_words(tuples, keyword, year, window,fdWord):
 t=select(tuples, year, fdWord)
 finder = BigramCollocationFinder.from_words(t, window_size=window)
 finder.apply_ngram_filter(lambda w1, w2: keyword not in (w1, w2))
 scored=finder.score_ngrams(bigram_measures.dice)
 #pairs2=[ (p, s*fdGlobal.N()/ (fdGlobal[p[0]] + fdGlobal[p[1]])) for (p,s) in scored ]
 pairs2=scored
 pairs2Sorted=sorted(pairs2, key=lambda x: x[1], reverse=True)
 close_words=[]
 for r in pairs2Sorted[:70]:
  close_words+=r[0][0], r[0][1]
 res=[w for w in close_words if w is not keyword]
 return list(set(res))

def common(vec1, vec2):
 return [w for w in vec1 if w in vec2]



"""
# LOADING CORPUS
reader=csv.DictReader(open("corpus9612.csv", "r"))
wnl = nltk.WordNetLemmatizer()
#tum kelimeler
sentences=[]
#kelime ve yıll tuple ları
tuples=[]

for row in reader:
 text=row["HEADLINE"].lower()+" . "+row["TEXT"] 
 text=mergeNP(mergeNP(rep_coll(text),agri), medical)		
 tokens = nltk.word_tokenize(text.lower())
 tokens=[wnl.lemmatize(w) for w in tokens]
 tokens= [w for w in tokens if (len(w)>2 and w not in stopwords.words("english"))]
 sentences.append(tokens)
 for t in tokens:
  if row["YR"].strip():
   tuples.append((t, int(row["YR"])))

"""
""" SAVINGS


#save(sentences,"sentences.txt")
#save(tuples,"tuples.txt")
#save(all, "all.txt")
""""

#loadings
tuples=load(wd+"tuples.txt")
all=load(wd+"all.txt")
sentences= load(wd+"sentences.txt")	


fdWord=nltk.FreqDist(all)
fdYear=nltk.FreqDist( [y for w,y in tuples])
fdTuple=nltk.FreqDist(tuples)

"""
GMO
Verili bir kelimenin yıllar içindeki en yakın kavramları
"""

window=10
keyword="genetically_modified"

corpus=['planting', 'labeling', 'liability', 'risk', 'crop', 'contaminated', 'import', 'commercial', 'farmer', 'free', 'seed', 'moratorium', 'soy', 'feed', 'field', 'issue', 'canola', 'policy', 'safety', 'rice', 'ban', 'maize', 'cultivation', 'reuters', 'organic', 'european', 'unauthorised', 'contamination', 'panel', 'approval', 'monsanto', 'product', 'corn', 'patented', 'organism', 'genetically', 'regulation', 'use', 'gmo', 'modified', 'food']

dictDef= ['application', 'biotechnology', 'legal', 'term', 'protocol', 'close', 'separate', 'material', 'scientific', 'also', 'source', 'different', 'genetic', 'used', 'combination', 'whose', 'ground', 'history', 'modern', 'cover', 'specifically', 'obtained', 'produce', 'sorted', 'novel', 'gmos', 'living', 'altered', 'engineered', 'using', 'research', 'article', 'much', 'technical', 'engineering', 'trade', 'widely', 'release', 'defined', 'international', 'organism', 'genetically', 'regulation', 'use', 'gmo', 'modified', 'food']



print("** DETAYLI AKIŞ")

for year in fdYear.keys():
 t=select(tuples, year,fdWord)
 print("Sene: ", year, " Kelimenin o seneki frekansı ", t.count(keyword))
 words=close_words(tuples, keyword, year, window,fdWord)
 print("Corpus Sim:", len(common(words, corpus))," Wiki Sim", len(common(words, dictDef)))
 print("Corpus'a benzerlik ",common(words, corpus))
 print("Wikipedia DEfinitiona benzerlik", common(words, dictDef))
 print("***********\n")
 




print("her sene corpusa ve wik defe yakınlık")

for year in fdYear.keys():
 t=select(tuples, year,fdWord)
 words=close_words(tuples, keyword, year, window,fdWord)
 print(year,t.count(keyword),len(common(words, corpus)), len(common(words, dictDef)))
 

print("anlam vektoru")

for year in fdYear.keys():
 t=select(tuples, year,fdWord)
 words=close_words(tuples, keyword, year, window,fdWord)
 print(year, t.count(keyword),words )

 












