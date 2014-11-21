CWIKIN 標記平台的 SQL 資料結構
=======
CWIKIN 標記平台的中文詞網資料儲存於 SQL 資料庫，主要有三個資料表：

1. cwnlemma：記錄 6 碼的 lemmaid 以及 lemmatype

2. cwnsense：在原 lemmaid 擴增 2 碼成為 8 碼的 senseid，以及 sense definition

3. cwngoodSynset：記錄 synset member 的 senseid
