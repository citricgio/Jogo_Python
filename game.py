import pygame
import sys
from scenario import Background
from hero import Player
from wave import Wave
from Coin import Coin

class Game:
    def __init__(self):
        pygame.init()
        self.test_font = pygame.font.Font("font/VT323-Regular.ttf", 25)
        self.SCREEN_WIDTH = 600
        self.SCREEN_HEIGHT = 180
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.moving_sprites = pygame.sprite.Group()
        self.player = Player(200, 150)
        self.moving_sprites.add(self.player)
        self.moving_wave = pygame.sprite.Group()
        self.wave = Wave(-18, 1)
        self.moving_wave.add(self.wave)
        self.moving_coin = pygame.sprite.Group()
        self.coin = Coin(250, 125)
        self.moving_coin.add(self.coin)
        self.score = 0
        self.hi_score = 0
        self.scroll = 0
        self.background = Background(self.SCREEN_WIDTH, self.SCREEN_HEIGHT,self.screen)

    def run(self):
        while True:
            self.scroll += 4
            self.background.draw_bg(self.scroll)
            self.background.draw_ground(self.scroll)
            self.draw_game_elements()
            self.handle_events()
            self.update_game()
            self.render_scores()
            pygame.display.update()


    def draw_game_elements(self):
        self.moving_sprites.draw(self.screen)
        self.moving_sprites.update()
        self.moving_coin.draw(self.screen)
        self.moving_coin.update()
        self.moving_wave.draw(self.screen)
        self.moving_wave.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.is_jumping = True

    def update_game(self):
        self.score += 0.02
        if self.player.rect.colliderect(self.coin):
            self.score = 0
        self.player.jump()

    def render_scores(self):
        placar = self.test_font.render("SCORE:" + str(int(self.score)), False, "Green")
        hi_placar = self.test_font.render("HI:" + str(int(self.hi_score)), False, "Green")
        self.screen.blit(placar, (450, 20))
        self.screen.blit(hi_placar, (380, 20))
        self.screen.blit(self.player.image, self.player.rect.topleft)

        pygame.display.update()