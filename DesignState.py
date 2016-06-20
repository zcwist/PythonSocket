import json

class DesignState(object):
	"""docstring for DesignState"""
	# statejson = dict()

	def __init__(self):
		super(DesignState, self).__init__()
		self.statejson = dict();

	def wrapMessage(self,message):
		self.statejson = eval(message)

	def setType(self, type):
		self.statejson['type'] = type

	def setMessage(self, message):
		self.statejson['body']= {"message":message}

	def addConnection(self, child, parent):
		self.statejson['type'] = {'request':'connect_request'}
		if ('body' not in self.statejson):
			self.statejson['body'] = []
		self.statejson['body'].append({child:parent});


	def getStateJson(self):
		return json.dumps(self.statejson)

def tester1():
	designstate = DesignState()
	designstate.setType("sys")
	designstate.setMessage("hello world")
	print(designstate.getStateJson())

def tester2():
	designstate = DesignState()
	designstate.addConnection("child1","parent1")
	designstate.addConnection("child2","parent2")
	# designstate2 = DesignState()
	# designstate2.addConnection("child4","parent1")
	# designstate2.addConnection("child3","parent2")
	print(designstate.getStateJson())
	# print(designstate2.getStateJson())

if __name__ == '__main__':
	tester2()


		