pos='r'
lines=open('data.adv').readlines()
index={}
for line in lines:
    line=line.split()
    offset=line[0]
    word=line[4]
    if word not in index:index[word]=[offset]
    else:index[word].append(offset)
for key,value in index.items():
    print key,pos,len(value),0,len(value),0,' '.join(value)
