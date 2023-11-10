import tkinter as tk
from gui.app import App
from algorithms.nln import nln_algorithm

root = tk.Tk()
app = App(root, nln_algorithm)
root.mainloop()
