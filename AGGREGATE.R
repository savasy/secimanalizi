
library(ca)
infile="out/KAVRAM_AGG.txt"
d=read.csv(infile, sep=",")

# aggregate
# birinci kolona göre AGGREGATE yapılıyor
d2=aggregate(. ~ d[,1], data =d, sum)


rownames(d2)<-d2[,1]
d2=d2[,c(-1,-2)]



png(paste(infile,"Plot.png"), width = 15, height = 15, units = 'in', res = 150)
myca=ca(d2)
plot(myca)
dev.off()


# kümeleme
# burada yine RCode.R dosaysında olduğu gibi bir analiz yapılıyor, ayrıntılar orda da var.
rc=myca$rowcoord[,1:2]
rc=cbind(rc, rowSums(d2))
colcr= myca$colcoord[,1:2]
colcr=cbind(colcr, colSums(d2)[-9])
all=rbind(rc,colcr)
cl=hclust(dist(all[,-3]))
clmember= cutree(cl, k = 10)
all2=as.data.frame(cbind(all,clmember))
colnames(all2)<- c("x",     "y",     "size" , "Color")
write.csv(all2,paste(infile, ".4tableu.csv"))


