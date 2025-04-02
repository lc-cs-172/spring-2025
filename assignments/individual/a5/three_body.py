"""Approximate trajectories of three identical bodies located at the vertices of
a scalene triangle and having zero initial velocities.."""

__author__ = 'Alain Kägi'

from body import Body, new_position
import graphics as g
from vector import Vector

MASS = 1.0                                  # kg

DT = 3600.0                                 # s

SCALE = 10

def main():
    win = g.GraphWin("Three-Body Problem", 1000, 1000, autoflush = False)
    win.setCoords(-SCALE, -SCALE, +SCALE, +SCALE)

    config = 4
    if config == 1:
        body1 = Body(MASS, Vector(-0.1,  0.0), Vector(0.0, 0.0))
        body2 = Body(MASS, Vector( 3.4,  0.0), Vector(0.0, 0.0))
        body3 = Body(MASS, Vector( 0.0,  2.7), Vector(0.0, 0.0))
    elif config == 2:
        body1 = Body(MASS, Vector( 0.0,  0.0), Vector(0.0, 0.0))
        body2 = Body(MASS, Vector( 3.8,  0.0), Vector(0.0, 0.0))
        body3 = Body(MASS, Vector( 0.0,  3.0), Vector(0.0, 0.0))
    elif config == 3:
        body1 = Body(MASS, Vector(-0.3,  0.0), Vector(0.0, 0.0))
        body2 = Body(MASS, Vector( 2.2,  0.0), Vector(0.0, 0.0))
        body3 = Body(MASS, Vector( 0.0,  2.4), Vector(0.0, 0.0))
    else:
        body1 = Body(MASS, Vector( 5.0,  0.0), Vector(0.0, 0.0))
        body2 = Body(MASS, Vector( 0.0,  0.9), Vector(0.0, 0.0))
        body3 = Body(MASS, Vector( 6.6,  5.95), Vector(0.0, 0.0))

    bodies = [body1, body2, body3]

    while True:
        orb1 = g.Circle(g.Point(body1.pos().get_x(), body1.pos().get_y()), .1)
        orb1.setFill('black')
        orb1.draw(win)
        orb2 = g.Circle(g.Point(body2.pos().get_x(), body2.pos().get_y()), .1)
        orb2.setFill('black')
        orb2.draw(win)
        orb3 = g.Circle(g.Point(body3.pos().get_x(), body3.pos().get_y()), .1)
        orb3.setFill('black')
        orb3.draw(win)

        line1 = g.Line(g.Point(body1.pos().get_x(), body1.pos().get_y()),
                       g.Point(body2.pos().get_x(), body2.pos().get_y()))
        line1.draw(win)
        line2 = g.Line(g.Point(body2.pos().get_x(), body2.pos().get_y()),
                       g.Point(body3.pos().get_x(), body3.pos().get_y()))
        line2.draw(win)
        line3 = g.Line(g.Point(body3.pos().get_x(), body3.pos().get_y()),
                       g.Point(body1.pos().get_x(), body1.pos().get_y()))
        line3.draw(win)
        half1 = g.Line(g.Point(body1.pos().get_x(), body1.pos().get_y()),
                       g.Point((body2.pos().get_x() + body3.pos().get_x())/2,
                               (body2.pos().get_y() + body3.pos().get_y())/2))
        half1.draw(win)
        half2 = g.Line(g.Point(body2.pos().get_x(), body2.pos().get_y()),
                       g.Point((body1.pos().get_x() + body3.pos().get_x())/2,
                               (body1.pos().get_y() + body3.pos().get_y())/2))
        half2.draw(win)
        half3 = g.Line(g.Point(body3.pos().get_x(), body3.pos().get_y()),
                       g.Point((body1.pos().get_x() + body2.pos().get_x())/2,
                               (body1.pos().get_y() + body2.pos().get_y())/2))
        half3.draw(win)

        trace = g.Circle(g.Point(body1.pos().get_x(), body1.pos().get_y()), .025)
        trace.setOutline('red')
        trace.setFill('red')
        trace.draw(win)
        trace = g.Circle(g.Point(body2.pos().get_x(), body2.pos().get_y()), .025)
        trace.setOutline('blue')
        trace.setFill('blue')
        trace.draw(win)
        trace = g.Circle(g.Point(body3.pos().get_x(), body3.pos().get_y()), .025)
        trace.setOutline('green')
        trace.setFill('green')
        trace.draw(win)

        g.update()

        new_position(bodies, DT)

        orb1.undraw()
        orb2.undraw()
        orb3.undraw()
        line1.undraw()
        line2.undraw()
        line3.undraw()
        half1.undraw()
        half2.undraw()
        half3.undraw()

if __name__ == '__main__':
    main()
