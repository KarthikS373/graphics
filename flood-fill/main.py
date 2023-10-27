import tkinter as tk
from gui.app import App
from algorithms.ff_4_connected import flood_fill_4_connected
from algorithms.ff_8_connected import flood_fill_8_connected

root = tk.Tk()
app = App(root, flood_fill_4_connected, flood_fill_8_connected)
root.mainloop()
