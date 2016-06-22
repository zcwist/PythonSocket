import tornado.web
import tornado.ioloop
import tornado.websocket

import json

from Sentence import Sentence
from DesignState import DesignState
from DesignStateSolver import DesignStateSolver
from StatesBroadcaster import StatesBroadcaster

class Index(tornado.web.RequestHandler):
	"""docstring for Index"""
	def get(self):
		self.render('templates/index.html')

class SocketHandler(tornado.websocket.WebSocketHandler):
	clients = set()
	terms = set()

	@staticmethod
	def send_to_all(message):
		for c in SocketHandler.clients:
			c.write_message(json.dumps(message))

	def send_to_other(self,message):
		for c in SocketHandler.clients:
			if not (c is self):
				c.write_message(json.dumps(message))

	def send_to_self(self,message):
		self.write_message(json.dumps(message))


	def open(self):
		self.write_message(json.dumps({
			'type':'sys',
			'message':'Welcome to WebSocket',
			}))
		SocketHandler.send_to_all({
			'type':'sys',
			'message': str(id(self)) + ' has joined',
			})
		SocketHandler.clients.add(self)

	def on_close(self):
		SocketHandler.clients.remove(self)
		SocketHandler.send_to_all({
			'type': 'sys',
			'message': str(id(self)) + ' has left',
			})

	# def on_message(self, message): # abandoned 
		designState = DesignState()
		designState.wrapMessage(message)
		designState.setId(id(self))
		# print(message)
		print(designState.getStateJson())

		stateType = designState.getType()




		if ('request' in eval(message)['type']):
			SocketHandler.send_to_all({
				'type': 'request',
				'message': eval(message)
				})
			return
		
		SocketHandler.send_to_other(self,{
			'type': 'user',
			'id': id(self),
			'message': eval(message),
			})

		SocketHandler.send_to_self(self,{
			'type': 'self',
			'id': id(self),
			'message': eval(message),
			})

		sentence = Sentence(message)
		termlist = sentence.getTerms()

		for term in termlist:
			if (term in SocketHandler.terms):
				termlist.remove(term)
			else:
				SocketHandler.terms.add(term)
			
		if (len(termlist) != 0):
			newmessage = {
				"termlist": termlist,
				"parent": eval(message)['parent']
			}
			SocketHandler.send_to_all({
				'type': 'term',
				'id': id(self),
				'message': newmessage,
				})

	def on_message(self, message):
		# print(message)
		solver = DesignStateSolver(message)
		broadcaster = StatesBroadcaster(solver.getStateToSend(),self)
		broadcaster.broadcast()
		

if __name__ == '__main__':
	app = tornado.web.Application([
			('/', Index),
			('/soc', SocketHandler),
			('/pic/(.*)', tornado.web.StaticFileHandler, {'path': './templates/pic/'}),
			('/static/(.*)', tornado.web.StaticFileHandler, {'path': './templates/static/'}),
		])
	app.listen(8000)
	tornado.ioloop.IOLoop.instance().start()

