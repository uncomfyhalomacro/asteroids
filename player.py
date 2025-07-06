from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
import pygame

class Bullet(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rotation = 0
        super().__init__(self.x, self.y, SHOT_RADIUS)

    def move(self, rotation, dt):
        self.rotation = rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def draw(self, screen):
        width = 2
        circle = pygame.draw.circle(
            screen, "#ffffff", self.position, self.radius, width
        )
        return circle

    def update(self, dt):
        self.move(self.rotation, dt)



class Player(CircleShape):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rotation = 0
        self.shoot_timer = 0
        super().__init__(self.x, self.y, PLAYER_RADIUS)

    def triangle(self):
        forward = pygame.Vector2(0, 2).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        width = 2
        polygon = pygame.draw.polygon(screen, "#ffffff", points, width)
        return polygon

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shoot_timer -= dt * PLAYER_SHOOT_COOLDOWN
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt - 0.1)

        if keys[pygame.K_d]:
            self.rotate(dt + 0.1)

        if keys[pygame.K_w]:
            self.move(dt + 0.1)

        if keys[pygame.K_s]:
            self.move(dt - 0.1)

        if keys[pygame.K_SPACE]:
            if self.shoot_timer <= 0:
                self.shoot(PLAYER_SHOOT_COOLDOWN - 0.1)
                self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            else:
                print("gun is in cooldown!")

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        bullet = Bullet(self.position.x, self.position.y)
        bullet.move(self.rotation, dt)

