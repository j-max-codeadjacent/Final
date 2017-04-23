class Text(object):
	def __init__(self, text_file, start_read, end_read):
		self.text_file = text_file
		self.start_read = start_read
		self.end_read = end_read

	def rawifier(self):
		raw = self.text_file.read().decode('utf8')
		start = raw.find(self.start_read)
		end = raw.rfind(self.end_read)
		raw = raw[start:end]
		return raw

