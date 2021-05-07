# Analysis-of-Women-Safety-in-Indian-Cities-Using-Twitter-data

Analysis of Women Safety in Indian Cities Using Twitter data is to analyze women safety using social networking messages and by applying machine learning algorithms on it. Now-a-days almost all peoples are using social networking sites to express their feelings and if any women feel unsafe in any area then she will express negative words in her post/tweets/messages and by analyzing those messages we can detect which area is more unsafe for women’s.


#Steps to run the project : 

TWEEPY package from python to download tweets from twitter but every time INTERNET will not available to download tweets online so we downloaded MEETOO tweets on women safety and safe inside dataset folder. Application will read these tweets to detect women’s sentiments. 

Here we are using NLTK (Natural language tool kit) to remove special symbols and stop words from tweets and to make them clean.

Author using TEXTBLOB corpora package and dictionary to count positive, negative and neutral polarity and the tweets which has polarity value less than 0 will consider as negative as and greater than 0 and less than 0.5 will consider as neutral and polarity greater than 0.5 will consider as positive. 

To run this project, install python software and then run below command to install packages

Pip install numpy
Pip install pandas==0.25.3



