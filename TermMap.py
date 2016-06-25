
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

	def getTermMap(self):
		return self.termMap

	def addTerm(self,term):
		self.termList.append(term)

	def addConnection(self,child,parent):
		if (not self.isConnected(child,parent)):
			if (child not in self.termMap):
				self.termMap[child] = []
			self.termMap[child].append(parent)

	# def isConnected(self,child,parent):
	# 	print ("****")
	# 	print (self.termMap[child])
	# 	print ("****")
	# 	if parent in self.termMap[child]:
	# 		return True
	# 	return False
	def isConnected(self,child,parent):
		if parent != "":
			if (child in self.termMap.keys()):
				if parent in self.termMap[child]:
					return True
		return False

	def getStatistics(self):
		sta = {}
		sta['terms#'] = len(self.termList)
		sta['relations#'] = 0
		for termrelaions in self.termMap:
			sta['relations#'] += len(self.termMap[termrelaions])
		return sta



def tester():
	# termMap = TermMap()
	# termMap2 = TermMap()
	# print(termMap.getTerms())
	# TermMap.addTerm("abc")
	# print(termMap2.getTerms())
	# print(termMap.getTerms())
	TermMap.addTerm("abc")
	TermMap.addTerm("bcd")
	TermMap.addConnection("abc","bcd")
	TermMap.addConnection("abc","bcd")
	TermMap.addConnection("bcd","abc")
	print(TermMap.getStatistics())

if __name__ == '__main__':
	tester()