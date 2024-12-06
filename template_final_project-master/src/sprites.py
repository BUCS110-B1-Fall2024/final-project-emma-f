import pygame 
from star  import Star
from player import Player 

all_sprites = pygame.sprite.Group()
asteroid_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
for i in range(20):
    Star(all_sprites, Star.image) 
player = Player(all_sprites)
