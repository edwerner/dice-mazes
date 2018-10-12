#!/usr/bin/python

import math

# Creates distance and uses rules to increase distance
# Dice must never show 6 side up
# Dice can only move vertically and horizontally
# Checks whether dice is on its side for optimal path 
# to goal state
def die_roll_distance(start, goal):
	x1, y1, top1 = start[0].x, start[0].y, start[1][0].x
	x2, y2, top2 = goal[0].x, goal[0].y, goal[1].x
	
	# One side is not facing up
	dx, dy, on_side = math.fabs(x1 - x2), math.fabs(y1 - y2), top1 != top2
	manhattan = manhattan_distance(start, goal)
	
	if dx == 0 and dy == 0 and not on_side:
		return manhattan
	
	if dx == 0 and dy == 0 and on_side:
		return 4
		
	if dx == 0 and dy > 0 and not on_side:
		return manhattan + 2
		
	if dx > 0 and dy == 0 and not on_side:
		return manhattan + 2
		
	if dx >= 0 and dy == 1 and on_side:
		return manhattan 
	
	if dx == 1 and dy >= 0 and on_side:
		return manhattan
	
	# special case 1
	if dx > 0 and dy > 0 and not on_side:
		return manhattan + 4
	
	# special case 2
	if dx > 0 and dy > 0 and on_side:
		return manhattan + 2
	
	# defaultn return
	return manhattan
	
# Creates manhattan distance between 
# current position and goal state	
def manhattan_distance(start, goal):
	x1, y1 = start[0].x, start[0].y
	x2, y2 = goal[0].x, goal[0].y
	return math.fabs(x1 - x2) + math.fabs(y1 - y2)

def euclidian_distance(start, goal):
	# Creates euclidian distance between current 
	# position and goal state
	# Dice must move vertically or horizontally
	x1, y1 = start[0].x, start[0].y
	x2, y2 = goal[0].x, goal[0].y
	return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))