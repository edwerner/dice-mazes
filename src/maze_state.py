import maze
import dice

Moves = ['up', 'right', 'down', 'left']

class MazeState:

	# Keeps trach of maze state and possible moves
	def __init__(self, maze):
		self.maze = maze
		self.position = maze.start
		
	def set_state(self, state):
		(self.position) = state
		
	def get_state(self):
		return self.position
		
	def describe_state(self):
		return "Position: %s" % (self.position.name)
		
	def goal_state(self):
		return (self.maze.goal)
		
	def moves(self):
		# generates possible moves from current state
		moves = {}
		for i in range(4):
			if self.position.transitions[i]:
				moves[Moves[i]] = (self.position.transitions[i])
		return moves
	
	def goal_reached(self):
		return self.position == self.maze.goal