import requests
from bs4 import BeautifulSoup
import spacy
from spacy import displacy

def soup_filter(els):
    allowed = ['p']
    for el in els:
        if el.parent.name in allowed:
            return True
        return False

def text_from_soup(soup):
    els = soup.find_all(text=True, class_=False)
    els = filter(soup_filter, els)
    return u" ".join([el.get_text() for el in els])

def tags_from_soup(data):
    els = soup.find_all(text=True, class_='tag tag--story')
    return [el.get_text() for el in els]

def visualize(textdata):
    doc = nlp(textdata)
    displacy.serve(doc, style='ent')

nlp = spacy.load('en_core_web_sm')

url = 'https://www.npr.org/2022/07/01/1109476072/india-plastics-ban-begins'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')
textdata = text_from_soup(soup)
#visualize(textdata)
tags = tags_from_soup(soup)
print(tags)