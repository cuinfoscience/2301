one.dice <- function(){
  dice <- sample(1:6, size = 1, replace = TRUE)
  return(dice)
}

loaded.dice <- function(){
  dice <- sample(1:6, size = 1, replace = TRUE, prob=c(3/6, 0, 0, 0, 0, 3/6))
  return(dice)
}

sims <- replicate(10000, one.dice())

ggplot(as.tibble(sims), aes(x=value)) + geom_histogram() + ggtitle("A")

Lsims <- replicate(10000, loaded.dice())

ggplot(as.tibble(Lsims), aes(x=value)) + geom_histogram() + ggtitle("B")
