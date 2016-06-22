from DesignState import DesignState
from Sentence import Sentence
from TermMap import TermMap
from MessageDesignState import MessageDesignState
from ConnectionDesignState import ConnectionDesignState

class DesignStateSolver(object):
	"""docstring for DesignStateSolver"""
	def __init__(self,message):
		super(DesignStateSolver, self).__init__()
		self.receivedState = MessageDesignState()
		self.receivedState.wrapMessage(message)
		self.stateToSend = list()
		self.process()

	def process(self):
		messageType = self.receivedState.getType()
		# common dialog
		if ("dialog" in messageType):
			#broadcast the message
			#egstr = '{"body": {"message": {"parent": "", "content": "#hey#"}}, "id": 140533467296152, "type": "dialog", "time_stamp": 1466492384.1284246}'
			


			messageToSelf = MessageDesignState()
			messageToSelf.wrapMessage(self.receivedState.getStateJson())
			messageToSelf.setReceiver('self')
			self.stateToSend.append(messageToSelf)


			messageToOther = MessageDesignState()
			messageToOther.wrapMessage(self.receivedState.getStateJson())
			messageToOther.setReceiver('other')
			self.stateToSend.append(messageToOther)



			# print("broadcasting")
			# self.printStatesToSend()

			#extract terms
			sentence = Sentence(self.receivedState.getContent())
			termlist = sentence.getTerms()

			termMap = TermMap



			parent = self.receivedState.getParent()

			if (parent == ""):

				for term in termlist:
					#term appear in the term map, extract semantic relation
					if (term in termMap.getTerms()):
						parent = term
						continue
					

					connection = ConnectionDesignState()
					connection.addConnection(term, parent)
					self.stateToSend.append(connection)

					termMap.addTerm(term)
					termMap.addConnection(term,parent)

			else:
				for term in termlist:
					connection = ConnectionDesignState()
					connection.addConnection(term, parent)
					self.stateToSend.append(connection)
					termMap.addConnection(term,parent)


		# connect request
		
		if ('request' in messageType):
			requestState = ConnectionDesignState()
			requestState.wrapMessage(self.receivedState.getStateJson())

			self.stateToSend.append(requestState)



	def getStateToSend(self):
		return self.stateToSend

	def printStatesToSend(self):
		# print ("There are %d states to send", len(self.stateToSend))
		for ds in self.stateToSend:
			print (ds.getStateJson())



def tester1():
	egstr1 = '{"body": {"message": {"parent": "", "content": "#hey#"}}, "id": 140533467296152, "type": "dialog", "time_stamp": 1466492384.1284246}'
	egstr2 = '{"body": {"message": {"parent": "", "content": "#hey#, #you#"}}, "id": 140533467296152, "type": "dialog", "time_stamp": 1466492384.1284246}'
	designStateSolver1 = DesignStateSolver(egstr1)

	print ("For message1") 
	designStateSolver1.printStatesToSend()

	designStateSolver2 = DesignStateSolver(egstr2)

	print ("For message2") 
	designStateSolver2.printStatesToSend()

if __name__ == '__main__':
	tester1()

