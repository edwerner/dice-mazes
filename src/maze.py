#!/usr/bin/python

import dice_node

# Reads in text file and created game grid
class Maze:

	# Array offsets for the different directions
	Up, Right, Down, Left = 0, 1, 2, 3
	
	def __init__(self, file_name):
		self.states = {}
		self.build_graph(self.read_file(file_name))
		
	# creates game matrix from text file
	def read_file(self, file_name):
		rows = []
		
		f = open(file_name, 'rU')
		for row in f:
			rows.append(list(row.rstrip()))
		f.close()
		
		return rows
	
	# Creates game grid from generated matrix
	def build_graph(self, matrix):
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				if matrix[i][j] != "*":
					node = dice_node.DiceNode("(%i, %i)" % (j, i))
					node.x, node.y = j, i
					
					if matrix[i][j] == "S": self.start = node
					if matrix[i][j] == "G": self.goal = node
					
					up = self.states.get("(%i, %i)" % (j, i - 1))
					left = self.states.get("(%i, %i)" % (j - 1, i))
					
					node.transitions[self.Up] = up
					node.transitions[self.Left] = left
					if up: up.transitions[self.Down] = node
					if left: left.transitions[self.Right] = node

					self.states[node.name] = node