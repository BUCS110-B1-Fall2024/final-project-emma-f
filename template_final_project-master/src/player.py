from os.path import join
import pygame
from controller import Controller
from laser import Laser
from sprites import laser_sprites, laser, all_sprites

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images/ship.jpg')).convert_alpha()
        self.rect = self.image.get_frect(center = (Controller.width / 2, Controller.height / 2))
        self.direction = pygame.Vector2()
        self.speed = 300

        #cooldown laser
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

        self.mask = pygame.mask.from_surface(self.image)
    
    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])  
        self.direction = self.direction.normalize() if self.direction else self.direction 
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser, self.rect.midtop, (all_sprites, laser_sprites)) 
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
        
        self.laser_timer()