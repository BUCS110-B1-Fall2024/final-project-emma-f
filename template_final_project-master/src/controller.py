import pygame
from laser import Laser
from player import Player
from star import Star
from asteroid import Asteroid
from sprites import all_sprites, asteroid_sprites
from collision import collisions
from explosion import Explosion
import random
from os.path import join

class Controller:
  
  def __init__(self):
    #setup pygame data
    width = 1200
    height = 600
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption('Space Game')
    
  def mainloop(self):
    #select state loop
    running = True
    while running:
      dt = self.clock.tick() / 1000
    
      all_sprites.update(dt)
      collisions()
      
      self.screen.fill('#3a2e3f')
      display_score()
      all_sprites.draw(self.screen)

    pygame.display.update()
  pygame.quit()
    
  def display_score():
    font = pygame.font.Font(join('assets/images/pixellettersfull.ttf'), 40)
    current_time = pygame.time.get_ticks() // 100
    text_surf = font.render(str(current_time), True, (240,240,240))
    text_rect = text_surf.get_frect(midbottom = (width / 2,height - 50))
    screen.blit(text_surf, text_rect)
    pygame.draw.rect(screen, (240,240,240), text_rect.inflate(20,10).move(0,-8), 5, 10)
  ### below are some sample loop states ###
  def menuloop(self):
    
      #event loop
    start_event = pygame.event.custom_type()
      #update data
      #redraw
      
  def gameloop(self):
      #event loop
      asteroid_event = pygame.event.custom_type()
      pygame.time.set_timer(asteroid_event, 200)
      #update data
      running = True
      while running:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
          if event.type == asteroid_event:
            x, y = random.randint(0, self.width), random.randint(-200, -100)
            Asteroid(asteroid, (x, y), (all_sprites, asteroid_sprites))
      #redraw
      self.screen.fill('#3a2e3f')
      display_score()
      all_sprites.draw(self.screen)

def gameoverloop(self):
    #event loop
    end = pygame.event.custom_type()
    #update data
    #redraw
    return None