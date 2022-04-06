import pandas as pd
import csv 

out = []

# https://data.world/crowdflower/sentiment-of-climate-change

with open("1377884570_tweet_global_warming.csv", "r", encoding='utf-8', errors='ignore') as inf: 
    reader = csv.reader(inf)
    for i in reader:
        tweet, label, score = i
        if label in ["Y", "N"]:
            out.append({"tweet": tweet, "label": label})

df = pd.DataFrame(out).drop_duplicates()

df.to_csv("climate_tweets.csv", index=False)