#following tutorial: https://pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/?completed=/stemming-nltk-tutorial/
import nltk
from nltk.tokenize import PunktSentenceTokenizer
from openpyxl import Workbook
import regex as re
import ba_titlekeys as ba
#Title keys, titles{title_key: author, year}, texts{title_key: pathtotext}



authorwords = {}

key = ba.title_keys[0] #middlemarch in this instance
train_text = open("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/aa_training/chone_mm.txt").read().decode('UTF8')
sample_text = open("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/aa_training/chtwo_mm.txt").read().decode('UTF8')

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
	for i in tokenized[:5]:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			print(tagged)

process_content()

#train_text = 

