import pygame

class Tiles: 
    def __init__(self, tile_type, x=0, y=0, img_file=str):
        self.tile_type = tile_type
        self.x = x
        self.y = y
        self.img_file = img_file
        self.image = pygame.image.load(self.img_file)  # Load the image
        self.rect = self.image.get_rect()  # Get the image's rectangle (position)
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        """Draw the tile on the screen at its (x, y) position."""
        screen.blit(self.image, self.rect)

#loading tiles
bg = (pygame.transform.scale(pygame.image.load('assets/background.jpg'), (1300, 650)))    
grass = pygame.transform.scale(pygame.image.load('assets/grasstile.png'), (100, 100))
dirt = pygame.transform.scale(pygame.image.load('assets/dirttile.png'), (100, 100))
water = pygame.transform.scale(pygame.image.load('assets/watertile.png'), (100, 100))
platform = pygame.transform.scale(pygame.image.load('assets/grass1.png'), (100, 100))
burn_plants = pygame.transform.scale(pygame.image.load('assets/plantsprites.png'), (100, 100))
flowers = pygame.transform.scale(pygame.image.load('assets/flowersprites.png'), (100, 100))
fire_flower = pygame.transform.scale(pygame.image.load('assets/fire_flower_sprites_sheet.png'), (100, 100))
lock = pygame.transform.scale(pygame.image.load('assets/locks.gif'), (100, 100))

tiles_images = {
    0: bg,  # Empty space or background tile
    1: dirt,
    2: grass,
    3: platform,
    4: water,
    5: None,  # Player spawn (if needed)
    6: fire_flower,  # Fire flower
    7: flowers,  # Normal flower
    8: flowers,  # Normal flower (you can adjust as needed)
    9: flowers,  # Normal flower (you can adjust as needed)
    10: burn_plants,  # Burn plants
    11: burn_plants,  # Burn plants
    12: burn_plants,  # Burn plants
    13: burn_plants  # Burn plants
                }

tile_objects = []

for i in range(len(level)):
    row = []
    for j in range(len(level[i])):
        value = level[i][j]
        image = tiles_images.get(value)
        if image:  # If there's an image for this tile value
            row.append(Tile(tile_type=value, x=j * tile_size, y=i * tile_size, image=image))
        else:
            row.append(None)  # Empty space (no tile)
    tile_objects.append(row)