from os import stat
import sys
from heuristics import Heuristics
from parser import FileParser
from solvability import is_solvable, in_bound

class Node(object):

    def __init__(self, grid, cost, heuristic, parent):
        self.grid = grid
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent

    def __lt__(self, other):
        if self.heuristic + self.cost != other.heuristic + other.cost:
            return self.heuristic + self.cost < other.heuristic + other.cost
        return self.heuristic < other.heuristic
    
    def __contains__(self, other): 
        return self.grid == other


class Solver:
    def __init__(self, grid, size, solved_grid, heuristic_name):
        self.grid = tuple(tuple(row) for row in grid)
        self.size = size
        self.solved_grid = tuple(tuple(row) for row in solved_grid)
        self.heuristic_name = heuristic_name


    def move(self, grid, turn):
        new_grid = None
        directions = [
            lambda i, j: (i, j + 1),
            lambda i, j: (i + 1, j),
            lambda i, j: (i, j - 1),
            lambda i, j: (i - 1, j),
        ]
        border = [0, self.size - 1, 0, self.size -1]
        for n in range(self.size * self.size):
            if grid[n // self.size][n % self.size] == 0:
                i, j = n // self.size, n % self.size
                break
        direction_func = directions[turn % 4]
        tmp_i, tmp_j = direction_func(i, j)
        if in_bound(tmp_i, tmp_j, border):
            new_grid = [list(row) for row in grid]
            new_grid[i][j], new_grid[tmp_i][tmp_j] = new_grid[tmp_i][tmp_j], 0
            new_grid = tuple(tuple(row) for row in new_grid)
        return new_grid

    def solve(self):
        heuristic = Heuristics(self.size, self.solved_grid, self.heuristic_name)
        opened = set()
        opened.add(Node(self.grid, 0, heuristic.heuristic_func(self.grid), None))
        closed = set()
        i = -1
        print("test")
        while len(opened) > 0:
            i += 1
            if i == 200000:
                print("NUL")
                exit()
            work_node = min(opened)
            f = work_node.cost + work_node.heuristic
            if work_node.grid == self.solved_grid:
                print(f"Win en {i} iteration")
                return work_node
            for n in range(4):
                state = self.move(work_node.grid, n)
                if state:
                    is_open = False
                    for node in opened:
                        if state in node:
                            is_open = True
                    if not state in closed and not is_open:
                        opened.add(Node(state, work_node.cost + 1, heuristic.heuristic_func(state), work_node))
                    else:
                        f_new = work_node.cost + 1 + heuristic.heuristic_func(state)
                        if f > f_new:
                            f = f_new
                            opened.add(Node(state, work_node.cost + 1, heuristic.heuristic_func(state), work_node))
                            if state in closed:
                                closed.remove(state)
            opened.remove(work_node)
            closed.add(work_node.grid)

import time

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
        raise Exception("python3 n_puzzle.py [self.map_name] optional: [heuristic_function_name]")
    file_name = args[1]
    heuristic_name = "manh"
    if len(args) == 3:
        heuristic_name = args[2]
    npuzzle(file_name, heuristic_name)