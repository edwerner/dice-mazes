#!/usr/bin/python

class CompositeState:
	# provides functionality for both maze
	# and dice state at the same time
	def __init__(self, maze_state, dice_state):
		self.maze_state = maze_state
		self.dice_state = dice_state
	
	# Define legal moves
	def moves(self):
		m_moves = self.maze_state.moves()
		d_moves = self.dice_state.moves()
		moves = {}
		for move in list(set(m_moves.keys()) & set(d_moves.keys())):
			moves[move] = (m_moves[move], d_moves[move])
		return moves
	
	# give current grid position description
	def describe_state(self):
		return "%s\n%s" % (self.maze_state.describe_state(), self.dice_state.describe_state())
	
	# get current grid state
	def get_state(self):
		return (self.maze_state.get_state(), self.dice_state.get_state())

	# ser current maze and dice states
	def set_state(self, state):
		self.maze_state.set_state(state[0])
		self.dice_state.set_state(state[1])
	
	# set goal state for maze and dice
	def goal_state(self):
		return (self.maze_state.goal_state(), self.dice_state.goal_state())
		
	# check if goal has been reached
	def goal_reached(self):
		return self.maze_state.goal_reached() and self.dice_state.goal_reached()