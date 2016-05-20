class Sentence(object):
	"""docstring for Sentence"""
	def __init__(self, sen):
		super(Sentence, self).__init__()
		self.sen = sen
	
	def getTerms(self):
		termList = []
		flag = 0
		while True:
			start = self.sen.find('#', flag) + 1
			flag = start
			if (not flag): 
				break
			end = self.sen.find('#', start)
			if (end == -1):
				break
			flag = end + 1
			termList.append(self.sen[start:end])

		return termList

if __name__ == '__main__':
	sentence = Sentence("I'm a #Mac#. I am not #Ubuntu#. Lol")
	print (sentence.getTerms())