from nltk.corpus import wordnet
for synset in wordnet.all_synsets():
    print synset.name().encode('utf8'),synset.definition().encode('utf8')
