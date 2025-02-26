from classes.line import Line
from classes.point import Point

class Cell():
  def __init__(self, win, colour="black"):
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self._x1 = None
    self._x2 = None
    self._y1 = None
    self._y2 = None
    self.center = None
    self._win = win
    self.colour = colour

  def draw(self, x1=None, y1=None, x2=None, y2=None, colour="black"):
    self._x1 = (x1 if x1 else self._x1)
    self._x2 = (x2 if x2 else self._x2)
    self._y1 = (y1 if y1 else self._y1)
    self._y2 = (y2 if y2 else self._y2)
    self.colour = colour
    center_x = min(self._x1, self._x2) + ((max(self._x1, self._x2) - min(self._x1, self._x2)) / 2)
    center_y = min(self._y1, self._y2) + ((max(self._y1, self._y2) - min(self._y1, self._y2)) / 2)
    self.center = Point(center_x, center_y)

    left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
    self._win.draw_line(left_wall, self.colour if self.has_left_wall else "white")

    right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
    self._win.draw_line(right_wall, self.colour if self.has_right_wall else "white")

    top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
    self._win.draw_line(top_wall, self.colour if self.has_top_wall else "white")

    bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
    self._win.draw_line(bottom_wall, self.colour if self.has_bottom_wall else "white")

  def draw_move(self, to_cell, undo=False):
    line_colour = "grey"
    if(undo):
      line_colour = "red"
    if(self.center and to_cell.center):
      self._win.draw_line(Line(self.center, to_cell.center), line_colour)
    else: 
      raise Exception(f"CELL CENTER IS NOT DEFINED self={self.center} to_cell={to_cell.center}")
    
  def __repr__(self):
    return f"(x1={self._x1} y1={self._y1} x2={self._x2} y2={self._y2})"