#!/usr/bin/python

import maze
import dice

Moves = ['up', 'right', 'down', 'left']

class MazeState:

	# Initializes maze and start position
	def __init__(self, maze):
		self.maze = maze
		self.position = maze.start

	# describe current maze state
	def describe_state(self):
		return "Position: %s" % (self.position.name)
		
	# define goal states
	def goal_state(self):
		return (self.maze.goal)
		
	# Checks if goal state has been reached
	def goal_reached(self):
		return self.position == self.maze.goal

	# generates possible moves from current state
	def moves(self):
		moves = {}
		for i in range(4):
			if self.position.transitions[i]:
				moves[Moves[i]] = (self.position.transitions[i])
		return moves
	
	# Get current maze state
	def get_state(self):
		return self.position

	# Sets current maze state
	def set_state(self, state):
		(self.position) = state