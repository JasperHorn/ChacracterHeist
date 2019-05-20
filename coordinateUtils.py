
def filledManhattanCircle(radius):
    for distance in range(1, radius + 1):
        for coordinate in manhattanCirle(distance):
            yield coordinate

def manhattanCirle(radius):
    for n in range(0, radius * 4):
        # Start (0, -r) instead of (r, 0)
        n = (n - radius) % (radius * 4)

        if n <= radius * 2:
            x = radius - n
            y = radius - abs(x)
        else:
            x = -3 * radius + n
            y = -radius + abs(x)
        yield (x, y)
