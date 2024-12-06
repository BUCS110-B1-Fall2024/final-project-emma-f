import pygame
from asteroid import Asteroid
from explosion import Explosion
from sprites import laser_sprites, asteroid_sprites, player, all_sprites

def collisions():

    collision_sprites = pygame.sprite.spritecollide(player, asteroid_sprites, True, pygame.sprite.collide_mask)
    if collision_sprites:
        running = False
    
    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, asteroid_sprites, True)
        if collided_sprites:
            laser.kill()
            Explosion(Explosion.frames, laser.rect.midtop, all_sprites)