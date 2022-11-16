import requests
from bs4 import BeautifulSoup
import spacy
from spacy import displacy

def text_from_html(data):
    soup = BeautifulSoup(data, 'html.parser')
    paragraphs = soup.find_all('div', {'class': 'ssrcss-7uxr49-RichTextContainer e5tfeyi1'})
    return u" ".join([paragraph.get_text() for paragraph in paragraphs])

def visualize(textdata):
    doc = nlp(textdata)
    displacy.serve(doc, style='ent')

def render(article):
	data = requests.get(article).text
	textdata = text_from_html(data)
	visualize(textdata)

nlp = spacy.load('en_core_web_sm')

url = 'https://www.bbc.com/news/business'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')
links = soup.find_all('a', href=True)
valid_articles = []
for lnk in links:
    print(lnk['href'])
    if lnk['href'][:15] == '/news/business-':
        valid_articles.append('http://bbc.com' + lnk['href'])
print(valid_articles)

### doesn't work, link is http://bbc.com/news/business-45489065
#render(valid_articles[0])

## this one works, link is http://bbc.com/news/business-61990864
#render(valid_articles[40])