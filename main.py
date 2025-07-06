from constants import *
from player import Player, Bullet
from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame
import sys


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Bullet.containers = (bullets, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    display = pygame.display
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill("#000000")
        updatable.update(dt)
        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.has_collided_with(asteroid):
                    print("bullet has hit an asteroid!")
                    bullet.kill()
                    asteroid.kill()

            if player.has_collided_with(asteroid):
                print("Game over!")
                sys.exit(1)
        for entity in drawable:
            entity.draw(screen)
            display.update()
        dt = clock.tick(30) / 1000


if __name__ == "__main__":
    main()
