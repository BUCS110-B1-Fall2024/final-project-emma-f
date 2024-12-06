import pygame
from os.path import join

class Laser(pygame.sprite.Sprite):
    def __init__(self, sprite, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('assets/images/laser.png')).convert_alpha()
        self.rect = self.image.get_frect(midbottom = pos)
        
    def update(self, dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()