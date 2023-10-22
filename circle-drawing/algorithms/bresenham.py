def bresenham_circle_algorithm(x_center, y_center, radius):
    x = radius
    y = 0
    points = []
    logs = []
    P = 3 - (radius << 1)

    logs.append(f"Bresenham's Circle Drawing Algorithm")
    logs.append(f"Initial point: ({x_center + x}, {y_center - y})")

    # Printing the initial point on the circle at the end of radius
    points.append((x_center + x, y_center - y))
    logs.append(
        f"Step 0: x = {x}, y = {y}, P = 3 - 2 * {radius} = {3 - (radius << 1)}")

    # When radius is zero, only a single point is printed at center
    if radius > 0:
        points.append((x_center - x, y_center - y))
        logs.append(
            f"Step 1: x = {x}, y = {y}, P = 3 - 2 * {radius} = {3 - (radius << 1)}")
        points.append((x_center + y, y_center + x))
        logs.append(f"Step 2: x = {y}, y = {x}, P = {P} (unchanged)")
        points.append((x_center - y, y_center + x))
        logs.append(f"Step 3: x = {y}, y = {x}, P = {P} (unchanged)")

    # Initial point on the circle at the end of radius
    while y <= x:
        y += 1
        logs.append(f"Step {y + 3}: x = {x}, y = {y}, P = {P}")

        # Mid-point is inside or on the perimeter of the circle
        if P <= 0:
            P += (y << 1) + 1
            logs.append(
                f"    P is less than or equal to 0: P = {P} + (2 * {y} + 1) = {P + (y << 1) + 1}")
        else:
            x -= 1
            P += ((y - x + 1) << 1)
            logs.append(
                f"    P is greater than 0: P = {P} + (2 * {y} - 2 * {x} + 2) = {P + ((y - x + 1) << 1)}")

        if x < y:
            break

        # Printing generated point and its reflection in the other octants
        points.append((x_center + x, y_center - y))
        logs.append(f"    Point ({x_center + x}, {y_center - y}) added")
        points.append((x_center - x, y_center - y))
        logs.append(f"    Point ({x_center - x}, {y_center - y}) added")
        points.append((x_center + x, y_center + y))
        logs.append(f"    Point ({x_center + x}, {y_center + y}) added")
        points.append((x_center - x, y_center + y))
        logs.append(f"    Point ({x_center - x}, {y_center + y}) added")

        # If the generated point is on the line x=Y, then the perimeter points
        # have only a set of symmetric points
        if x != y:
            points.append((x_center + y, y_center - x))
            logs.append(f"    Point ({x_center + y}, {y_center - x}) added")
            points.append((x_center - y, y_center - x))
            logs.append(f"    Point ({x_center - y}, {y_center - x}) added")
            points.append((x_center + y, y_center + x))
            logs.append(f"    Point ({x_center + y}, {y_center + x}) added")
            points.append((x_center - y, y_center + x))
            logs.append(f"    Point ({x_center - y}, {y_center + x}) added")

    return points, logs
