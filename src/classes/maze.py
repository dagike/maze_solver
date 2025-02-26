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
      win
    ):
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_size_x = cell_size_x
    self.cell_size_y = cell_size_y
    self.win = win
    self._create_cells()

  def _create_cells(self):
    self._cells = [ [ Cell(self.win) for x in range(self.num_rows) ] for y in range(self.num_cols) ] 
    self._draw_cells()


  def _draw_cells(self):
    for x in range(self.num_rows):
      for y in range(self.num_cols):
        x1 = self.x1 + (self.cell_size_x * x)
        y1 = self.y1 + (self.cell_size_y * y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[x][y].draw(x1, y1, x2, y2)
        print(f"{x}, {y} = {self._cells[x][y]}")
        self._animate()

  def _animate(self):
    self.win.redraw()
    time.sleep(0.005)