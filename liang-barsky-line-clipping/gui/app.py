import tkinter as tk
from tkinter import ttk, Canvas, messagebox


class App:
    def __init__(self, root, liang_barsky_algorithm):
        self.root = root
        self.root.title("Line Clipping with Liang-Barsky Algorithm")

        self.liang_barsky_algorithm = liang_barsky_algorithm

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.canvas = None
        self.log = None
        self.entries = {}

        liang_barsky_btn = ttk.Button(self.frame, text="Liang-Barsky Algorithm",
                                      command=self.on_algorithm_selected)
        liang_barsky_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    def on_algorithm_selected(self):
        # Clear previous widgets
        if self.canvas:
            self.canvas.destroy()
        for entry in self.entries.values():
            entry.destroy()

        # Input for line endpoints and clipping window
        labels = ["startX", "startY", "endX", "endY",
                  "clipXmin", "clipYmin", "clipXmax", "clipYmax"]
        for i, label in enumerate(labels):
            ttk.Label(self.frame, text=label).grid(
                row=i + 1, column=0, sticky="w")
            entry = ttk.Entry(self.frame, width=20)
            entry.grid(row=i + 1, column=1, padx=5, pady=2)
            self.entries[label] = entry

        # Submit Button
        ttk.Button(self.frame, text="Clip Line", command=self.clip_line).grid(
            row=9, column=0, columnspan=2, pady=5)

        # Canvas for drawing
        self.canvas = Canvas(self.frame, width=400, height=400,
                             bg="#d3d3d3", bd=3, relief="ridge")
        self.canvas.grid(row=10, column=0, columnspan=2, pady=10)

        # Log for displaying calculations
        self.log = ttk.Label(self.frame, text="",
                             wraplength=350, foreground="blue")
        self.log.grid(row=11, column=0, columnspan=2)

    def append_to_log(self, message):
        current_log = self.log["text"]
        self.log["text"] = current_log + "> " + message + "\n"

    def validate_inputs(self):
        for label, entry in self.entries.items():
            try:
                float(entry.get())
            except ValueError:
                messagebox.showerror("Error", f"Invalid input for {label}")
                return False
        return True

    def clip_line(self):
        if not self.validate_inputs():
            return

        self.canvas.delete("all")
        self.log["text"] = ""

        x1, y1 = float(self.entries["startX"].get()), float(
            self.entries["startY"].get())
        x2, y2 = float(self.entries["endX"].get()), float(
            self.entries["endY"].get())
        clip_xmin, clip_ymin = float(self.entries["clipXmin"].get()), float(
            self.entries["clipYmin"].get())
        clip_xmax, clip_ymax = float(self.entries["clipXmax"].get()), float(
            self.entries["clipYmax"].get())

        clipped_line, logs = self.liang_barsky_algorithm(
            x1, y1, x2, y2, clip_xmin, clip_ymin, clip_xmax, clip_ymax)
        for log in logs:
            self.append_to_log(log)

        # Draw the clipping window
        self.canvas.create_rectangle(
            clip_xmin, clip_ymin, clip_xmax, clip_ymax, outline='blue')

        # Draw the original line
        self.canvas.create_line(x1, y1, x2, y2, fill='red', dash=(4, 2))

        # Draw the clipped line
        if clipped_line:
            self.canvas.create_line(
                clipped_line[0], clipped_line[1], clipped_line[2], clipped_line[3], fill='green')
