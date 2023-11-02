def liang_barsky_algorithm(x1, y1, x2, y2, clip_xmin, clip_ymin, clip_xmax, clip_ymax):
    logs = []
    p = [-1 * (x2 - x1), x2 - x1, -1 * (y2 - y1), y2 - y1]
    q = [x1 - clip_xmin, clip_xmax - x1, y1 - clip_ymin, clip_ymax - y1]
    u1 = 0.0
    u2 = 1.0

    for i in range(4):
        if p[i] == 0:
            logs.append(f"Line is parallel to one of the clipping boundary")
            if q[i] < 0:
                return None, logs  # Line is outside and parallel to the clipping edge
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, t)
                logs.append(
                    f"Intersection at outside to inside for boundary {i+1}: u1 = {u1}")
            else:
                u2 = min(u2, t)
                logs.append(
                    f"Intersection at inside to outside for boundary {i+1}: u2 = {u2}")
            if u1 > u2:
                return None, logs  # Line is outside

    logs.append(f"Line is partially inside with u1 = {u1} and u2 = {u2}")
    clipped_line = (
        x1 + u1 * (x2 - x1),
        y1 + u1 * (y2 - y1),
        x1 + u2 * (x2 - x1),
        y1 + u2 * (y2 - y1)
    )

    return clipped_line, logs
