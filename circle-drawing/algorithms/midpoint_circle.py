def midpoint_circle_algorithm(x_center, y_center, radius):
    x = radius
    y = 0
    points = []
    logs = []

    logs.append(f"Midpoint circle algorithm")
    logs.append(f"Initial point: ({x_center + x}, {y_center - y})")

    # The initial point on the circle at the end of the radius
    points.append((x_center + x, y_center - y))
    logs.append(f"Step 0: x = {x}, y = {y}, P = 1 - {radius} = {1 - radius}")

    P = 1 - radius  # The parameter value for the initial point

    while x > y:
        y += 1
        logs.append(f"Step {y}: x = {x}, y = {y}, P = {P}")

        if P <= 0:
            P = P + (2 * y + 1)
            logs.append(
                f"    P is less than or equal to 0: P = {P} + 2 * {y} + 1 = {P + (2 * y + 1)}")
        else:
            x -= 1
            P = P + (2 * y - 2 * x + 1)
            logs.append(
                f"    P is greater than 0: P = {P} + 2 * {y} - 2 * {x} + 1 = {P + (2 * y - 2 * x + 1)}")

        if x < y:
            break

        # Printing the generated point and its reflection in the other octants
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
