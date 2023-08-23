from renderSystem import RenderSystem
from drawable import Drawable


class SolarSystem(Drawable):
    def __init__(self, star=None, planets=None):
        Drawable.__init__(self, pos=(0, 0), size=(0, 0), color=(0, 0, 0))
        self.star = None
        self.show_trail = False

        if star is not None:
            self.star = star

        if planets is not None:
            for planet in self.planets:
                self.add_planet(planet)

    def add_planet(self, planet):
        self.star.add_observer(planet)


    def draw(self, win, scale, offset):
        if self.show_trail:
            for planet in self.planets:
                planet.draw_trail(win)

        for planet in self.planets:
            planet.draw(win, scale, offset)

        self.star.draw(win, scale, offset)

    def update(self, dt):
        self.star.update(dt)
        for planet in self.planets:
            planet.update(dt)
            if self.show_trail:
                planet.update_trail()

    def toggle_trail(self):
        self.clear_trails()
        self.show_trail = not self.show_trail

    def clear_trails(self):
        for planet in self.planets:
            planet.clear_trail()

    @property
    def planets(self):
        return self.star.observers
