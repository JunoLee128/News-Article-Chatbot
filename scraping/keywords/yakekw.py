import requests
from bs4 import BeautifulSoup
import time
import pickle
from datetime import date, timedelta
import yake

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

START_DATE = date(2022, 7, 1)
END_DATE = date(2022, 7, 5)

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
    print('getting <{}>'.format(article))
    data = requests.get(article).text 
    textdata = text_from_html(data)
    max_ngram_size = 3
    deduplication_threshold = 0.9
    numOfKeywords = 10
    kw_extractor = yake.KeywordExtractor(
        n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords)
    keywords = kw_extractor.extract_keywords(textdata)
    for kw in keywords:
        kw_str = kw[0]
        if not kw_str in entity_map:
            entity_map[kw_str] = set()
        entity_map[kw_str].add(article)

with open('entmapyake.pkl', 'wb') as f:
    pickle.dump(entity_map, f)
