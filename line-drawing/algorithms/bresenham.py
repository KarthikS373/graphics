def bresenham_algorithm(x1, y1, x2, y2):
    points = []
    logs = []

    points.append((x1, y1))

    slope = 2 * (y2 - y1)
    d = slope - (x2 - x1)

    logs.append(f"Slope = {slope}")

    y = y1
    for x in range(x1, x2+1):

        points.append((x, y))
        d = d + slope

        if (d >= 0):
            y = y+1
            d = d - 2 * (x2 - x1)

        logs.append(f"Chosen Point ({x}, {y}), decision parameter = {d}")

    return points, logs
