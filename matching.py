import spacy
from spacy import displacy
from spacy.matcher import Matcher 
from spacy.tokens import Span 

with open('wsjfordgm.txt', 'r', encoding='utf-8') as f:
    textdata = f.readlines()

nlp = spacy.load('en_core_web_sm')
ruler = nlp.add_pipe('entity_ruler', before='ner')
patterns = [{'label': 'PRODUCT', 'pattern': 'Silverado'}, 
            {'label': 'PRODUCT', 'pattern': 'F-150 Lightning'},
            {'label': 'PRODUCT', 'pattern': 'F-150'}]
ruler.add_patterns(patterns)
docs = list(nlp.pipe(textdata))
ents = [doc.ents for doc in docs]
#print(ents)
displacy.serve(docs, style='ent')