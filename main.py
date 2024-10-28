import sys
import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 300))

def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        #print("asdf")
        pygame.display.flip()

if __name__ == "__main__":
    main()