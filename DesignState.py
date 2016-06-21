import json
import time

class DesignState(object):
	"""docstring for DesignState"""
	def __init__(self):
		super(DesignState, self).__init__()
		self.statejson = dict()
		self.statejson['time_stamp'] = time.time()
	def setId(self, id):
		self.statejson['id'] = id

	def setReceiver(self, receiver):
		self.statejson['receiver']=receiver

	def getReceiver(self):
		return self.statejson['receiver']

	def setType(self, type):
		self.statejson['type'] = type

	def getType(self):
		return self.statejson['type']

	def getStateJson(self):
		return self.statejson
		