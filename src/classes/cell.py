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

  def draw(self, x1, y1, x2, y2, colour="black"):
    self._x1 = x1
    self._x2 = x2
    self._y1 = y1
    self._y2 = y2
    self.colour = colour
    center_x = min(x1, x2) + ((max(x1, x2) - min(x1, x2)) / 2)
    center_y = min(y1, y2) + ((max(y1, y2) - min(y1, y2)) / 2)
    self.center = Point(center_x, center_y)

    if(self.has_left_wall):
      left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
      self._win.draw_line(left_wall, self.colour)

    if(self.has_right_wall):
      right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
      self._win.draw_line(right_wall, self.colour)

    if(self.has_top_wall):
      top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
      self._win.draw_line(top_wall, self.colour)

    if(self.has_bottom_wall):
      bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
      self._win.draw_line(bottom_wall, self.colour)

  def draw_move(self, to_cell, undo=False):
    line_colour = "grey"
    if(undo):
      line_colour = "red"
    if(self.center and to_cell.center):
      self._win.draw_line(Line(self.center, to_cell.center), line_colour)
    else: 
      raise Exception(f"CELL CENTER IS NOT DEFINED self={self.center} to_cell={to_cell.center}")