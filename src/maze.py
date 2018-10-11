import dice_node

class Maze:	 
	"""Maze takes in a file and builds a maze graph from it."""
	
	"""Array offsets for the different directions."""
	Up, Right, Down, Left = 0, 1, 2, 3
	
	def __init__(self, file_name):
		self.states = {}
		self.build_graph(self.read_file(file_name))
		
	def read_file(self, file_name):
		"""Builds a matrix from the input file where each character is a cell."""
		rows = []
		
		f = open(file_name, 'rU')
		for line in f:
			rows.append(list(line.rstrip()))
		f.close()
		
		return rows
	
	def build_graph(self, matrix):
		"""Builds a graph from the matrix generated from the maze file."""
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