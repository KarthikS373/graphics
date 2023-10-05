import tkinter as tk

from gui.app import App
from algorithms.dda import dda_algorithm
from algorithms.bresenham import bresenham_algorithm

root = tk.Tk()
app = App(root, dda_algorithm, bresenham_algorithm)
root.mainloop()
