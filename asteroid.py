from circleshape import CircleShape
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
