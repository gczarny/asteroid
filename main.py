import pygame
from pygame import display, time

from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    _clock = time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)
        display.flip()
        time_passed = _clock.tick(60)
        dt += time_passed / 1000.0


if __name__ == "__main__":
    main()