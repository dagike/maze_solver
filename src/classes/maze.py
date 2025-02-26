import random
import time
from classes.cell import Cell

class Maze():
  def __init__(
      self,
      x1,
      y1,
      num_rows,
      num_cols,
      cell_size_x,
      cell_size_y,
      win,
      seed=None
    ):
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_size_x = cell_size_x
    self.cell_size_y = cell_size_y
    self.win = win

    if seed:
      random.seed(seed)

    self._create_cells()
    self._break_entrance_and_exit()
    self._break_walls_r(0, 0)
    self._reset_cells_visited()


  def _create_cells(self):
    self._cells = [ [ Cell(self.win) for y in range(self.num_cols) ] for x in range(self.num_rows) ] 
    for x in range(self.num_rows):
      for y in range(self.num_cols):
        self._draw_cell(x, y)


  def _draw_cell(self, x, y):
    x1 = self.x1 + (self.cell_size_x * x)
    y1 = self.y1 + (self.cell_size_y * y)
    x2 = x1 + self.cell_size_x
    y2 = y1 + self.cell_size_y

    self._cells[x][y].draw(x1, y1, x2, y2)
    self._animate()

  def _animate(self):
    self.win.redraw()
    time.sleep(0.05)

  def _break_entrance_and_exit(self):
    self._cells[0][0].has_top_wall = False
    self._draw_cell(0, 0)
    
    self._cells[-1][-1].has_bottom_wall = False
    self._draw_cell(self.num_rows - 1, self.num_cols - 1)

  def _break_walls_r(self, x, y):
    self._cells[x][y].visited = True

    while True:
      next_cells = []

      # right of cell
      if x < self.num_rows - 1 and not self._cells[x + 1][y].visited:
        next_cells.append((x + 1, y))

      # left of cell
      if x > 0 and not self._cells[x - 1][y].visited:
        next_cells.append((x - 1, y))

      # top of cell
      if y > 0 and not self._cells[x][y - 1].visited:
        next_cells.append((x, y - 1))

      # bottom of cell
      if y < self.num_cols - 1 and not self._cells[x][y + 1].visited:
        next_cells.append((x, y + 1))

      if not next_cells:
        self._draw_cell(x, y)
        return

      next_cell_index = random.randrange(len(next_cells))
      next_cell = next_cells[next_cell_index]

      if next_cell[0] == x + 1:
        self._cells[x][y].has_right_wall = False
        self._cells[x + 1][y].has_left_wall = False

      if next_cell[0] == x - 1:
        self._cells[x][y].has_left_wall = False
        self._cells[x - 1][y].has_right_wall = False

      if next_cell[1] == y - 1:
        self._cells[x][y].has_top_wall = False
        self._cells[x][y - 1].has_bottom_wall = False

      if next_cell[1] == y + 1:
        self._cells[x][y].has_bottom_wall = False
        self._cells[x][y + 1].has_top_wall = False

      self._break_walls_r(next_cell[0], next_cell[1])

  def _reset_cells_visited(self):
    for x in range(self.num_rows):
      for y in range(self.num_cols):
        self._cells[x][y].visited = False

  def solve(self):
    self._solve_r(0, 0)

  def _solve_r(self, x, y):
    self._animate()

    self._cells[x][y].visited = True

    if(x == self.num_rows - 1 and y == self.num_cols - 1):
      return True
    
    # right of cell
    if x < self.num_rows - 1 and not self._cells[x][y].has_right_wall and not self._cells[x + 1][y].visited:
      self._cells[x][y].draw_move(self._cells[x + 1][y])
      solved = self._solve_r(x + 1, y)
      if solved:
        return True
      else:
        self._cells[x][y].draw_move(self._cells[x + 1][y], True)

    # left of cell
    if x > 0 and not self._cells[x][y].has_left_wall and not self._cells[x - 1][y].visited:
      self._cells[x][y].draw_move(self._cells[x - 1][y])
      solved = self._solve_r(x - 1, y)
      if solved:
        return True
      else:
        self._cells[x][y].draw_move(self._cells[x - 1][y], True)


    # top of cell
    if y > 0 and not self._cells[x][y].has_top_wall and not self._cells[x][y - 1].visited:
      self._cells[x][y].draw_move(self._cells[x][y - 1])
      solved = self._solve_r(x, y - 1)
      if solved:
        return True
      else:
        self._cells[x][y].draw_move(self._cells[x][y - 1], True)

    # bottom of cell
    if y < self.num_cols - 1 and not self._cells[x][y].has_bottom_wall and not self._cells[x][y + 1].visited:
      self._cells[x][y].draw_move(self._cells[x][y + 1])
      solved = self._solve_r(x, y + 1)
      if solved:
        return True
      else:
        self._cells[x][y].draw_move(self._cells[x][y + 1], True)
    
    return False