from DesignState import DesignState

class StatesBroadcaster(object):
	"""docstring for StatesBroadcaster"""
	def __init__(self, states, socketHandler):
		super(StatesBroadcaster, self).__init__()
		self.states = states
		self.socketHandler = socketHandler

	def broadcast(self):
		for state in self.states:
			
			receiver = state.getReceiver()
			if receiver == "all":
				self.socketHandler.send_to_all(state.getStateJson())
			elif receiver == "other":
				self.socketHandler.send_to_other(state.getStateJson())
			elif receiver == "self":
				self.socketHandler.send_to_self(state.getStateJson())
