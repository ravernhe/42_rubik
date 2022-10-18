from heuristics import Heuristics

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
                tmp = self.grid[:]
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
        self.time = 0
        self.space = 0

        self.solved_path = []

        
    def search(self, node, goal, g, threshold, path):
        f = g + self.heuristic.function(node.grid)
        self.time += 1
        if f > threshold:
            return f
   
        if node == goal:
            return True

        min = float('inf')
        neighbours = node.nextnodes(self.size)
        self.space += len(neighbours)
        for n in neighbours:
            if n not in path:
                path.add(n)
                i = self.search(n, goal, g + 1, threshold, path)
                if i == True:
                    self.solved_path.append(n.grid)
                    return True
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
            if i == True:
                self.solved_path.append(self.grid)
                self.solved_path.reverse()
                for g in self.solved_path:
                    for i in range(self.size):
                        print(g[i * self.size:(i + 1) * self.size])
                    print("")
                print(f"Solved in {len(self.solved_path) - 1} moves")
                print(f"Time complexity = {self.time}")
                print(f"Space complexity = {self.space}")
                return self.solved_path
            elif i == float("inf"):
                return None
            threshold = i
