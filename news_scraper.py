from bs4 import BeautifulSoup
from datetime import date
import requests
import spacy
today = date.today()
d = today.strftime("%m-%d-%y")

url = "https://edition.cnn.com/world/live-news/coronavirus-pandemic-{}-intl/index.html".format(d)
url1 = "https://www.hindustantimes.com/it-s-viral/"
print(url)

html = requests.get(url1).text
soup = BeautifulSoup(html)
print(soup.title)

nlp = spacy.load('en_core_web_sm')

data = []
for link in soup.find_all("div", {"class" : "media-heading headingfour"}):
    print("Headline : {}".format(link.text))
    for ent in nlp(link.text).ents:
        print("\tText : {}, Entity : {}".format(ent.text, ent.label_))
