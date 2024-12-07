import pygame
import random

asteroid_surf = pygame.transform.scale((pygame.image.load('assets/images/asteroidsprite.png')), (70, 70))
bullet_surf = pygame.transform.scale((pygame.image.load('assets/images/bullet.png')), (20, 50))

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale((pygame.image.load('assets/images/spaceship.png')), (60, 50))
        self.rect = self.image.get_rect(center = (600,300))
        self.direction = pygame.math.Vector2(0, 0)
        self.pressed_down = False
        self.speed = 200
        self.lives = 3
        
        #anti-spamming space xxxxx
        self.can_shoot = True
        self.bullet_shoot_time = 0
        self.cooldown = 500
        
    def bullet_cooldown(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.cooldown >= self.cooldown:
                self.can_shoot = True
        
    def update(self, dt):
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
        self.rect.center += self.direction * self.speed * dt
        if self.direction.length() != 0:
            self.direction = self.direction.normalize()
        self.rect.x = max(0, min(self.rect.x, 1200 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))
    
        if keys[pygame.K_SPACE] and not self.pressed_down and self.can_shoot:
            self.pressed_down = True  
            Bullet(bullet_surf, self.rect.midtop, (my_sprites, bullet_sprites))
            self.can_shoot = False
            self.bullet_shoot_time = pygame.time.get_ticks()
        if not keys[pygame.K_SPACE]:
            self.pressed_down = False
        self.bullet_cooldown()
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, pos, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(midtop = pos)
    
    def update(self, dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()
    
class Asteroid(pygame.sprite.Sprite):
    def __init__(self, image, pos, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.speed = random.randint(100, 300)
        self.strt_time = pygame.time.get_ticks()
        self.life = 6000
        self.direction = pygame.math.Vector2(random.choice([-0.7, 0.7]), 1)
        
    def update(self, dt):
        self.rect.centerx += self.direction.x * self.speed * dt
        self.rect.centery += self.direction.y * self.speed * dt
        if pygame.time.get_ticks() - self.strt_time >= self.life:
            self.kill()
            
my_sprites = pygame.sprite.Group()
asteroid_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()