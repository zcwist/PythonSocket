#coding:utf-8

import os.path

import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpclient
import tornado.websocket

import json

class IndexHandler(tornado.web.RequestHandler):
	"""docstring for IndexHandler"""
	def get(self):
		self.