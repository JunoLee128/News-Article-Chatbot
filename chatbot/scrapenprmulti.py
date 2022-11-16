from tkinter import END
import requests
from bs4 import BeautifulSoup
import spacy
from spacy import displacy
import time
import pickle
from datetime import date, timedelta

def soup_filter(els):
    allowed = ['p']
    for el in els:
        if el.parent.name in allowed:
            return True
        return False

def text_from_html(data):
    soup = BeautifulSoup(data, 'html.parser')
    els = soup.find_all(text=True, class_=False)
    els = filter(soup_filter, els)
    return u" ".join([el.get_text() for el in els])

def visualize(textdata):
    doc = nlp(textdata)
    displacy.serve(doc, style='ent')

def render(article):
	data = requests.get(article).text
	textdata = text_from_html(data)
	visualize(textdata)

START_DATE = date(2022, 6, 1)
END_DATE = date(2022, 7, 5)

nlp = spacy.load('en_core_web_sm')

date = START_DATE
valid_articles = set()

while date <= END_DATE:
    url = 'https://www.npr.org/sections/business/archive?date=' \
        + time.strftime("%m-%d-%Y", date.timetuple())
    print('processing {}'.format(url))
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    links = soup.find_all('a', href=True)
    valid_start = 'https://www.npr.org/' \
        + time.strftime("%Y/%m/%d/", date.timetuple())
    for lnk in links:
        if lnk['href'].startswith(valid_start):
            valid_articles.add(lnk['href'])
    date += timedelta(days=1)

entity_map = {}

print('scraping {} articles.'.format(len(valid_articles)))

for article in valid_articles:
    time.sleep(0.25) #could use scrapy
    print('getting <{}>'.format(article))
    data = requests.get(article).text 
    textdata = text_from_html(data)
    doc = nlp(textdata)
    for ent in doc.ents:
        ent_str = str(ent)
        if not ent_str in entity_map:
            entity_map[ent_str] = set()
        entity_map[ent_str].add(article)

with open('entmap.pkl', 'wb') as f:
    pickle.dump(entity_map, f)


#print(valid_articles)
#render(valid_articles[0])