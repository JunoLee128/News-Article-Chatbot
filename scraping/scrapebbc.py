import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import csv
import pandas as pd
import spacy
from spacy import displacy
from spacy.matcher import Matcher 
from spacy.tokens import Span 


#def tag_visible(element):
    #if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
    #    return False 
    #if isinstance(element, Comment):
    #    return False
    #return True

def text_from_html(data):
    soup = BeautifulSoup(data, 'html.parser')
    #texts = soup.findAll(text=True)
    #visible_texts = filter(tag_visible, texts)
    #texts = soup.findAll("p")
    #print(texts)
    #return u" ".join(t.strip() for t in visible_texts)
    #return u" ".join(t.strip() for t in texts)
    ##paragraphs = soup.find_all("p", {'class': 'ssrcss-1q0x1qg-Paragraph eq5iqo00'})
    paragraphs = soup.find_all('div', {'class': 'ssrcss-7uxr49-RichTextContainer e5tfeyi1'})
    #for paragraph in paragraphs:
    #    print(paragraph.get_text())
    return u" ".join([paragraph.get_text() for paragraph in paragraphs])

def visualize(textdata):
    #docs = list(nlp.pipe(textdata))
    doc = nlp(textdata)
    #ents = [doc.ents for doc in docs]
    displacy.serve(doc, style='ent')

nlp = spacy.load('en_core_web_sm')

url = 'https://www.bbc.com/news/business-62008413'
data = requests.get(url).text
textdata = text_from_html(data)
#print(textdata)
visualize(textdata)