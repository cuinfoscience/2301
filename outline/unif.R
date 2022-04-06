draw <- runif(10000, 0, 1)

hist(draw, main="Histogram of 10000 draws") 

abline(v=.6,col="blue",lwd=2)