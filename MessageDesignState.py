import json
import time


from DesignState import DesignState

class MessageDesignState(DesignState):
	"""docstring for DesignState"""
	# statejson = dict()

	def __init__(self):
		super(MessageDesignState, self).__init__()

	
	

	def setMessage(self, message):
		self.statejson['body']= {"message":message}

	def getContent(self):
		return self.statejson['body']['message']['content']

	def getParent(self):
		return self.statejson['body']['message']['parent']

	


	

def tester1():
	designstate = DesignState()
	designstate.setType("sys")
	designstate.setMessage("hello world")
	print(designstate.getStateJson())

def tester2():
	designstate = DesignState()
	# designstate.addConnection("child1","parent1")
	# designstate.addConnection("child2","parent2")
	# designstate2 = DesignState()
	# designstate2.addConnection("child4","parent1")
	# designstate2.addConnection("child3","parent2")
	print(designstate.getStateJson())
	# print(designstate2.getStateJson())

if __name__ == '__main__':
	tester2()


		