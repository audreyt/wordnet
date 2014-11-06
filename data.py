from sqlite3 import connect

pos='v'

print '%08d' % 0,
count=0
conn=connect('cwn_dirty.sqlite')
c=conn.cursor()
c.execute('select * from cwn_pos where pos like "%'+pos+'%"')
for cwn_pos in c.fetchall():
    cwn_id,pos_sno,p=cwn_pos

    c.execute('select * from cwn_lemma where lemma_id="'+cwn_id[:6]+'"')
    cwn_lemma=c.fetchone()
    if cwn_lemma:
        lemma_type=cwn_lemma[4].encode('utf-8')

        c.execute('select * from cwn_sense where sense_id="'+cwn_id[:8]+'"')
        cwn_sense=c.fetchone()
        if cwn_sense:
            sense_def=cwn_sense[2].encode('utf-8')
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
