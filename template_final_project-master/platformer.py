from player import Player
import pygame

#screen setup
pygame .init()
width = 1300
height = 650
tile_size = 100
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flower Platformer')
fps = 60
time = pygame.time.Clock()
level = [[0 for _ in range(int((width/tile_size)))]for _ in range(int((height/tile_size)))]
level.append([1, 1, 2, 2, 3, 3, 4, 4, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13])
level.append([11, 11, 12, 12, 13, 13, 1, 1,1 ,1 ,1, 1, 12, 3])

bg = (pygame.transform.scale(pygame.image.load('assets/background.jpg'), (1300, 650)))
grass = pygame.transform.scale(pygame.image.load('assets/grasstile.png'), (100, 100))
dirt = pygame.transform.scale(pygame.image.load('assets/dirttile.png'), (100, 100))
water = pygame.transform.scale(pygame.image.load('assets/watertile.png'), (100, 100))
platform = pygame.transform.scale(pygame.image.load('assets/grass1.png'), (100, 100))
burn_plants = pygame.transform.scale(pygame.image.load('assets/plantsprites.png'), (100, 100))
flowers = pygame.transform.scale(pygame.image.load('assets/flowersprites.png'), (100, 100))
fire_flower = pygame.transform.scale(pygame.image.load('assets/fire_flower_sprites_sheet.png'), (100, 100))
lock = pygame.transform.scale(pygame.image.load('assets/locks.gif'), (100, 100))
tiles = [' ', grass, dirt, water, platform]
key = [fire_flower]
coins = [flowers]
gate = [burn_plants]
frames = []
player_scale = 10
for i in range(4):
    frames.append(pygame.transform.scale(pygame.image.load(f'assets/walkingsprites.png'),
                                         (5 * player_scale, 8 * player_scale)))
    
#game variables
inventory = [False, False, False, False]  #4 fire flowers

#draw all tiles based on value in level array
def draw_board(board):
    # 0 - empty frame, 1 - below ground dirt, 2 - walkable grass, 3 - platform, 4 - water, 5 - player spawn, 6-9 fire flowers, 10-13 burn plants
    for i in range(len(board)):
        for j in range(len(board[i])):
            value = board[i][j]
            if 0 < value < 4:
                screen.blit(tiles[value], (j * tile_size, i * tile_size))
            elif value == 4: 
                screen.blit(tiles[value], (j * tile_size, i * tile_size + 75))
            elif 6 <= value < 10:
                if value - 6 < len(key) and not inventory[value - 6]:
                    screen.blit(key[value - 6], (j * tile_size + 20, i * tile_size))
            elif 10 <= value < 14:  
                if value - 10 < len(gate):
                    screen.blit(gate[value - 10], (j * tile_size, i * tile_size))
                    if value - 10 < len(inventory) and not inventory[value - 10]:
                        screen.blit(lock, (j * tile_size + 20, i * tile_size + 20))
        
run = True
while run:
    time.tick(fps)
    screen.fill('light blue')
    screen.blit(bg, (0, 0))
    draw_board(level)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
