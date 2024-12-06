import pygame
from random import randint
from controller import Controller
from os.path import join

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, sprite):
        super().__init__(groups)
        self.image = pygame.image.load(join('assets/images/star.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (randint(0, Controller.width),randint(0, Controller.height)))
        
