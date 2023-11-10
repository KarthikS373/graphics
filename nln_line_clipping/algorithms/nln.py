def nln_algorithm(x1, y1, x2, y2, clip_xmin, clip_ymin, clip_xmax, clip_ymax):
    logs = []
    dx = x2 - x1
    dy = y2 - y1
    p = [-dx, dx, -dy, dy]
    q = [x1 - clip_xmin, clip_xmax - x1, y1 - clip_ymin, clip_ymax - y1]
    u1 = 0.0
    u2 = 1.0

    for i in range(4):
        if p[i] == 0:
            logs.append(f"Line is parallel to clipping boundary {i+1}")
            if q[i] < 0:
                logs.append("Line is completely outside")
                return None, logs
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, t)
                logs.append(f"Updating u1 for boundary {i+1}: u1 = {u1}")
            else:
                u2 = min(u2, t)
                logs.append(f"Updating u2 for boundary {i+1}: u2 = {u2}")
            if u1 > u2:
                logs.append("Line is completely outside")
                return None, logs

    clipped_line = (
        x1 + u1 * dx,
        y1 + u1 * dy,
        x1 + u2 * dx,
        y1 + u2 * dy
    )
    logs.append(f"Clipped line coordinates: {clipped_line}")

    return clipped_line, logs
