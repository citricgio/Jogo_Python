import pygame

from hero import Player
from wave import Wave
from Coin import Coin

# create game window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 180


# score
score = 0
hi_score = 0

#create game window
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 180

# heroi = sprite('sprites/image 1.svg')
# heroi_grupo = pygame.sprite.Group()
# heroi_grupo.add(heroi)

test_font = pygame.font.Font("font/VT323-Regular.ttf", 25)


##########################
#       PLAYER VAR       #
##########################
moving_sprites = pygame.sprite.Group()
player = Player(200, 150)
moving_sprites.add(player)

##########################
#       WAVE VAR       #
##########################
moving_wave = pygame.sprite.Group()
wave = Wave(-18, 1)
moving_wave.add(wave)

first_ground_image = pygame.image.load("Forest_tileset/Tiles/Sliced/Tile_01.png").convert_alpha()
middle_ground_image = pygame.image.load("Forest_tileset/Tiles/Sliced/Tile_02.png").convert_alpha()
last_ground_image = pygame.image.load("Forest_tileset/Tiles/Sliced/Tile_03.png").convert_alpha()

ground = [first_ground_image, middle_ground_image, last_ground_image]

#########################
#       COIN VAR        #
#########################
moving_coin = pygame.sprite.Group()
coin = Coin(250, 125)
moving_coin.add(coin)


# define game variables
scroll = 0
ground_image = pygame.image.load(
    "Forest_tileset/Tiles/Objects/Sliced/obj_0011_Layer-12.png"
).convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

subground = [first_subground_image, middle_subground_image, last_subground_image]

ground_width = first_ground_image.get_width()
ground_height = first_ground_image.get_height()


def draw_bg():
    for x in range(2000):
        speed = 1
        for i in bg_images:
            screen.blit(i, ((x * bg_width) - scroll * speed, 0))
            speed += 0.2


def draw_ground():
    for x in range(2000):
        screen.blit(
            ground_image,
            ((x * ground_width) - scroll * 1.0, SCREEN_HEIGHT - ground_height),
        )


# heroi = pygame.image.load('sprites/image_1.png').convert_alpha()

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


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if in_menu:
        # Código do menu
        draw_bg()
        draw_ground()
        # draw world
        menu_text = "APERTE ESPAÇO PARA COMEÇAR"
        text = test_font.render(menu_text, True, (255, 255, 255))

        screen.blit(text, (160, 60))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            in_menu = False
            in_game = True

        pygame.display.update()
    elif in_game:
        # draw world
        draw_bg()
        draw_ground()

        # screen.blit(heroi,(100,SCREEN_HEIGHT - 40))
        moving_sprites.draw(screen)
        moving_sprites.update()

        # draw coin & update
        moving_coin.draw(screen)
        moving_coin.update()

        # draw wave & update
        moving_wave.draw(screen)
        moving_wave.update()

        # get keypresses
        scroll += 1.5

        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.is_jumping = True

        score += 0.02

        if player.rect.colliderect(coin):
            score = 0

        player.jump()
        placar = test_font.render("SCORE:" + str(int(score)), False, "Green")
        hi_placar = test_font.render("HI:" + str(int(hi_score)), False, "Green")

        screen.blit(placar, (450, 20))
        screen.blit(hi_placar, (380, 20))
        screen.blit(player.image, player.rect.topleft)

        pygame.display.update()

        # heroi_grupo.draw(screen)
pygame.quit()

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