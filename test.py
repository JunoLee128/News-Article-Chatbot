import spacy
from spacy import displacy
from spacy.matcher import Matcher 
from spacy.tokens import Span 

with open('test.txt', 'r', encoding='utf-8') as f:
    textdata = f.readlines()

print(textdata)
#nlp = spacy.load('en_core_web_sm')
#docs = list(nlp.pipe(textdata))
#ents = [doc.ents for doc in docs]
#print(ents)
#displacy.serve(docs, style='ent')