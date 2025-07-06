from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS
import random
import pygame


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        width = 2
        circle = pygame.draw.circle(
            screen, "#ffffff", self.position, self.radius, width
        )
        return circle

    def split(self, screen):
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("asteroid destroyed")
            self.kill()
            return True
        elif ASTEROID_MIN_RADIUS * 2 == self.radius:
            self.spawn(ASTEROID_MIN_RADIUS, self.position)
            self.radius = ASTEROID_MIN_RADIUS
        elif ASTEROID_MAX_RADIUS == self.radius:
            self.spawn(ASTEROID_MIN_RADIUS * 2, self.position)
            self.radius = ASTEROID_MIN_RADIUS * 2
        return False

    def spawn(self, radius, position):
        speed = random.randint(40, 100)
        velocity = pygame.Vector2(0, 1) * speed
        velocity.rotate(random.randint(-60, 60))
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
        self.velocity.rotate(random.randint(-60, 60))
