#textblob library
#import Textblob
from textblob import TextBlob
#create a sample text

text=[
    "i love NLP, It work great and I am very satisfied",
    "This is my first experience on doing sentiment analysis, Iam little bit disappointed"
    "The NLP sentiment analysis is quiet interesting it is neither good or bad"
]

#creare function to do the sentiment analysis
def analyze_sentiment(text):
    analysis=TextBlob(text)
    #-1.0-1.0 polarity score
    polarity = analysis.sentiment.polarity
    if polarity>0:
        sentiment="postive"
    elif polarity<0:
        sentiment="negative"
    else:
        sentiment="neutral"
    return sentiment
for text in text:
    sentiment=analyze_sentiment(text)
    print(f"Text:{text}")
    print(f"sentiment:{sentiment}\n")
    