class DiceNode:
	# Single graph node
	def __init__(self, name):
		self.name = name
		# Current x position
		self.x = None
		# Current y position
		self.y = None
		# Dice moves up, down, left, right
		self.transitions = [None, None, None, None]
		# Goal state
		self.goal = False