import yake
import pickle

def get_ent_str(text):
    max_ngram_size = 3
    deduplication_threshold = 0.9
    numOfKeywords = 10
    kw_extractor = yake.KeywordExtractor(
        n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords)
    keywords = kw_extractor.extract_keywords(text)
    return str(keywords[0][0])

with open('entmapyake.pkl', 'rb') as f:
    entity_map = pickle.load(f)

inp = input('What would you like to read about?\n')
ent_str = get_ent_str(inp)
if ent_str is None or ent_str not in entity_map.keys():
    print("Couldn't find an article about that.")
else:
    print('Here you go:')
    for article in entity_map[ent_str]:
        print(article)