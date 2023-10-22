import tkinter as tk
from tkinter import ttk, Canvas, messagebox, Text


class App:
    def __init__(self, root, bresenham_circle_algorithm, midpoint_circle_algorithm):
        self.root = root
        self.root.title("Circle Drawing Algorithms")

        self.bresenham_circle_algorithm = bresenham_circle_algorithm
        self.midpoint_circle_algorithm = midpoint_circle_algorithm

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.canvas = None
        self.log = None
        self.entries = {}

        bresenham_btn = ttk.Button(self.frame, text="Bresenham's Circle Algorithm",
                                   command=lambda: self.on_algorithm_selected("bresenham"))
        bresenham_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        midpoint_btn = ttk.Button(self.frame, text="Mid-Point Circle Algorithm",
                                  command=lambda: self.on_algorithm_selected("midpoint"))
        midpoint_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    def on_algorithm_selected(self, algo_name):
        self.algorithm = algo_name

        # Clear previous widgets
        if self.canvas:
            self.canvas.destroy()
        for entry in self.entries.values():
            entry.destroy()

        # Input points
        labels = ["centerX", "centerY", "radius"]
        for i, label in enumerate(labels):
            ttk.Label(self.frame, text=label).grid(
                row=i + 1, column=0, sticky="w")
            entry = ttk.Entry(self.frame, width=20)
            entry.grid(row=i + 1, column=1, padx=5, pady=2)
            self.entries[label] = entry

        # Submit Button
        ttk.Button(self.frame, text="Draw Circle", command=self.draw_circle).grid(
            row=4, column=0, columnspan=2, pady=5)

        # Canvas for drawing
        self.canvas = Canvas(self.frame, width=400, height=400,
                             bg="#d3d3d3", bd=3, relief="ridge")
        self.canvas.grid(row=5, column=0, columnspan=2, pady=10)

        # Log Text Area
        self.log = Text(self.frame, width=100, height=10)
        self.log.grid(row=6, column=0, columnspan=2, pady=10)

    def validate_inputs(self):
        for label, entry in self.entries.items():
            try:
                int(entry.get())
            except ValueError:
                messagebox.showerror("Error", f"Invalid input for {label}")
                return False
        return True

    def draw_circle(self):
        if not self.validate_inputs():
            return

        self.canvas.delete("all")

        x_center = int(self.entries["centerX"].get())
        y_center = int(self.entries["centerY"].get())
        radius = int(self.entries["radius"].get())

        if self.algorithm == "bresenham":
            points, logs = self.bresenham_circle_algorithm(
                x_center, y_center, radius)
        elif self.algorithm == "midpoint":
            points, logs = self.midpoint_circle_algorithm(
                x_center, y_center, radius)

        # Draw points on canvas
        for (x, y) in points:
            self.canvas.create_oval(x, y, x + 1, y + 1, fill='black')

        # Display logs in the log text area
        for log in logs:
            self.log.insert(tk.END, log + "\n")
