import tkinter as tk
from tkinter import ttk, Canvas, messagebox


class App:
    def __init__(self, root, dda_algorithm, bresenham_algorithm):
        self.root = root
        self.root.title("LIT2021012 Line Drawing")

        self.dda_algorithm = dda_algorithm
        self.bresenham_algorithm = bresenham_algorithm

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.canvas = None
        self.log = None
        self.entries = {}

        dda_btn = ttk.Button(self.frame, text="DDA Algorithm",
                             command=lambda: self.on_algorithm_selected("dda"))
        dda_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        bresenham_btn = ttk.Button(self.frame, text="Bresenham's Algorithm",
                                   command=lambda: self.on_algorithm_selected("bresenham"))
        bresenham_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    def on_algorithm_selected(self, algo_name):
        self.algorithm = algo_name

        # Clear previous widgets
        if self.canvas:
            self.canvas.destroy()
        for entry in self.entries.values():
            entry.destroy()

        # Input points
        labels = ["startX", "startY", "endX", "endY"]
        for i, label in enumerate(labels):
            ttk.Label(self.frame, text=label).grid(row=i + 1, column=0, sticky="w")
            entry = ttk.Entry(self.frame, width=20)
            entry.grid(row=i + 1, column=1, padx=5, pady=2)
            self.entries[label] = entry

        # Submit Button
        ttk.Button(self.frame, text="Submit", command=self.plot_line).grid(
            row=5, column=0, columnspan=2, pady=5)

        # Canvas for drawing
        self.canvas = Canvas(self.frame, width=300, height=300, bg="#d3d3d3", bd=3, relief="ridge")
        self.canvas.grid(row=6, column=0, columnspan=2, pady=10)

        # Log for displaying calculations
        self.log = ttk.Label(self.frame, text="", wraplength=250, foreground="blue")
        self.log.grid(row=7, column=0, columnspan=2)
    
    def append_to_log(self, message):
        current_log = self.log["text"]
        self.log["text"] = current_log + "> " + message + "\n"

    def validate_inputs(self):
        for label, entry in self.entries.items():
            try:
                int(entry.get())
            except ValueError:
                messagebox.showerror("Error", f"Invalid input for {label}")
                return False
        return True

    def plot_line(self):
        if not self.validate_inputs():
            return

        self.canvas.delete("all")
        self.log["text"] = ""

        x1, y1 = int(self.entries["startX"].get()), int(
            self.entries["startY"].get())
        x2, y2 = int(self.entries["endX"].get()), int(
            self.entries["endY"].get())

        if self.algorithm == "dda":
            points, logs = self.dda_algorithm(x1, y1, x2, y2)
            for log in logs:
                self.append_to_log(log)
            self.append_to_log(f"Slope: {(y2-y1)/(x2-x1) if x2 != x1 else 'Infinity'}")
            self.log.config(foreground="green")

        elif self.algorithm == "bresenham":
            points, logs = self.bresenham_algorithm(x1, y1, x2, y2)
            for log in logs:
                self.append_to_log(log)
            self.log.config(foreground="red")
        
        # Draw points on canvas
        print(points)
        for (x, y) in points:
            self.canvas.create_oval(x*5, y*5, x*5 + 5, y*5 + 5, fill='black')
