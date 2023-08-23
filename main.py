import pygame
from solarSystem import SolarSystem
from random import randint, random, choice
from fpsCounter import FPSCounter
from renderSystem import RenderSystem
from math import cos, sin, sqrt, pi
from universe import Universe
from celestial import Celestial
import sys
from utils import multiply, randbetween, inverse



#initialze pygame font

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Solar System")
clock = pygame.time.Clock()
run = True

renderSystem = RenderSystem()

sun = Celestial(pos=(0, 0), mass=2e24, radius=20, color=Universe.color)
solarSystem = SolarSystem(star=sun)


planet_count = sys.argv[1] if len(sys.argv) > 1 else 1000


for i in range(int(planet_count)):
    distance = sqrt(randint(0.09e16, 81e16))
    angle = random() * 2 * pi
    pos = (distance * cos(angle), distance * sin(angle))
    mass = 1e24
    radius = randint(1, 2)
    color = (randint(0, 192), randint(128, 255), 0.5*randint(128, 255))
    planet = Celestial(pos=pos, mass=mass, radius=radius, color=color)
    planet.set_velocity(multiply(sun.perfect_velocity(planet), randbetween(1, 1)))
    solarSystem.add_planet(planet)



fpsCounter = FPSCounter(pos=(10, 10), color=inverse(Universe.color) , size=20, refresh_rate=1)

renderSystem.add(solarSystem, 0)
renderSystem.add(fpsCounter, 0)

while run:
    clock.tick(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

            if event.key == pygame.K_SPACE:
                fpsCounter.show = not fpsCounter.show

            if event.key == pygame.K_t:
                solarSystem.toggle_trail()

    screen.fill(Universe.color)

    dt = clock.get_time() / 1000

    fpsCounter.update(1 / dt)

    solarSystem.update(100000 * dt)

    renderSystem.draw(screen, scale=1e-6, offset=(780, 430))

    pygame.display.update()
