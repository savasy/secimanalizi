library(ca)
infile="out/KAVRAM_genç.txt"
d=read.csv(infile, sep=",")

rownames(d)<-d[,1]
d=d[,-1]


# Klasik CA uygulaması
png("out/myPlot.png", width = 20, height = 20, units = 'in', res = 200)
myca=ca(d)
plot(myca)
dev.off()


# kümeleme
# Hem kolon hem de satır değişkenkerinin
# - CA koordinatları Dim1, Dim2
# - Kelime frekasnları
# - HCLUST  kümelenmesinden oluşan cluster numaraları
#  dışarı bir dosyaya yazılıyor: doysa sonu .kume.csv
# Bu 4tableu.csv dosyası RAW DEnsity DEsign gibi araçlarla çok uyumlu çalışıyor

rc=myca$rowcoord[,1:2]
rc=cbind(rc, rowSums(d))
colcr= myca$colcoord[,1:2]
colcr=cbind(colcr, colSums(d)[-9])
all=rbind(rc,colcr)
cl=hclust(dist(all[,-3]))
clmember= cutree(cl, k = 10)
all2=as.data.frame(cbind(all,clmember))
colnames(all2)<- c("x",     "y",     "size" , "Color")
write.csv(all2,paste(infile, ".4Tableu.csv"))

