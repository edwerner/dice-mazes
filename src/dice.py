#!/usr/bin/python

import dice_node

class Die:
	
	def __init__(self):
		self.states = {}
		self.build_graph()
	
	# Constructs graph and states
	def build_graph(self):
		
		# Generate states
		for i in range(1, 7):
			self.states[i] = dice_node.DiceNode("%i" % (i))
			self.states[i].x = i
		
		# Create three-dimensional dice states
		# and set start and goal states
		self.states[1].transitions = [self.states[2], self.states[4], self.states[5], self.states[3]]
		self.states[2].transitions = [self.states[6], self.states[4], self.states[1], self.states[3]]
		self.states[4].transitions = [self.states[2], self.states[6], self.states[5], self.states[1]]
		self.states[3].transitions = [self.states[2], self.states[1], self.states[5], self.states[6]]
		self.states[5].transitions = [self.states[1], self.states[4], self.states[6], self.states[3]]
		self.states[6].transitions = [self.states[5], self.states[4], self.states[2], self.states[3]]
		
		self.goal = self.states[1]
		self.start = self.states[1]