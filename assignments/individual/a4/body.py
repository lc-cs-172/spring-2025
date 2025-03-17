"""Two-dimensional simulation of gravitational forces acting on a particular
body."""

import math

# Gravitational constant
G = 6.6743e-11  # N⋅m^2/kg^2

class Body:
    def __init__(self, mass : float, p0 : tuple[float, float], v0 : tuple[float, float]):
        """Create a new body of given mass in kg, given position in (m, m),
        and given velocity in (m/s, m/s)."""
        self.mass = mass
        self.p = p0
        self.v = v0

    def force_with(self, other):
        """Return the force in (N, N) exerted by the other body on this body."""
        dx = self.p[0] - other.p[0]
        dy = self.p[1] - other.p[1]
        r2 = dx**2 + dy**2
        r = math.sqrt(r2)
        m1 = self.mass
        m2 = other.mass
        f = G*m1*m2/r2
        return (-f/r*dx, -f/r*dy)

    def force_with_all(self, others):
        """Return the force in (N, N) exerted by all the other bodies on this
        body."""
        f = (0.0, 0.0)
        for b in others:
            fp = self.force_with(b)
            f = (f[0] + fp[0], f[1] + fp[1])
        return f

    def update_position(self, f : tuple[float, float], dt : float):
        """Update the position of this body based on the total force (fx, fy)
        imparted on it and assuming `dt` seconds have elpased."""
        a = (f[0]/self.mass, f[1]/self.mass)
        dv = (a[0]*dt, a[1]*dt)
        self.v = (self.v[0] + dv[0], self.v[1] + dv[1])
        dx = (self.v[0]*dt, self.v[1]*dt)
        self.p = (self.p[0] + dx[0], self.p[1] + dx[1])

    def pos(self):
        """Return the position in (m, m) of this body."""
        return self.p

    def __str__(self):
        """Return a string describing this body."""
        s = str(self.mass) + ' at <'
        s += str(self.p[0]) + ', ' + str(self.p[1]) + '> velocity <'
        s += str(self.v[0]) + ', ' + str(self.v[1]) + '>'
        return s

def new_position(bodies : list[Body], dt : float):
    """Compute the new position of all bodies in our system."""
    forces = []
    for i in range(len(bodies)):
        others = bodies[:]
        others.pop(i)
        forces.append(bodies[i].force_with_all(others))
    for i in range(len(bodies)):
        bodies[i].update_position(forces[i], dt)

def main():
    # A simple test case based on information found below.
    # https://qsstudy.com/gravitational-force-sun-earth/
    # https://en.wikipedia.org/wiki/Orbital_speed
    sun = Body(1.99e30, (0.0, 0.0), (0.0, 0.0))
    earth = Body(5.96e24, (1.497e11, 0.0), (0.0, 29800.0))
    print(earth)
    print(earth.force_with(sun))

if __name__ == '__main__':
    main()
