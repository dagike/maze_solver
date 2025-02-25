from tkinter import Tk, BOTH, Canvas

class Window():
  def __init__(self, width, height):
    self.root_widget = Tk()
    self.root_widget.title = ""
    self.canvas_widget = Canvas(self.root_widget, width=width, height=height)
    self.canvas_widget.pack()
    self.isRunning = False
    self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

  def redraw(self):
    self.root_widget.update_idletasks()
    self.root_widget.update()

  def wait_for_close(self):
    self.isRunning = True
    while(self.isRunning):
      self.redraw()

  def close(self):
    self.isRunning = False