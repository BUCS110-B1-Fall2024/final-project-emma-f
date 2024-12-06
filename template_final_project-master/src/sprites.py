import pygame 
from star  import Star
from player import Player 
from os.path import join

star = pygame.image.load(join('assets/images/star.png')).convert_alpha()
asteroid = pygame.image.load(join('assets/images/asteroidsprite.png')).convert_alpha()
laser = pygame.image.load(join('assets/images/laser.png')).convert_alpha()
font = pygame.font.Font(join('assets/images/pixellettersfull.ttf'), 40)
explosion_frames = [pygame.image.load(join('assets/images/explosions', f'{i}.png')).convert_alpha() for i in range(4)]

all_sprites = pygame.sprite.Group()
asteroid_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
for i in range(20):
    Star(all_sprites, star) 
player = Player(all_sprites)
