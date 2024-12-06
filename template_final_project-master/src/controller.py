import pygame
from src.models import Player, Bullet, Asteroid, sprites, asteroid_surf
import random

class Controller:
  
  def __init__(self):
    #setup pygame data
    self.w = 1200
    self.h = 600
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode([self.w, self.h])
    pygame.display.set_caption('Space Game')
    self.bg = pygame.transform.scale((pygame.image.load('assets/images/bg.png')), (self.w,self.h))
    self.p = Player(sprites)
    self.time = self.clock.tick() / 1000 
    
  def mainloop(self):
    #select state loop
    time = self.clock.tick() / 1000 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            self.p.update(self.time)
            self.screen.blit(self.bg, (0, 0))
            sprites.draw(self.screen)
            sprites.update(time)
        pygame.display.flip()
    pygame.quit()
  
  ### below are some sample loop states ###
def asteroidloop(self):
      time = self.clock.tick() / 1000 
      asteroid_event = pygame.event.custom_type()
      pygame.time.set_timer(asteroid_event, 1000)
      running = True
      #event loop
      while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == asteroid_event:
                (x, y) = (random.randint(0, 1200), random.randint(0, 600))
                Asteroid(asteroid_surf, (x, y), sprites)
      #update data
        sprites.update(time)
      #redraw
        sprites.draw(self.screen)
        pygame.display.flip()
      pygame.quit()
      
      