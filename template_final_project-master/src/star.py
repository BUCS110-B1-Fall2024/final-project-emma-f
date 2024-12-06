import pygame
from random import randint
from controller import Controller

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, Controller.width),randint(0, Controller.height)))
        
