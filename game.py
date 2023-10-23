import pygame
from scenario import draw_bg
from scenario import draw_ground
from hero import Player
from wave import Wave
from Coin import Coin

pygame.init()
test_font = pygame.font.Font("font/VT323-Regular.ttf", 25)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 180

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


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


def game(score,hi_score):
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