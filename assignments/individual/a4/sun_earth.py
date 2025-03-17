"""Simulate the orbit of Earth around the Sun."""

__author__ = 'Alain Kägi'

from body import Body, new_position
import graphics as g

SUN_MASS = 1.99e30                          # kg
EARTH_MASS = 5.96e24                        # kg
EARTH_AVERAGE_DISTANCE_FROM_SUN = 1.497e11  # m
EARTH_AVERAGE_ORBITAL_SPEED     = 2.9800e04 # m/s

DT = 3600.0                                 # s

DISPLAY_WIDTH = EARTH_AVERAGE_DISTANCE_FROM_SUN*1.1
SCALE = 1000000000

def main():
    win = g.GraphWin("Sun-Earth", 1000, 1000, autoflush = False)
    win.setCoords(-SCALE, -SCALE, +SCALE, +SCALE)

    sun = Body(SUN_MASS, (0.0, 0.0), (0.0, 0.0))
    earth = Body(EARTH_MASS,
                 (EARTH_AVERAGE_DISTANCE_FROM_SUN, 0.0),
                 (0.0, EARTH_AVERAGE_ORBITAL_SPEED))

    bodies = [sun, earth]

    while True:
        sunPos = sun.pos()
        sunCircle = g.Circle(g.Point(sunPos[0]/DISPLAY_WIDTH*SCALE,
                                     sunPos[0]/DISPLAY_WIDTH*SCALE), 10000000)
        sunCircle.setOutline('orange')
        sunCircle.setFill('orange')
        sunCircle.draw(win)

        earthPos = earth.pos()
        earthCircle = g.Circle(g.Point(earthPos[0]/DISPLAY_WIDTH*SCALE,
                                       earthPos[1]/DISPLAY_WIDTH*SCALE), 10)
        earthCircle.setOutline('blue')
        earthCircle.setFill('blue')
        earthCircle.draw(win)

        g.update()

        new_position(bodies, DT)

        sunCircle.undraw()
        earthCircle.undraw()

if __name__ == '__main__':
    main()
