import pygame 

class Player():
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("player_sprite.png")  # Replace with your sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.jumping = False
        self.collecting_flowers = 0
        self.has_fire_flower = False
        
        