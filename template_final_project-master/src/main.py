import pygame

#screen setup
pygame .init()
width = 1300
height = 650
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flower Platformer')
fps = 60
time = pygame.time.Clock()

#load images
bg = pygame.image.load('assets/background.jpg')
grass = pygame.transform.scale(pygame.image.load('assets/grasstile.png')), (tile_size, tile_size)
dirt = pygame.transform.scale(pygame.image.load('assets/dirttile.png')), (tile_size, tile_size)
water = pygame.transform.scale(pygame.image.load('assets/watertile.png')), (tile_size, tile_size * 0.25)
platform = pygame.transform.scale(pygame.image.load('assets/grass1.png')), (tile_size, tile_size * 0.5)
burn_plants = pygame.transform.scale(pygame.image.load('assets/plantsprite.png')), (0.6 * tile_size, tile_size)
flowers = pygame.transform.scale(pygame.image.load('assets/flowersprites.png')), (0.6 * tile_size, tile_size)
fire_flower = pygame.transform.scale(pygame.image.load('assets/fire_flower.png')), (0.6 * tile_size, tile_size)
tiles = [' ', grass, dirt, water, platform]
key = [fire_flower]
coins = [flowers]
gate = [burn_plants]
frames = []
player_scale = 10
for i in range(4):
    frames.append(pygame.transform.scale(pygame.image.load('assets/walkingsprite.png')), (5 * player_scale, 5 * player_scale))

run = True
while run:
    time.tick(fps)
    screen.fill('light blue')
    screen.blit(bg, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
