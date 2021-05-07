from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
from string import punctuation
from nltk.corpus import stopwords
import pandas as pd
from tkinter import *

tweets_list = []

def tweetCleaning(doc):
    tokens = doc.split()
    table = str.maketrans('', '', punctuation)
    tokens = [w.translate(table) for w in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    tokens = [word for word in tokens if len(word) > 1]
    tokens = ' '.join(tokens) #here upto for word based
    return tokens

def connectTweet():
    tweets_list.clear()
    filename = filedialog.askopenfilename(initialdir = "dataset")
    train = pd.read_csv(filename,encoding='iso-8859-1')
    for i in range(len(train)):
        tweet = train.get_value(i, 'Text')
        tweets_list.append(tweet)
        tweet = tweet.strip("\n")
        tweet = tweet.strip()
        tweet = tweetCleaning(tweet.lower())
        blob = TextBlob(tweet)
        if blob.polarity <= 0.2:
            print (str(blob)+" ===== Negative "+str(blob.polarity))
        if blob.polarity > 0.2 and blob.polarity <= 0.5:
            print (str(blob)+" ===== Neutral "+str(blob.polarity))
        if blob.polarity > 0.5:
            print (str(blob)+" ===== Positive "+str(blob.polarity))
connectTweet()
