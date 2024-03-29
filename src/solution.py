#!/usr/bin/python

import maze
import dice
import maze_state
import dice_state
import composite_state
import search_heuristics

# Solves mazes through graph search
# and prints maze states and solutions
class Solution(object):

    # Inititalize maze and dice
    def __init__(self, file_name):
        self.maze = maze.Maze(file_name)
        self.die = dice.Die()

    # Performs A* graph search
    def search(self, cs, heuristic):
        (closed_list, g, h, f) = ({}, {}, {}, {})
        start = cs.get_state()
        goal = cs.goal_state()
        came_from = {}
        g[start] = 0
        h[start] = heuristic(start, goal)
        f[start] = h[start]
        states_generated = 1
        states_visited = 0

        print('****** Previous States ******')
        frontier = [start]
        while len(frontier) > 0:
            cs.set_state(sorted(frontier, key=lambda current: \
                         f[current])[0])
            x = cs.get_state()
            states_visited = states_visited + 1

            # Print dice moves
            if came_from.get(x):
                print('Moving ', came_from.get(x)[1])
            print(cs.describe_state(), '\n')

            if cs.goal_reached():
                self.print_states(states_generated, states_visited)
                self.print_solution(came_from, x)
                return

            frontier.remove(x)
            closed_list[x] = True

            moves = cs.moves()
            for move in moves.keys():
                y = moves[move]
                if closed_list.get(y):
                    continue

                states_generated = states_generated + 1

                tentative_g = g[x] + 1

                if y not in frontier:
                    frontier.append(y)
                    tentative_better = True
                elif tentative_g < g[y]:
                    tentative_better = True
                else:
                    tentative_better = False

                if tentative_better:
                    came_from[y] = (x, move)
                    g[y] = tentative_g
                    h[y] = heuristic(y, goal)
                    f[y] = g[y] + h[y]
        self.print_states(states_generated, states_visited)
        print('No solution found')
        print (" ")

    # Initializes search for each heuristic
    # and tracks state and possible transitions
    def solve(self):
        for heuristic in (search_heuristics.die_roll_distance,
                          search_heuristics.euclidean_distance,
                          search_heuristics.manhattan_distance):
            self.print_heuristic_name(heuristic)
            ms = maze_state.MazeState(self.maze)
            ds = dice_state.DiceState(self.die)
            cs = composite_state.CompositeState(ms, ds)
            self.search(cs, heuristic)


    # Print the solution
    def print_solution(self, came_from, current_node, first=True):

        ms = maze_state.MazeState(self.maze)
        ds = dice_state.DiceState(self.die)
        cs = composite_state.CompositeState(ms, ds)
        if came_from.get(current_node):
            last_node = current_node
            current_node = came_from.get(current_node)

            retval = self.print_solution(came_from, current_node[0], False)

            cs.set_state(current_node[0])
            print(cs.describe_state(), '\n')
            print('Move %s to:' % current_node[1])
            if first:
                cs.set_state(last_node)
                print(cs.describe_state())
                print(" ")
                print('Goal Reached!')
                print(" ")
            return retval
        else:
            print('****** Solution ******')
            print('Starting at:')

    def print_heuristic_name(self, heuristic):
        print(heuristic.__name__.replace('_', ' ').capitalize())
        print('**************************')

    def print_states(self, states_generated, states_visited):
        print('****** Results ******')
        print('Nodes generated: ', states_generated)
        print('Previous nodes:', states_visited)
        print (" ")