from drawable import Drawable
import pygame
from math import sqrt
from universe import Universe
from observable import Observable
from moveable import Moveable
from trailable import Trailable


class Celestial(Drawable, Observable, Moveable, Trailable):
    def __init__(self, pos, radius, mass, color, velocity=None):
        Drawable.__init__(self, pos=pos, size=(radius, radius), color=color)
        Moveable.__init__(self, pos=pos, velocity=velocity)
        Trailable.__init__(self, color=color, max_size=16, refresh_rate=20)
        Observable.__init__(self)
        self.mass = mass
        self.radius = radius

    def gravity(self, other):
        # F = G * m1 * m2 / r^2 => a = G * m1 / r^2
        "return the gravitational acceleration of the other planet as a vector"

        x1, y1 = self.pos
        x2, y2 = other.pos

        dx, dy = x2 - x1, y2 - y1

        distance = sqrt(dx * dx + dy * dy)
        if distance < self.radius + other.radius:
            return 0, 0

        dx, dy = dx / distance, dy / distance

        constant = Universe.G * self.mass / (distance * distance)

        return - dx * constant, - dy * constant

    def perfect_velocity(self, planet):
        x1, y1 = self.pos
        x2, y2 = planet.pos
        dx, dy = x1 - x2, y1 - y2
        distance = sqrt(dx * dx + dy * dy)
        dx, dy = dx / distance, dy / distance

        constant = sqrt(Universe.G * self.mass / distance)

        # 183905029
        return - dy * constant, dx * constant

    def update_trail(self):
        if self.screen_pos is not None:
            self.trail.add_point(self.screen_pos)

    def draw_trail(self, win):
        self.trail.draw(win)

    def add_orbiter(self, planet):
        self.add_observer(planet)

    def notify(self, dt):
        for observer in self.observers:
            observer.accelerate(acceleration=self.gravity(observer), dt=dt)

    def update(self, dt):
        self.move(dt)
        self.notify(dt)
        """if self.screen_pos is not None:
            self.trail.add_point(self.screen_pos)"""

    def remove_planet(self, planet):
        self.remove_observer(planet)

    def __lt__(self, other):
        return 0

    def __gt__(self, other):
        return 0
