import tkinter as tk

from gui.app import App
from algorithms.liang_barsky import liang_barsky_algorithm

root = tk.Tk()
app = App(root, liang_barsky_algorithm)
root.mainloop()
