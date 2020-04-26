import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

df = pd.read_csv('scraped_raw_data.csv')

company = df['news'].apply(lambda x: x.split('*')[1])
df['company'] = company
df['news'] = df['news'].apply(lambda x:x.split('*')[0])
df.columns
df.head(10)



corpus = []
for i in range(0,546):
    review = re.sub('[^a-zA-Z]', ' ', df['news'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)

#word cloud
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
words = " ".join(corpus)
def punctuation_stop(text):
    filtered = []
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    for w in word_tokens:
        if w not in stop_words and w.isalpha():
            filtered.append(w.lower())
    return filtered
    
words_filtered = punctuation_stop(words)
text = " ".join([ele for ele in words_filtered])

wc = WordCloud(background_color = 'white', random_state = 1, stopwords = STOPWORDS, max_words = 6000,
               width = 800, height = 1500)
wc.generate(text)
plt.figure(figsize = [10,10])
plt.imshow(wc, interpolation = "bilinear")
plt.axis('off')
plt.show()

words = " ".join(corpus)
def punctuation_stop(text):
    filtered = []
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    for w in word_tokens:
        if w not in stop_words and w.isalpha():
            filtered.append(w.lower())
    return filtered
    
words_filtered = punctuation_stop(words)
text = " ".join([ele for ele in words_filtered])

wc = WordCloud(background_color = 'white', random_state = 1, stopwords = STOPWORDS, max_words = 500,
               width = 800, height = 1500)
wc.generate(text)
plt.figure(figsize = [10,10])
plt.imshow(wc, interpolation = "bilinear")
plt.axis('off')
plt.savefig('WordCloud.png', dpi = 100)
plt.show()







