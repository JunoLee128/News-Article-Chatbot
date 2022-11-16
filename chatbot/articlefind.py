import requests
from bs4 import BeautifulSoup
import spacy
from spacy import displacy
import time
import pickle

def get_ent_str(text):
    doc = nlp(text)
    if doc.ents:
        return str( doc.ents[0] )

nlp = spacy.load('en_core_web_sm')

with open('entmap.pkl', 'rb') as f:
    entity_map = pickle.load(f)

inp = input('What would you like to read about?\n')
ent_str = get_ent_str(inp)
if ent_str is None or ent_str not in entity_map.keys():
    print("Couldn't find an article about that.")
else:
    print('Here you go:')
    for article in entity_map[ent_str]:
        print(article)