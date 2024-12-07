import pygame
import random
from src.models import Player, Bullet, Asteroid, my_sprites, asteroid_surf, bullet_sprites, asteroid_sprites

player = Player(my_sprites)

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    self.width = 1200
    self.height = 600
    self.screen = pygame.display.set_mode((self.width, self.height))
    pygame.display.set_caption('Space Shooter Game')
    self.clock = pygame.time.Clock()
    self.font = pygame.font.Font('assets/pixellettersfull.ttf', 75)
    
  def mainloop(self):
    #select state loop
    bg = pygame.transform.scale((pygame.image.load('assets/images/bg.png')), (self.width, self.height))
    running = True
    
    #creating asteroids
    asteroidevent = pygame.event.custom_type()
    pygame.time.set_timer(asteroidevent, 500)
    
    while running:
        dt = self.clock.tick() / 1000
        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == asteroidevent:
                (x, y) = (random.randint(0, 1200), random.randint(-50, 10))
                Asteroid(asteroid_surf, (x, y), (my_sprites, asteroid_sprites))
        
        #update
        my_sprites.update(dt)
        
        #collision updates
        for bullet in bullet_sprites:
            collided = pygame.sprite.spritecollide(bullet, asteroid_sprites, True)
            if collided:
                bullet.kill()
        
        player_collided = pygame.sprite.spritecollide(player, asteroid_sprites, True)
        if player_collided:
            player.lives -= 1
        if player.lives == 0:
            running = False
        
        #redraw
        self.screen.blit(bg, (0, 0))
        
        #display time passed/score
        self.current_time = pygame.time.get_ticks() // 100
        self.text_surf = self.font.render(str(self.current_time), True, 'blue')
        self.text_rect = self.text_surf.get_rect(midbottom = (self.width/2, self.height - 20))
        self.screen.blit(self.text_surf, self.text_rect)
        my_sprites.draw(self.screen)
        pygame.display.update()
    
    pygame.quit()
    
  
  ### below are some sample loop states ###
