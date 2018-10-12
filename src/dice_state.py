#!/usr/bin/python

# Possible grid moves
Moves = ['up', 'right', 'down', 'left']

# Keeps track of dice state 
# and possible moves
class DiceState:
	def __init__(self, die):
		self.die = die
		self.position = die.start
		self.north = 0
		self.history = []
		
	# Describe current dice state
	def describe_state(self):
		return "North side: %s\nFacing side: %s" % (self.position.transitions[self.north].name, self.position.name)

	# set state for goal reached
	def goal_reached(self):
		return self.position == self.die.goal
	
	# set goal state
	def goal_state(self):
		return (self.die.goal)
		
	# Converts move to method call 
	# and stores move history
	def move(self, direction):
		self.history.append((self.position, self.north))
		getattr(self, direction)()
	
	# Generates set of legal moves
	def moves(self):
		legalMoves = {}
		for move in Moves:
			self.move(move)

			# Check for valid state except for six
			if self.position != self.die.states[6]:
				legalMoves[move] = (self.position, self.north)

			# move back to original state
			self.rewind()
		return legalMoves
		
	# move back one previous move
	# and remove from history
	def rewind(self):
		elm = (self.position, self.north) = self.history[-1]
		self.history.remove(elm)

	# moves dice up on grid
	def up(self):
		old_position = self.position
		self.position = self.position.transitions[self.north - 2]
		self.north = self.position.transitions.index(old_position)

	# move dice down on grid
	def down(self):
		old_position = self.position
		self.position = self.position.transitions[self.north]
		self.north = (self.position.transitions.index(old_position) + 2) % 4

	# move dice left on grid
	def left(self):
		old_north = self.position.transitions[self.north]
		self.position = self.position.transitions[self.north - 1]
		self.north = self.position.transitions.index(old_north)

	# move dice right on grid
	def right(self):
		old_north = self.position.transitions[self.north]
		self.position = self.position.transitions[self.north - 3]
		self.north = self.position.transitions.index(old_north)
	
	# get current dice state
	def get_state(self):
		return (self.position, self.north)
		
	# sets current dice state
	def set_state(self, state):
		(self.position, self.north) = state