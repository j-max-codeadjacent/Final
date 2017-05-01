def rawifier(book, start_read, end_read):
	raw = book.read()
	start = raw.find(start_read)
	end = raw.rfind(end_read)
	raw = raw[start:end]
	return raw
	#test_book = open('test.txt', 'w')
	#test_book.write(raw)
	#test_book.close

"""book = open ("/Users/jmax.barry/Documents/Coding/DataScience/Final/Texts/unicode_adambede.txt",'r')
start_read = 'Book One'
end_read = "SELECTED BIBLIOGRAPHY"
test(book, start_read, end_read)"""
