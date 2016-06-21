from DesignStateSolver import DesignStateSolver
from StatesBroadcaster import StatesBroadcaster

if __name__ == '__main__':
	message = '{"type":"dialog","body":{"message":{"content":"#hey#","parent":""}}}'
	solver = DesignStateSolver(message)
	broadcaster = StatesBroadcaster(solver.getStateToSend(),"abc")
	broadcaster.broadcast()