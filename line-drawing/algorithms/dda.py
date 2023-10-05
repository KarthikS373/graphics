def dda_algorithm(x1, y1, x2, y2):
    points = []
    logs = []

    dx = x2 - x1
    dy = y2 - y1
    logs.append(f"dx = {dx}, dy = {dy}")
    logs.append(f"Slope = {(y2-y1)/(x2-x1) if x2 != x1 else 'Infinity'}")

    steps = max(abs(dx), abs(dy))
    logs.append(f"Steps = {steps}")

    Xinc = dx / float(steps)
    Yinc = dy / float(steps)
    logs.append(f"Xinc = {Xinc}")
    logs.append(f"Yinc = {Yinc}")

    x, y = x1, y1
    points.append((x, y))

    for _ in range(steps):
        x += Xinc
        y += Yinc
        points.append((round(x), round(y)))

    return points, logs
