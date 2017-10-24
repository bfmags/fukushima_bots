import nltk
from nltk.corpus import wordnet as wn

def find_terms(text):
	sentences = nltk.sent_tokenize(text) #tokenize sentences
	nouns = [] #empty to array to hold all nouns
	keywords = set()

	for sentence in sentences:
	     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
	         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
	             nouns.append(word)

	for noun in nouns: 
		for syn in wn.synsets(noun):
			keywords.update(syn.lemma_names())

	return tuple(keywords)