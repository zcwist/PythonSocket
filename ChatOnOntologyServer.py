import tornado.web
import tornado.ioloop
import tornado.websocket

import json

from Sentence import Sentence

class Index(tornado.web.RequestHandler):
	"""docstring for Index"""
	def get(self):
		self.render('templates/index.html')

class SocketHandler(tornado.websocket.WebSocketHandler):
	clients = set()

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

	def on_message(self, message):

		
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
		

if __name__ == '__main__':
	app = tornado.web.Application([
			('/', Index),
			('/soc', SocketHandler),
			('/pic/(.*)', tornado.web.StaticFileHandler, {'path': '/home/kiwi/code/python/OntologyChat/templates/pic/'}),
			('/static/(.*)', tornado.web.StaticFileHandler, {'path': '/home/kiwi/code/python/OntologyChat/templates/static/'}),
		])
	app.listen(8000)
	tornado.ioloop.IOLoop.instance().start()

