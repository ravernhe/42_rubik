from heuristics import Heuristics
import heapq


class Node(object):

    def __init__(self, grid, cost=0, h=0, search_type=2, parent=None):
        self.grid = grid
        self.cost = cost
        self.parent = parent
        if search_type == 3:
            self.f = h
        elif search_type == 4:
            self.f = self.cost
        else :
            self.f = self.cost + h

    def __repr__(self):
        return tuple(self.grid)

    def __hash__(self):
        return hash(self.__repr__())
        
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
    
    def __lt__(self, other):
        return self.f < other.f

    def nextnodes(self, size, heuristic, search_type):
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
                arr.append(Node(tmp, self.cost + 1, heuristic.function(tmp), search_type, self))
        return arr

         

class Solver:
    def __init__(self, grid, size, solved_grid, heuristic_name, search_type):
        self.grid = [n for row in grid for n in row]
        self.size = size
        self.solved_grid = [n for row in solved_grid for n in row]
        self.heuristic_name = heuristic_name
        self.heuristic = Heuristics(self.size, self.solved_grid, self.heuristic_name)
        self.search_type = search_type
        self.time = 0
        self.space = 0


    def print_solution(self, node):
        path = []
        while node.parent:
            path.append(node.grid)
            node = node.parent
        path.append(self.grid)
        path.reverse()
        for g in path:
            for i in range(self.size):
                print(g[i * self.size:(i + 1) * self.size])
            print("")
        print(f"Solved in {len(path) - 1} moves")
        print(f"Time complexity = {self.time}")
        print(f"Space complexity = {self.space}")
        return

    def solve(self):
        opened = set()
        openHeap = []
        closed = set()


        initial_node = Node(self.grid, 0, self.heuristic.function(self.grid), self.search_type, None)
        goal_node = Node(self.solved_grid)
        opened.add(initial_node)
        openHeap.append((0, initial_node))

        f = self.heuristic.function(initial_node.grid)
        while len(opened) > 0:
            self.time += 1
            node = heapq.heappop(openHeap)[1]
            opened.remove(node)
            closed.add(node)
            if node == goal_node:
                self.print_solution(node)
                return

            for current in node.nextnodes(self.size, self.heuristic, self.search_type):
                self.space += 1
                not_closed = False
                if not current in closed :
                    not_closed = True
                if not_closed and current not in opened:
                    opened.add(current)
                    heapq.heappush(openHeap, (current.f, current))
                else:
                    if f > current.f:
                        f = current.f
                        if not not_closed:
                            opened.add(current)
                            heapq.heappush(openHeap, (current.f, current))
                            closed.remove(current)
