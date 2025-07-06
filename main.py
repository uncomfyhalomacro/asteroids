from constants import *
from player import Player
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
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    display = pygame.display
    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    player.containers = (updatable, drawable)
    while True:
        for event in pygame.event.get():
            if event.type in [
                pygame.WINDOWSHOWN,
                pygame.WINDOWENTER,
                pygame.WINDOWFOCUSGAINED,
            ]:
                screen.fill("#000000")
                for entity in drawable:
                    entity.draw(screen)
                    display.update()
            if event.type == pygame.KEYDOWN:
                updatable.update(dt)
                screen.fill("#000000")
                for entity in drawable:
                    entity.draw(screen)
                    display.update()
            if event.type == pygame.QUIT:
                sys.exit()
        clock.tick(60)


if __name__ == "__main__":
    main()
