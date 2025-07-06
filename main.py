from constants import *
from player import Player, Bullet
from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame
from pygame.locals import *
import sys
import random


def main():
    random.seed(1)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
    clock = pygame.time.Clock()
    dt = 0
    flags = DOUBLEBUF
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, 16)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Bullet.containers = (bullets, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    display = pygame.display
    asteroids_destroyed = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.has_collided_with(asteroid):
                    bullet.kill()
                    asteroids_destroyed += 1 if asteroid.split(screen) else 0

            if player.has_collided_with(asteroid):
                print("Game over!")
                print(f"Number of asteroids destroyed before succumbing to skill issue: {asteroids_destroyed}")
                sys.exit(1)
        for entity in drawable:
            entity.draw(screen)
        display.update()
        dt = clock.tick(60) / 1000
        screen.fill("#000000")
        updatable.update(dt)


if __name__ == "__main__":
    main()
