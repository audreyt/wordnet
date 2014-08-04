from xml.dom.minidom import parse

pos='r'
senses=parse('cwn_16.xml').getElementsByTagName('Sense')
synsets=parse('cwn_16.xml').getElementsByTagName('Synset')
print '%08d' % 0,
count=0
for i in range(len(senses)):
    if senses[i].getAttributeNode('synset').value[-1]==pos:
        word=senses[i].getAttributeNode('id').value
        word=word[:(len(word.encode('utf-8'))-len(word))/2].encode('utf-8')
        gloss=synsets[i].getElementsByTagName('Definition')[0].getAttributeNode('gloss').value.encode('utf-8')
        count+=27+len(word)+len(gloss)
        print '00',
        print pos,
        print '01',
        print word,
        print '0',
        print '000',
        print '|',
        print gloss
        print '%08d' % count,
