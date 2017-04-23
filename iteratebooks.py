import fourb_author_objects as fourb
import nltk

titles = ["adambede", 'themillonthefloss', 'silasmarner', 'romola', 'felixholt', 'middlemarch', "deronda", "roderickhudson", "thebeastinthejungle", "theinnocentsabroad"]

texts = {"adambede":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/adambede.txt"),
"themillonthefloss":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/themillonthefloss.txt"),
"silasmarner":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/silasmarner.txt"),
"romola":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/romola.txt"),
"felixholt":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/felixholt.txt"),
"middlemarch":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/middlemarch.txt"),
"deronda": ("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/deronda.txt"),
"roderickhudson":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/HenryJames/roderickhudson.txt"),
"thebeastinthejungle":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/HenryJames/thebeastinthejungle.txt"),
"theinnocentsabroad":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/MarkTwain/theinnocentsabroad.txt")
}
start_end = {'adambede': ('Book One', 'SELECTED BIBLIOGRAPHY'), 
'themillonthefloss': ('Book I', 'End of the Project Gutenberg EBook'), 
'silasmarner': ('PART ONE', 'End of the Project Gutenberg EBook'), 
'romola': ('PART ONE', 'End of the Project Gutenberg EBook'), 
'felixholt': ('INTRODUCTION', 'THE END'), 
'middlemarch': ('PRELUDE', 'End of the Project Gutenberg EBook'), 
'deronda':('BOOK I', 'End of the Project Gutenberg'),
'roderickhudson':('CHAPTER I', 'End of the Project Gutenberg EBook'),
'thebeastinthejungle':('CHAPTER I', 'End of the Project Gutenberg EBook'),
'theinnocentsabroad':('CHAPTER I', 'End of the Project Gutenberg EBook')
}


#book = raw_input("What book would you like to analyze?")
#text_file = texts[book]

for x in titles:
	book = texts[x]
	raw_book = fourb.Text(open(book, 'r'), start_end[str(x)][0], start_end[str(x)][1])
	raw_book = raw_book.rawifier()


	sent_tokens = nltk.sent_tokenize(raw_book)
	total_length = 0
	for sentence in sent_tokens:
		total_length += len(sentence)
	avg_sent_length = total_length/len(sent_tokens)
	print "%r has an average sentence length of %r" %(x, avg_sent_length)

	"""tokens = nltk.word_tokenize(raw_book)
	print sorted(set(tokens))
	print len(tokens)
	types = set(tokens)
	print len(types)
	t_text = nltk.Text(tokens)
	type(t_text)"""



