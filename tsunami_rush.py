import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

#create game window
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 180

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tsunami Rush")

#define game variables
scroll = 0

first_ground_image = pygame.image.load("Forest_tileset/Tiles/Sliced/Tile_01.png").convert_alpha()
middle_ground_image = pygame.image.load("Forest_tileset/Tiles/Sliced/Tile_02.png").convert_alpha()
last_ground_image = pygame.image.load("Forest_tileset/Tiles/Sliced/Tile_03.png").convert_alpha()

ground = [first_ground_image, middle_ground_image, last_ground_image]

first_subground_image = pygame.image.load("Forest_tileset/Tiles/Sliced/Tile_13.png").convert_alpha()
middle_subground_image = pygame.image.load("Forest_tileset/Tiles/Sliced/Tile_14.png").convert_alpha()
last_subground_image = pygame.image.load("Forest_tileset/Tiles/Sliced/Tile_15.png").convert_alpha()

subground = [first_subground_image, middle_subground_image, last_subground_image]

ground_width = first_ground_image.get_width()
ground_height = first_ground_image.get_height()

bg_images = []


for i in range(1, 5):
    bg_image = pygame.image.load(f"Forest_tileset/BG/{i}.png").convert_alpha()
    bg_images.append(bg_image)

bg_width = bg_images[0].get_width()

def draw_bg():
    for x in range(200):
      speed = 0.2
      for i in bg_images:
          screen.blit(i, ((x * bg_width) - scroll * speed, - ground_height - 10))
          speed += 0.2

def draw_generic_platform(grounds, ground_width, scroll, n, x, y):
    screen.blit(grounds[0], (x, y))
    for i in range(n):
      screen.blit(grounds[1], ((x + i * ground_width) - scroll * 1.0, y))
    screen.blit(grounds[2], (x + n * ground_width, y))


#game loop
run = True
while run:

    clock.tick(FPS)

    #draw world
    draw_bg()
    draw_generic_platform(ground, ground_width, scroll, 200, 0, SCREEN_HEIGHT - 2 * ground_height)
    draw_generic_platform(subground, ground_width, scroll, 200, 0, SCREEN_HEIGHT - ground_height)
    draw_generic_platform(ground, ground_width, scroll, 10, 50, 100)


    #get keypresses
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll > 0:
      scroll -= 5
    if key[pygame.K_RIGHT] and scroll < 3000:
      scroll += 5

    #event handlers
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    pygame.display.update()


pygame.quit()