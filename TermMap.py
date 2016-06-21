
def singleton(cls):
   instance = cls()
   instance.__call__ = lambda: instance
   return instance

@singleton
class TermMap():
	termList = list()
	termMap = dict()

	def getTerms(self):
		return self.termList

	def addTerm(self,term):
		self.termList.append(term)

	def addConnection(self,child,parent):
		if (child not in self.termMap):
			self.termMap[child] = []
		self.termMap[child].append(parent)



def tester():
	# termMap = TermMap()
	# termMap2 = TermMap()
	# print(termMap.getTerms())
	# TermMap.addTerm("abc")
	# print(termMap2.getTerms())
	# print(termMap.getTerms())
	TermMap.addTerm("abc")
	print(TermMap.getTerms())

if __name__ == '__main__':
	tester()