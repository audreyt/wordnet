from nltk.corpus import wordnet
from ckip import seg

def similar(def1,def2):
    sum=0
    for w in def1[:-1]:
        if w in def2:sum+=1
    return sum

synsets=list(wordnet.all_synsets())

def1=seg(synsets[0].definition())
def2=seg(synsets[1].definition())
print ' '.join(def1),' '.join(def2),similar(def1,def2)
