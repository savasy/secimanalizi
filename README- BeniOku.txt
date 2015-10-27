Bu klasördeki 
 Metin.py ve Main.py kodları asıl kodlar

 Main.py kodu data altındaki 8 partinin secim bildirgelerini okuyup bir matris üretiyor.

- Ayrıca data/np2.txt içindeki kelimelerden bir kelime vektörü üretiyor ve partileri bu keliemeler üüzerinden görüntülüyor.
- Ayrıca data/karvam2.txt ile  keliemelre üst MEta kavramlar atayabiliyoruz

INPUT: data folder'ı altına
 *np2.txt Noun phrase
 *karvam2.txt: kavram ilişkisi
 *Belki stopword list
 * seçim bildirgeleri 

OUTPUT: 3 çıktı var

 * np ile belirtilern tüm kelimeler ve partilerin matris hali
 * her bir meta kavram altına gelen kelimelerle parti lerin matris hali, eğer 5 tane meta kavram varsa, (spor, politika, kültür, tarih, din) 5 tane dosya üretiri herbirinde özel seçilmiş ilişli kelimelerle ile 8 bildirgenin analizi yapılıypor
 * Kelimeler yerne kavramlar METa olarak temsil edilir yani yukarıdaki örnekta 5x 8 lik bir matris üzerinden hesap edilir


######
rcode.R:
Bu R dosyası Main.py tarafında üretilmiş matiris alır ve Ca analizi uyuglar bir Plot çizer ve Tabşeu ve Raw density desgin için bir dosya üretir

AGGREAGE.R ise meta kavramlar kelimelerle replace edildiği için birden fazla tekrarlar satırlar halinde. Meta düzeyinde gruplanarak bu satırların toplanması gerekmektedir. Klasik bir Goup by gibi çalışır







 
