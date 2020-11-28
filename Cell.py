class Cell:
    """A cell in the maze.

    A maze "Cell" is a point in the grid which may be surrounded by walls to
    the north, east, south or west.

    """

    def __init__(self, point, n: bool = True, e: bool = True, s: bool = True, w: bool = True):
        """Initialize the cell at (x,y). At first it is surrounded by walls."""

        self.n, self.e, self.s, self.w = n, e, s, w
        self.visited: bool = False
        self.pos = point
        self.cost = 0
        self.parent = None

    def setter(self, n: bool = True, e: bool = True, s: bool = True, w: bool = True):
        self.n = n
        self.e = e
        self.s = s
        self.w = w
