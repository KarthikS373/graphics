def flood_fill_4_connected(x, y, canvas,  min_x=0, min_y=0, max_x=None, max_y=None):
    color = "red"
    logs = []

    max_x = max_x if max_x else canvas.winfo_width()
    max_y = max_y if max_y else canvas.winfo_height()

    if canvas.find_overlapping(x, y, x, y):
        return

    coords_to_fill = [(x, y)]
    filled_coords = set()

    while coords_to_fill:
        x, y = coords_to_fill.pop()

        if (x, y) in filled_coords or x < min_x or x >= max_x or y < min_y or y >= max_y:
            continue

        print(x, y)

        canvas.create_rectangle(x, y, x+1, y+1, outline=color, fill=color)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if canvas.find_overlapping(new_x, new_y, new_x, new_y):
                continue
            coords_to_fill.append((new_x, new_y))

        filled_coords.add((x, y))
        logs.append(f"Filling 4-connected: ({x}, {y})\n")

    return logs
