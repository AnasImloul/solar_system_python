import pygame


class Drawable:
    def __init__(self, pos, size, color):
        self.pos = pos
        self.screen_pos = None
        self.size = size
        self.color = color

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    def draw(self, win, scale, offset):
        x, y = self.pos

        pos = (x * scale + offset[0], y * scale + offset[1])
        size = self.size
        self.screen_pos = pos

        pygame.draw.rect(win, self.color, pygame.Rect(pos, size))
        # pygame.draw.circle(win, self.color, pos, radius=size[0])

    def __lt__(self, other):
        return self.y < other.y
