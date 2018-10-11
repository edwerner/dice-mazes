
# Possible grid moves
Moves = ['up', 'right', 'down', 'left']

class DiceState:

	# Keeps track of dice state and possible moves
	def __init__(self, die):
		self.die = die
		self.position = die.start
		self.north = 0
		self.history = []
	
	def set_state(self, state):
		(self.position, self.north) = state
		
	def get_state(self):
		return (self.position, self.north)
		
	def describe_state(self):
		return "North side: %s\nFacing side: %s" % (self.position.transitions[self.north].name, self.position.name)
	
	def goal_state(self):
		return (self.die.goal)
	
	def moves(self):
		# Generate set of possible moves
		moves = {}
		for move in Moves:
			self.move(move)
			# Check for valid state except for six
			if self.position != self.die.states[6]:
				moves[move] = (self.position, self.north)
			# move back to original state
			self.rewind()
		return moves
		
	def move(self, direction):
		# Converts move to method call and stores move history
		self.history.append((self.position, self.north))
		getattr(self, direction)()

	def up(self):
		old_position = self.position
		self.position = self.position.transitions[self.north - 2]
		self.north = self.position.transitions.index(old_position)

	def right(self):
		old_north = self.position.transitions[self.north]
		self.position = self.position.transitions[self.north - 3]
		self.north = self.position.transitions.index(old_north)

	def down(self):
		old_position = self.position
		self.position = self.position.transitions[self.north]
		self.north = (self.position.transitions.index(old_position) + 2) % 4

	def left(self):
		old_north = self.position.transitions[self.north]
		self.position = self.position.transitions[self.north - 1]
		self.north = self.position.transitions.index(old_north)
		
	def rewind(self):
		elm = (self.position, self.north) = self.history[-1]
		self.history.remove(elm)
	
	def goal_reached(self):
		return self.position == self.die.goal