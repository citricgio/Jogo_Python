import pygame
from hero import Player
from wave import Wave
from Coin import Coin
from Menu import PygameMenu 
from game import Game


pygame.init()

clock = pygame.time.Clock()
FPS = 60

# create game window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 180



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tsunami Rush")


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


#########################
#       COIN VAR        #
#########################
moving_coin = pygame.sprite.Group()
coin = Coin(250, 125)
moving_coin.add(coin)


menu = PygameMenu(screen, ["Start", "Level", "Options"])
game = Game()

# heroi = pygame.image.load('sprites/image_1.png').convert_alpha()


in_menu = True
in_game = False
# game loop
run = True
while run: 
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if in_menu:
        # Código do menu
        menu.run()
        if menu.selected_option == 0:
            in_menu = False
            in_game = True


    elif in_game:
        game.run()
        #score += 0.01
        #scroll += 2
        # heroi_grupo.draw(screen)

pygame.quit()
