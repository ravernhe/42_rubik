import sys
from heuristics import Heuristics
from parser import FileParser
from solvability import is_solvable, in_bound
import time
from copy import deepcopy


class Node(object):

    def __init__(self, grid, cost, heuristic, parent):
        self.grid = grid
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent
        self.f = self.heuristic + self.cost
        self.size = len(self.grid)

    def __repr__(self):
        return str([n for row in self.grid for n in row])

    def __hash__(self):
        return hash(self.__repr__())
        
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
    
    def __lt__(self, other):
        return self.f < other.f

    def nextnodes(self, heuristic):
        for n in range(self.size * self.size):
            if (self.grid[n // self.size][n % self.size] == 0):
                y, x = n // self.size, n % self.size
                break
        
        up = (y - 1, x) 
        down = (y + 1, x)
        right = (y, x + 1)
        left = (y, x - 1)

        arr = []
        for direction in (up, down, right, left):
            if len(self.grid) - 1 >= direction[0] >= 0 and len(self.grid) - 1 >= direction[1] >= 0:
                tmp = deepcopy(self.grid)
                tmp[direction[0]][direction[1]], tmp[y][x] = tmp[y][x], tmp[direction[0]][direction[1]]
                arr.append(Node(tmp, self.cost + 1, heuristic(self.grid), self))
        return arr

         

class Solver:
    def __init__(self, grid, size, solved_grid, heuristic_name):
        self.grid = grid
        self.size = size
        self.solved_grid = solved_grid
        self.heuristic_name = heuristic_name
        self.heuristic = Heuristics(self.size, self.solved_grid, self.heuristic_name)


    def solve(self):
        opened = set()
        opened.add(Node(self.grid, 0, self.heuristic.function(self.grid), None))
        closed = set()
        i = -1
        print("test")
        f = self.heuristic.function(self.grid)
        while len(opened) > 0:
            i += 1
            print(i)
            if i == 2000000:
                print("NUL")
                exit()
            work_node = min(opened)
            opened.remove(work_node)
            closed.add(work_node)
            if work_node.grid == self.solved_grid:
                print(f"Win en {i} iteration")
                return work_node
            for current in work_node.nextnodes(self.heuristic.function):
                if not current in closed and not current in opened:
                    opened.add(current)
                else:
                    if f > current.f:
                        f = current.f
                        if current in closed:
                            opened.add(current)
                            closed.remove(current)
            


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