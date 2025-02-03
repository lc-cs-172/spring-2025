import graphics as g

def main():
    # Create a graphics window
    width = 400
    height = 400
    win = g.GraphWin("Bouncing Ball", width, height)

    x = 50.0
    y = 50.0
    dx = 1.0
    dy = 0.5
    radius = 10.0

    c = g.Circle(g.Point(x, y), radius)
    c.draw(win)

    while win.checkMouse() is None:
        if (x >= width - radius) or (x <= radius):
            dx = -dx
        if (y >= height - radius) or (y <= radius):
            dy = -dy
        x += dx
        y += dy
        c.move(dx, dy)

    # Wait until the user click in the window
    win.close()

if __name__ == '__main__':
    main()
