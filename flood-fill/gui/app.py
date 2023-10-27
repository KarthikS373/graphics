import tkinter as tk
from tkinter import ttk, messagebox


class App:
    def __init__(self, root, flood_fill_4_connected, flood_fill_8_connected):
        self.root = root
        self.flood_fill_4_connected = flood_fill_4_connected
        self.flood_fill_8_connected = flood_fill_8_connected

        self.root.title("Flood Fill Algorithm")

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.canvas = tk.Canvas(self.frame, width=400, height=400, bg="white")
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        self.canvas.bind('<Button-1>', self.on_canvas_click)

        self.log = tk.Text(self.frame, width=50, height=20)
        self.log.grid(row=0, column=1, padx=10, pady=10)

        self.connected_var = tk.StringVar()
        self.connected_var.set("4")

        ttk.Radiobutton(self.frame, text="4-connected", variable=self.connected_var,
                        value="4").grid(row=1, column=0, sticky="w")
        ttk.Radiobutton(self.frame, text="8-connected", variable=self.connected_var,
                        value="8").grid(row=2, column=0, sticky="w")

        ttk.Button(self.frame, text="Clear", command=self.clear_canvas).grid(
            row=3, column=0, columnspan=2, pady=5)

    def on_canvas_click(self, event):
        x, y = event.x, event.y
        connected_type = self.connected_var.get()

        self.clear_canvas()

        min_x = max(0, x - 100)
        max_x = min(self.canvas.winfo_width(), x + 100)
        min_y = max(0, y - 100)
        max_y = min(self.canvas.winfo_height(), y + 100)

        logs = []
        if connected_type == "4":
            logs = self.flood_fill_4_connected(x, y, self.canvas, min_x, min_y, max_x, max_y)

        elif connected_type == "8":
            logs = self.flood_fill_8_connected(x, y, self.canvas, min_x, min_y, max_x, max_y)

        for log in logs:
            self.log.insert(tk.END, log)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.log.delete(1.0, tk.END)
