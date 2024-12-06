import pygame
import random

sprites = pygame.sprite.Group()

#images
asteroid_surf = pygame.transform.scale((pygame.image.load('assets/images/asteroidsprite.png')), (70, 50))
bullet_surf = pygame.transform.scale((pygame.image.load('assets/images/bullet.png')), (20, 50))

class Player(pygame.sprite.Sprite): 
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale((pygame.image.load('assets/images/spaceship.png')), (70, 50))
        self.rect = self.image.get_rect(center = (600, 300))
        self.direction = pygame.Vector2()
        self.speed = 50
        self.cooldown = 400
        self.canshoot = True
        self.shoottime = 0 
    
    def bullettimer(self):
        if not self.canshoot:
            time = pygame.time.get_ticks()
            if time - self.shoottime >= self.cooldown:
                self.canshoot = True

    def update(self, time):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.direction.x = -1
        else: 
            self.direction.x = 0
        if keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            self.direction.y = 1
        elif keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.direction.y = -1
        else: 
            self.direction.y = 0 
        self.rect.center += self.direction * self.speed * time
        self.rect.x = max(0, min(self.rect.x, 1200 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))

        recent_keys = pygame.key.get_pressed()
        if recent_keys[pygame.K_SPACE] and self.canshoot:
            Bullet(bullet_surf, self.rect.midtop, sprites) 
            self.canshoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
        
        self.bullettimer()
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf 
        self.rect = self.image.get_rect(midbottom = pos)
    
    def update(self, time):
        self.rect.centery -= 400 * time
        if self.rect.bottom < 0:
            self.kill()
            
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(center = pos)
        self.start_time = pygame.time.get_ticks()
        self.life = 3000
        self.direction = pygame.Vector2(random.uniform(-0.5, 0.5),1)
        self.speed = random.randint(400,500)
    
    def update(self, time):
        self.rect.center += self.direction * self.speed * time
        if pygame.time.get_ticks() - self.start_time >= self.life:
            self.kill()

