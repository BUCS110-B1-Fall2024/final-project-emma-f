import pygame
import random
from src.models import Player, Bullet, Asteroid, my_sprites, asteroid_surf, bullet_sprites, asteroid_sprites
from etc.others import draw_text, Button

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
    self.font = pygame.font.Font('assets/pixellettersfull.ttf', 50)
    self.bg = pygame.transform.scale((pygame.image.load('assets/images/bg.png')), (self.width, self.height))
    self.dt = self.clock.tick() / 1000
    
  def mainloop(self):
    #select state loop
    running = True
    
    #creating asteroids
    asteroidevent = pygame.event.custom_type()
    pygame.time.set_timer(asteroidevent, 350)
    
    while running:
        self.mainmenu()

        while running:
          selection = self.mainmenu()  
          if selection == "play":
              self.start_game()
          elif selection == "how to play":
              self.howtoplay()
          elif selection == "quit":
              running = False
        
        #update
        my_sprites.update(self.dt)
        
        #redraw
        self.screen.blit(self.bg, (0, 0))
        
        my_sprites.draw(self.screen)
        pygame.display.update()
    
    pygame.quit()
    
  def howtoplay(self):
    self.screen.fill('black')
    draw_text("How to Play", self.font, 'white', self.screen, self.width // 2, 100)
    
    instructions = [
        "Use arrow keys to move.",
        "Press space to shoot.",
        "Avoid asteroids!"
    ]
    
    for i, instruction in enumerate(instructions):
       draw_text(instruction, self.font, 'green', self.screen, self.width // 2, 200 + i * 50)

    back_button = Button("Back to Menu", (self.width // 2 - 130, self.height - 100))
    back_button.draw(self.screen, self.font)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_clicked():
                    return "mainmenu"
                  
                  
  def mainmenu(self):
    pygame.init()
    self.screen.fill('black')
    draw_text("Space Shooter", self.font, 'red', self.screen, self.width // 2, 100)
    
    play_button = Button("Play", (self.width // 2 - 130, 250))
    how_to_play_button = Button("How to Play", (self.width // 2 - 130, 325))
    quit_button = Button("Quit", (self.width // 2 - 130, 400))
    
    play_button.draw(self.screen, self.font)
    how_to_play_button.draw(self.screen, self.font)
    quit_button.draw(self.screen, self.font)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_clicked():
                    return "play"
                if how_to_play_button.check_clicked():
                    return "how to play"
                if quit_button.check_clicked():
                    pygame.quit()
                    
  def start_game(self):
    # Game loop
    game_running = True
    
    # Create asteroids
    asteroidevent = pygame.event.custom_type()
    pygame.time.set_timer(asteroidevent, 350)
    
    while game_running:
        self.screen.blit(self.bg, (0, 0))
        
        my_sprites.update(self.dt)
        
        # Event loop for gameplay
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == asteroidevent:
                (x, y) = (random.randint(0, 1200), random.randint(-50, 10))
                Asteroid(asteroid_surf, (x, y), (my_sprites, asteroid_sprites))

        # Update and check for collisions
        my_sprites.update(self.dt)
        for bullet in bullet_sprites:
            collided = pygame.sprite.spritecollide(bullet, asteroid_sprites, True)
            if collided:
                bullet.kill()

        player_collided = pygame.sprite.spritecollide(player, asteroid_sprites, True)
        if player_collided:
            player.lives -= 1
        if player.lives == 0:
            self.mainmenu() 
        
        # Redraw
        self.screen.blit(self.bg, (0, 0))

        # Display time passed/score
        self.current_time = pygame.time.get_ticks() // 100
        draw_text(f"Score: {str(self.current_time)}", self.font, 'blue', self.screen, (self.width/2), (self.height - 40))
        draw_text(f"Lives Left: {player.lives}", self.font, 'white', self.screen, 140, 40)

        my_sprites.draw(self.screen)
        pygame.display.update()
        
    pygame.quit()