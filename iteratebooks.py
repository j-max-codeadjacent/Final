import fourb_author_objects as fourb
import nltk
from openpyxl import Workbook

titles = ["adambede", 'themillonthefloss', 'silasmarner', 'romola', 'felixholt', 'middlemarch', "deronda", 
"roderickhudson", "theamericans", 'theeuropeans', 'confidence', 'portraitofaladyvol1', 'portraitofaladyvol2', 'thegoldenbowl', "thebeastinthejungle", 
"theinnocentsabroad", "roughingit", "theadventuresoftomsawyer", 'lifeonthemississippi', 'aconnecticutyankee', 'thetragedyofpuddnhead', 'joanofarcvol1', 'joanofarcvol2']

texts = {"adambede":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/adambede.txt"),
"themillonthefloss":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/themillonthefloss.txt"),
"silasmarner":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/silasmarner.txt"),
"romola":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/romola.txt"),
"felixholt":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/felixholt.txt"),
"middlemarch":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/middlemarch.txt"),
"deronda": ("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/GeorgeEliot/deronda.txt"),
"roderickhudson":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/HenryJames/roderickhudson.txt"),
"theamericans":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/HenryJames/theamericans.txt"),
"theeuropeans":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/HenryJames/theeuropeans.txt"),
"confidence":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/HenryJames/confidence.txt"),
"portraitofaladyvol1":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/HenryJames/portraitofaladyvol1.txt"),
"portraitofaladyvol2":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/HenryJames/portraitofaladyvol2.txt"),
"thegoldenbowl":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/HenryJames/thegoldenbowl.txt"),
"thebeastinthejungle":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/HenryJames/thebeastinthejungle.txt"),
"theinnocentsabroad":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/MarkTwain/theinnocentsabroad.txt"),
"roughingit":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/MarkTwain/roughingit.txt"),
"theadventuresoftomsawyer":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/MarkTwain/theadventuresoftomsawyer.txt"),
"lifeonthemississippi":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/MarkTwain/lifeonthemississippi.txt"),
"aconnecticutyankee":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/MarkTwain/aconnecticutyankee.txt"),
"thetragedyofpuddnhead":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/MarkTwain/thetragedyofpuddnhead.txt"),
"joanofarcvol1":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/MarkTwain/joanofarcvol1.txt"),
"joanofarcvol2":("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/MarkTwain/joanofarcvol2.txt")
}

start_end = {'adambede': ('Book One', 'SELECTED BIBLIOGRAPHY'), 
'themillonthefloss': ('Book I', 'End of the Project Gutenberg EBook'), 
'silasmarner': ('PART ONE', 'End of the Project Gutenberg EBook'), 
'romola': ('PART ONE', 'End of the Project Gutenberg EBook'), 
'felixholt': ('INTRODUCTION', 'THE END'), 
'middlemarch': ('PRELUDE', 'End of the Project Gutenberg EBook'), 
'deronda':('BOOK I', 'End of the Project Gutenberg'),
'roderickhudson':('CHAPTER I', 'End of the Project Gutenberg EBook'),
'theamericans':('On a brilliant', 'End of the Project Gutenberg EBook'),
'theeuropeans':('A narrow grave-yard', 'The End'),
'confidence':('CHAPTER I', 'End of the Project Gutenberg EBook'),
'portraitofaladyvol1':('Under certain circumstances', 'End of the Project Gutenberg EBook'),
'portraitofaladyvol2':('CHAPTER XXVIII', 'End of the Project Gutenberg EBook'),
'thegoldenbowl':('BOOK FIRST: THE PRINCE', 'End of the Project Gutenberg EBook'),
'thebeastinthejungle':('CHAPTER I', 'End of the Project Gutenberg EBook'),
'theinnocentsabroad':('CHAPTER I', 'End of the Project Gutenberg EBook'),
'roughingit':('My brother had just been', 'End of the Project Gutenberg EBook'),
'theadventuresoftomsawyer':('TOM!', 'End of the Project Gutenberg EBook'),
'lifeonthemississippi':('The River and Its History', 'End of the Project Gutenberg EBook'),
'aconnecticutyankee':('The ungentle laws', 'End of the Project Gutenberg EBook'),
'thetragedyofpuddnhead':('A Whisper', 'Transcriber\'s Notes'),
'joanofarcvol1':('By The Sieur Louis De Conte', 'End of the Project Gutenberg EBook'),
'joanofarcvol2':('BOOK II -- IN COURT AND CAMP (Continued)', 'End of the Project Gutenberg EBook')
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

wb = Workbook()

dest_filename = 'novel_data.xlsx'
ws1 = wb.active



