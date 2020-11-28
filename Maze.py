"""
this class is for preparing the screen, start pos, and target pos

"""
import Cell
from POINT import Point


class Maze:
    """A Maze, represented as a grid of cells."""

    def __init__(self, infile: str):
        """Initialize the maze grid.
        The maze consists of nx x ny cells and will be constructed starting
        at the cell indexed at (ix, iy).

        """
        self.data = infile
        self.data_list = []
        self.maze_row = None
        self.maze_col = None
        self.start: Point = None
        self.target: Point = None
        self.maze_map = []
        self.fetch()

    def cell_at(self, x, y):
        """Return the Cell object at (x,y)."""

        return self.maze_map[x][y]

    def flush_parents(self):
        for i in range(self.maze_row):
            for j in range(self.maze_col):
                self.maze_map[i][j].parent = None

    def flush_visited(self):
        for i in range(self.maze_row):
            for j in range(self.maze_col):
                self.maze_map[i][j].visited = False

    def set_size(self):
        size = self.data_list[0].split(' ')
        self.maze_row = int(size[0])
        self.maze_col = int(size[1])

    def set_s_t(self):
        st = self.data_list[len(self.data_list) - 1].split(' ')
        self.start = Point(int(st[0]) % self.maze_row - 1, int(st[0]) // self.maze_row)
        self.target = Point(int(st[1]) % self.maze_row - 1, int(st[1]) // self.maze_row)

    def fetch(self):
        # try:
        with open(self.data, 'r', ) as _infile:
            self.data_list = _infile.readlines()
        self.set_size()
        self.set_s_t()
        self.make_maze()
        for i in range(self.maze_row):
            for j in range(self.maze_col):
                item = self.data_list[j * self.maze_row + i + 1]
                self.maze_map[i][j].setter(bool(int(item[0])), bool(int(item[2])),
                                           bool(int(item[4])), bool(int(item[6])))

    def make_maze(self):
        for x in range(self.maze_row):
            cells = []
            for y in range(self.maze_col):
                cells.append(Cell.Cell(Point(x, y)))
            self.maze_map.append(cells)
