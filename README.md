Chinese Wordnet 標記平台的 SQL 資料結構
=======
Chinese Wordnet 標記平台的資料儲存於 SQL 資料庫，主要有三個資料表：

1. cwn_lemma：記錄 6 碼的 lemma_id、cwn_pinyin、cwn_zhuyin、lemma_sno 以及 lemma_type

2. cwn_sense：在原 lemmaid 擴增 2 碼成為 8 碼的 senseid、lemma_id 以及 sense definition

3. cwn_goodSynset：記錄 id、gloss、synset member 的 senseid
