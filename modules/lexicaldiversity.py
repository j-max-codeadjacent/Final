#lexical diversity
from __future__ import division

def lexical_diversity(text):
	tokens = nltk.word_tokenize(text)
	lex_div = len(tokens)/len(text)
	print lex_div