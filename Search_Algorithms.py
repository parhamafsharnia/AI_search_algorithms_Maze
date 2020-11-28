import Maze
from queue import Queue

"""
############################################################################
this is implementation of the uninformed search algorithms : BFS, DFS, IDS 
x = board number = j * self.row + i + 1 --> to find board number (Target)  
############################################################################
 """


class Algorithms:
    def __init__(self, f_name):
        self.maze = Maze.Maze(f_name)
        self.start_point = self.maze.start
        self.bfsqueue = Queue()
        self.dfsstack = []
        self.dlsstack = []
        self.expanded_num = 0

    def successor(self, point, cost_limit=None):
        expanded = []
        current = self.maze.cell_at(point.x, point.y)
        if cost_limit is None:
            if (current.n is True) and not self.maze.cell_at(point.x - 1, point.y).visited:
                expanded.append(self.maze.cell_at(point.x - 1, point.y))
                self.maze.cell_at(point.x - 1, point.y).parent = current.pos
            if (current.e is True) and not self.maze.cell_at(point.x, point.y + 1).visited:
                expanded.append(self.maze.cell_at(point.x, point.y + 1))
                self.maze.cell_at(point.x, point.y + 1).parent = current.pos
            if (current.s is True) and not self.maze.cell_at(point.x + 1, point.y).visited:
                expanded.append(self.maze.cell_at(point.x + 1, point.y))
                self.maze.cell_at(point.x + 1, point.y).parent = current.pos
            if (current.w is True) and not self.maze.cell_at(point.x, point.y - 1).visited:
                expanded.append(self.maze.cell_at(point.x, point.y - 1))
                self.maze.cell_at(point.x, point.y - 1).parent = current.pos
            if len(expanded) != 0:
                self.expanded_num += 1
            return expanded
        else:
            parent_cost = current.cost
            if current.cost >= cost_limit:
                return expanded  # expanded is empty here
            if (current.n is True) and not self.maze.cell_at(point.x - 1, point.y).visited:
                self.maze.cell_at(point.x - 1, point.y).cost = parent_cost + 1
                self.maze.cell_at(point.x - 1, point.y).parent = current.pos
                expanded.append(self.maze.cell_at(point.x - 1, point.y))

            if (current.e is True) and not self.maze.cell_at(point.x, point.y + 1).visited:
                self.maze.cell_at(point.x, point.y + 1).cost = parent_cost + 1
                self.maze.cell_at(point.x, point.y + 1).parent = current.pos
                expanded.append(self.maze.cell_at(point.x, point.y + 1))

            if (current.s is True) and not self.maze.cell_at(point.x + 1, point.y).visited:
                self.maze.cell_at(point.x + 1, point.y).cost = parent_cost + 1
                self.maze.cell_at(point.x + 1, point.y).parent = current.pos
                expanded.append(self.maze.cell_at(point.x + 1, point.y))

            if (current.w is True) and not self.maze.cell_at(point.x, point.y - 1).visited:
                self.maze.cell_at(point.x, point.y - 1).cost = parent_cost + 1
                self.maze.cell_at(point.x, point.y - 1).parent = current.pos
                expanded.append(self.maze.cell_at(point.x, point.y - 1))
            return expanded

    def isGoal(self, point):
        if point.x == self.maze.target.x and point.y == self.maze.target.y:
            return True
        return False

    def BFS(self, point=None):
        if point is None:
            point = self.start_point
        u = self.maze.cell_at(point.x, point.y)
        u.visited = True
        if self.isGoal(point):
            self.trace()
            return True
        expanded = self.successor(point)
        if expanded is not None:
            for item in expanded:
                self.bfsqueue.put(item)
        if not self.bfsqueue.empty():
            u = self.bfsqueue.get()
            return self.BFS(u.pos)
        return False

    def DFS(self, point=None):
        if point is None:
            point = self.start_point
        u = self.maze.cell_at(point.x, point.y)
        u.visited = True
        if self.isGoal(point):
            self.trace()
            return True
        expanded = self.successor(point)
        if expanded is not None:
            for item in expanded:
                self.dfsstack.append(item)
        if not len(self.dfsstack) == 0:
            u = self.dfsstack.pop()
            return self.DFS(u.pos)
        return False

    def DLS(self, point=None, cost_limit=0):
        if point is None:
            point = self.start_point
        u = self.maze.cell_at(point.x, point.y)
        u.visited = True
        if self.isGoal(point):
            return True
        expanded = self.successor(point, cost_limit)
        if expanded is not None:
            for item in expanded:
                self.dlsstack.append(item)
        if not len(self.dlsstack) == 0:
            u = self.dlsstack.pop()
            return self.DLS(u.pos, cost_limit)
        return False

    def IDS(self, point=None, max_depth=0):
        if max_depth == 0:
            max_depth = self.maze.maze_row * self.maze.maze_col
        if point is None:
            point = self.start_point
        for depth in range(max_depth + 1):
            self.maze.flush_visited()
            self.maze.flush_parents()
            if self.DLS(point, depth):
                self.trace()
                return True
        return False

    def trace(self):

        result = []
        current = self.maze.cell_at(self.maze.target.x, self.maze.target.y)
        while current.parent is not None:
            result.insert(0, current.pos.y * self.maze.maze_row + current.pos.x + 1)
            current_point = current.parent
            current = self.maze.cell_at(current_point.x, current_point.y)
        result.insert(0, self.start_point.y * self.maze.maze_row + self.start_point.x + 1)
        print('path: ', result)
        print('path length: ', len(result))
        print('number of expanded nodes: ', self.expanded_num)
