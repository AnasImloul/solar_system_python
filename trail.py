from collections import deque
from drawable import Drawable
import pygame
from time import time
from universe import Universe
from math import sqrt


def distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    dx, dy = x2 - x1, y2 - y1
    return sqrt(dx * dx + dy * dy)


class Trail(Drawable):
    def __init__(self, object, color, max_size, refresh_rate=10):
        super().__init__(pos=(0, 0), size=(0, 0), color=color)
        self.color = color
        self.object = object
        self.max_size = max_size
        self.refresh_rate = refresh_rate
        self.points = deque(maxlen=max_size)
        self.last_update = None

    def add_point(self, point):
        """
        Add a point to the trail.
        if the trail is full, remove the oldest point.
        if the trail length is greater than max_length, remove the oldest point. and subtract the length of the removed point.
        if the trail length is less than max_length, add the length of the new point. and add the length of the new point.
        """

        if self.last_update is not None:
            if time() - self.last_update < 1 / self.refresh_rate:
                return

        if len(self.points) == self.max_size:
            if len(self.points) > 1:
                self.points.popleft()

        self.points.append(point)
        self.last_update = time()

    def draw(self, win):
        """Draw the trail."""
        if self.object.screen_pos is None:
            return

        background = Universe.color

        if len(self.points) > 0:
            color = (
                self.color[0] + background[0] // 2,
                self.color[1] + background[1] // 2,
                self.color[2] + background[2] // 2,
            )
            pygame.draw.line(win, color, self.object.screen_pos, self.points[-1], 2)

        for i in range(1, len(self.points)):
            # blend the color of the trail with the color of the planet near the planet.
            # blend the color of the trail with the color of the background away from the planet.

            alpha = (i + 1) / len(self.points)

            color = (int(self.color[0] * alpha + background[0] * (1 - alpha)),
                     int(self.color[1] * alpha + background[1] * (1 - alpha)),
                     int(self.color[2] * alpha + background[2] * (1 - alpha)))

            pygame.draw.line(win, color, self.points[i - 1], self.points[i], 2)

    def clear(self):
        """Clear the trail."""
        self.points.clear()

    def __lt__(self, other):
        return 0

    def __gt__(self, other):
        return 0
