from DesignState import DesignState
from TermMap import TermMap

class ConnectionDesignState(DesignState):
	"""docstring for ConnectionDesignState"""
	def __init__(self):
		super(ConnectionDesignState, self).__init__()
		self.setType("connect_request")
		self.setReceiver("all")
		self.statejson['type'] = 'request'
		self.statejson['body'] = {'termlist':[],'request_type':'connect_request'}


	
	def addConnection(self, child, parent):
		# if TermMap.isConnected(child,parent):
		# 	return
		self.statejson['body']['termlist'].append({child:parent});


if __name__ == '__main__':
	connection = ConnectionDesignState()
	connection.addConnection("abc","")
	print (connection.getStateJson())