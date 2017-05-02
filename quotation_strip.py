# -- coding: utf-8 --
def quote_strip(title):
	lines_noquotes = []
	book = open(title, 'r')
	book = book.readlines()
	for line in book:
		line = line.replace('“','').replace('”','')
		lines_noquotes.append(line)
	
