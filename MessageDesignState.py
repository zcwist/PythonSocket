import json
import time
import ast

from DesignState import DesignState

class MessageDesignState(DesignState):
	"""docstring for DesignState"""
	# statejson = dict()

	def __init__(self):
		super(MessageDesignState, self).__init__()

	def wrapMessage(self,message):
		message = str(message)
		self.statejson.update(ast.literal_eval(message))

	

	def setMessage(self, message):
		self.statejson['body']= {"message":message}

	def getContent(self):
		return self.statejson['body']['message']['content']

	


	

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


		