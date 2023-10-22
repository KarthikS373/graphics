import tkinter as tk
from gui.app import App
from algorithms.bresenham import bresenham_circle_algorithm
from algorithms.midpoint_circle import midpoint_circle_algorithm

root = tk.Tk()
app = App(root, bresenham_circle_algorithm, midpoint_circle_algorithm)
root.mainloop()
