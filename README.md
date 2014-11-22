Chinese Wordnet 標記平台的 SQL 資料結構
=======
Chinese Wordnet 標記平台的資料儲存於 SQL 資料庫，請先下載 (http://lope.linguistics.ntu.edu.tw/cwnvis/data/cwn_dirty.sqlite) ，主要有三個資料表：

1. cwn_lemma：記錄 6 碼的 lemma_id、cwn_pinyin、cwn_zhuyin、lemma_sno 以及 lemma_type

2. cwn_sense：在原 lemma_id 擴增 2 碼成為 8 碼的 sense_id、lemma_id 以及 sense definition

3. cwn_goodSynset：記錄 id、gloss、synset member 的 sense_id

Chinese Wordnet 的 Python NLTK 模組
======
請 clone 本資料夾後覆蓋到 nltk_data/corpora 即可使用

取得第一個詞意：
from nltk.corpus import wordnet

wordnet.all_synsets()[0].definition

CKIP 中研院斷詞服務
======
請自行申請帳號 (http://ckipsvr.iis.sinica.edu.tw) 並寫入 ckip.py

from ckip import seg

username='your username'

password='your password'

詞意相似度計算
======
from test import similar

similar(seg(def1),seg(def2))
