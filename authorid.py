import nltk

texts = {"adambede":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/adambede.txt"),
"deronda": ("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/deronda.txt"),
"roderickhudson":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/HenryJames/roderickhudson.txt"),
"thebeastinthejungle":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/HenryJames/thebeastinthejungle.txt"),
"theinnocentsabroad":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/MarkTwain/theinnocentsabroad.txt")
}
start_end = {'adambede': ('Book One', 'SELECTED BIBLIOGRAPHY'), 
'deronda':('BOOK I', 'End of the Project Gutenberg'),
'roderickhudson':('CHAPTER I', 'End of the Project Gutenberg EBook'),
'thebeastinthejungle':('CHAPTER I', 'End of the Project Gutenberg EBook'),
'theinnocentsabroad':('CHAPTER I', 'End of the Project Gutenberg EBook')
}


book = open("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/adambede.txt")
raw = book.read().decode('utf8')

tokens = nltk.word_tokenize(raw)
print sorted(set(tokens))
print len(tokens)
types = set(tokens)
print len(types)
t_text = nltk.Text(tokens)
type(t_text)
print t_text

"""for line in text_file:
	print line"""