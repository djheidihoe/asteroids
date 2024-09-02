import pygame
from constants import *

def main():
    pygame.init()
    # print("Starting asteroids! ")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # gameloop:
    #     1. check for player inputs
    #     2. update game world
    #     3. draw the game to the screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()

