import pygame
from drawable import Drawable
from time import time
from buffer import Buffer

class FPSCounter(Drawable):
    buffer_size = 32
    def __init__(self, pos, color=(255, 255, 255), size=20, refresh_rate=1):
        super().__init__(pos=pos, size=(size, size), color=color)
        self.font = pygame.font.SysFont('Comic Sans MS', size)
        self.text = self.font.render('FPS: 0', False, tuple(color))
        self.fps = 0
        self.refresh_rate = refresh_rate
        self.last_update = None
        self.show = True
        self.fps_buffer = Buffer(FPSCounter.buffer_size)

    def draw(self, win, scale, offset):
        if not self.show:
            return

        self.text = self.font.render(f'FPS: {round(self.fps)}', False, tuple(self.color))
        win.blit(self.text, tuple(self.pos))

    def update(self, fps):
        self.fps_buffer.add(fps)

        if self.last_update is None:
            self.fps = self.fps_buffer.average()
            self.last_update = time()

        elif time() - self.last_update > self.refresh_rate:
            self.fps = self.fps_buffer.average()
            self.last_update = time()


