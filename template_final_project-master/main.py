import pygame
import src
from src.controller import Controller
#import your controller

def main():
    pygame.init()
    Controller()
    Controller.mainloop()

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

width = 1300
height = 650
tile_size = 100
screen = pygame.display.set_mode((width, height))

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
