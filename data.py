from sqlite3 import connect
print '%08d' % 0,
count=0
conn=connect('cwn_dirty.sqlite')
c=conn.cursor()

# begin with one sense (cwn_id) of a particular POS from cwn_pos table
pos='n' # noun,verb,adj,adv
c.execute('select * from cwn_pos where pos like "%'+pos+'%"')
processed_sense_ids=set()
for cwn_pos in c.fetchall():
    cwn_id,pos_sno,p=cwn_pos
    sense_id=cwn_id[:8]
    lemma_id=cwn_id[:6]
    # fetch the lemma_type of this sense id from cwn_lemma table
    c.execute('select * from cwn_lemma where lemma_id="'+lemma_id+'"')
    cwn_lemma=c.fetchone()
    if cwn_lemma and sense_id not in processed_sense_ids:
        # omit meaning facets of this sense
        processed_sense_ids.add(sense_id)
        lemma_type=cwn_lemma[4].encode('utf-8')
        # fetch sense_def of this sense id from cwn_sense table
        c.execute('select * from cwn_sense where sense_id="'+sense_id+'"')
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
            print ''.join(sense_def.split())
            print '%08d' % count,
