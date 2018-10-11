class CompositeState:
	"""CombinedState provides methods to perform actions on both the maze and die simultaniously."""
	def __init__(self, maze_state, dice_state):
		self.maze_state = maze_state
		self.dice_state = dice_state
	
	def set_state(self, state):
		self.maze_state.set_state(state[0])
		self.dice_state.set_state(state[1])
		
	def get_state(self):
		return (self.maze_state.get_state(), self.dice_state.get_state())
		
	def describe_state(self):
		return "%s\n%s" % (self.maze_state.describe_state(), self.dice_state.describe_state())
		
	def goal_state(self):
		return (self.maze_state.goal_state(), self.dice_state.goal_state())
	
	def moves(self):
		m_moves = self.maze_state.moves()
		d_moves = self.dice_state.moves()
		moves = {}
		for move in list(set(m_moves.keys()) & set(d_moves.keys())):
			moves[move] = (m_moves[move], d_moves[move])
		return moves
		
	def goal_reached(self):
		return self.maze_state.goal_reached() and self.dice_state.goal_reached()