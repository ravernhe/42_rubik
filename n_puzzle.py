from collections import deque
import sys
from heuristics import Heuristics
from parser import FileParser
from solvability import is_solvable
import time
from copy import deepcopy


class Node(object):
    def __init__(self, grid):
        self.grid = grid

    def __repr__(self):
        return tuple(self.grid)

    def __hash__(self):
        return hash(self.__repr__())
        
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def nextnodes(self, size):
        zero = self.grid.index(0)
        y, x = zero // size, zero % size

        up = (y - 1, x) 
        down = (y + 1, x)
        right = (y, x + 1)
        left = (y, x - 1)

        arr = []
        for direction in (up, down, right, left):
            if size - 1 >= direction[0] >= 0 and size - 1 >= direction[1] >= 0:
                tmp = deepcopy(self.grid)
                tmp[size * direction[0] + direction[1]], tmp[size * y + x] = tmp[size * y + x], tmp[size * direction[0] + direction[1]]
                arr.append(Node(tmp))
        return arr



class Solver:
    def __init__(self, grid, size, solved_grid, heuristic_name):
        self.grid = [n for row in grid for n in row]
        self.size = size
        self.solved_grid = [n for row in solved_grid for n in row]
        self.heuristic_name = heuristic_name
        self.heuristic = Heuristics(self.size, self.solved_grid, self.heuristic_name)
        
    def search(self, node, goal, g, threshold, path):
        f = g + self.heuristic.function(node.grid)
        
        if f > threshold:
            return f
   
        if node == goal:
            return "FOUND"

        min = float('inf')

        for n in node.nextnodes(self.size):
            if n not in path:
                path.add(n)
                i = self.search(n, goal, g + 1, threshold, path)
                if i == "FOUND":
                    return "FOUND"
                if i < min:
                    min = i
        return min

    
    def solve(self):
        initial_node = Node(self.grid)
        goal_node = Node(self.solved_grid)
        threshold = self.heuristic.function(initial_node.grid)
        while True:
            path = set([initial_node])
            i = self.search(initial_node, goal_node, 0, threshold, path)
            if i == "FOUND":
                print(len(path))
                print("TATATATA  TA  TA  TA TATA")
                return
            elif i == float("inf"):
                return None
            threshold = i


def npuzzle(file_name, heuristic_name):
    parser = FileParser(file_name)
    parser.parse()
    solved_grid = is_solvable(parser.map)
    solution = Solver(parser.map["grid"], parser.map["size"], solved_grid, heuristic_name)
    start = time.time()
    solution.solve()
    print(time.time() - start)

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2 or len(args) > 3:
        raise Exception("python3 n_puzzle.py [self.map_name] optional: [functiontion_name]")
    file_name = args[1]
    heuristic_name = "manh"
    if len(args) == 3:
        heuristic_name = args[2]
    npuzzle(file_name, heuristic_name)