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
    while True:
        for event in pygame.event.get():
            if event.type in [
                pygame.WINDOWSHOWN,
                pygame.WINDOWENTER,
                pygame.WINDOWFOCUSGAINED,
            ]:
                screen.fill("#000000")
                player.draw(screen)
                pygame.display.update()
            if event.type == pygame.KEYDOWN:
                player.update(dt)
                screen.fill("#000000")
                player.draw(screen)
                pygame.display.update()
            if event.type == pygame.QUIT:
                sys.exit()
        clock.tick(60)


if __name__ == "__main__":
    main()
