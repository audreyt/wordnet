from sqlite3 import connect

print '%08d' % 0,
count=0
conn=connect('cwn_dirty.sqlite')
c=conn.cursor()
c.execute('select * from cwn_pos where pos like "%N%"')
for cwn_pos in c.fetchall():
    cwn_id,pos_sno,pos=cwn_pos

    c.execute('select * from cwn_lemma where lemma_id="'+cwn_id[:6]+'"')
    cwn_lemma=c.fetchone()
    if cwn_lemma:
        lemma_type=cwn_lemma[4].encode('utf-8')

        c.execute('select * from cwn_sense where sense_id="'+cwn_id[:8]+'"')
        cwn_sense=c.fetchone()
        if cwn_sense:
            sense_def=cwn_sense[2].encode('utf-8')

   #         print
    #        print 'cwn_id',cwn_id[:8]
     #       print 'sense_def',sense_def

    
#    print ' '.join([pos,lemma_type,sense_def]).encode('utf-8')

#for i in range(len(senses)):
 #   if senses[i].getAttributeNode('synset').value[-1]==pos:
  #      word=senses[i].getAttributeNode('id').value
   #     word=word[:(len(word.encode('utf-8'))-len(word))/2].encode('utf-8')
    #    gloss=synsets[i].getElementsByTagName('Definition')[0].getAttributeNode('gloss').value.encode('utf-8')
            count+=27+len(lemma_type)+len(sense_def)
            print '00',
            print pos,
            print '01',
            print lemma_type,
            print '0',
            print '000',
            print '|',
            print sense_def
            print '%08d' % count,
