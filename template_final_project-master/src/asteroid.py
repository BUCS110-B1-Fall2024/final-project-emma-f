import pygame 
import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, sprite, pos, groups):
        super().__init__(groups)
        self.original_surf = sprite
        self.image = pygame.image.load(join('assets/images/asteroidsprite.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 2000
        self.direction = pygame.Vector2(random.uniform(-0.5, 0.5),1)
        self.speed = random.randint(100,500)
        self.rotation_speed = random.randint(40,80)
        self.rotation = 0
    
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()
        self.rotation += self.rotation_speed * dt
        self.image = pygame.transform.rotozoom(self.original_surf, self.rotation, 1)
        self.rect = self.image.get_frect(center = self.rect.center)