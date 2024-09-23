import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    y = SCREEN_HEIGHT / 2 
    x = SCREEN_WIDTH / 2
    player = Player(x, y)
    dt = 0
    # gameloop:
    #     1. check for player inputs
    #     2. update game world
    #     3. draw the game to the screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

