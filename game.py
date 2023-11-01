import pygame
import sys
from random import randint
from scenario import Background
from hero import Player
from wave import Wave
from enemy import Enemy
from Coin import Coin
from gameOver import GameOver
from time import sleep

class Game:
    def __init__(self):
        pygame.init()
        self.test_font = pygame.font.Font("font/8-BIT_WONDER.TTF", 25)
        self.SCREEN_WIDTH = 1100
        self.SCREEN_HEIGHT = 600
        self.clock = pygame.time.Clock()
        self.FPS = 60  
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.moving_sprites = pygame.sprite.Group()
        self.player = Player(300, 500)
        self.moving_sprites.add(self.player)
        self.moving_wave = pygame.sprite.Group()
        self.wave = Wave(-18,320)
        self.moving_wave.add(self.wave)
        self.moving_coin = pygame.sprite.Group()
        self.coin = Coin(randint(600,1000), 500)
        self.moving_coin.add(self.coin)
        self.moving_shark = pygame.sprite.Group()
        self.shark = Enemy(2500,430)
        self.moving_shark.add(self.shark)
        self.score = 0
        self.hi_score = 0
        self.scroll = 0
        self.background = Background(self.SCREEN_WIDTH, self.SCREEN_HEIGHT,self.screen)

    def run(self):
        running = True
        while running:
            self.clock.tick(self.FPS)  # Control the frame rate
            self.scroll += 2
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
        self.moving_shark.draw(self.screen)
        self.moving_shark.update() 
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
            self.score += 10
            self.coin.rect.y = randint(1000,3000)
        
        self.shark.update()
        # Check for collision with the shark using spritecollide
        if pygame.sprite.spritecollide(self.player, self.moving_shark, False, pygame.sprite.collide_mask) or pygame.sprite.spritecollide(self.shark, self.moving_sprites, False, pygame.sprite.collide_mask):
            game_over = GameOver(self.screen, self.score, self.hi_score)    
            if self.score > self.hi_score:  # Check if the current score is higher
                self.hi_score = self.score
            sleep(2)
            game_over.run()


        self.player.jump()

    def render_scores(self):
        placar = self.test_font.render("SCORE " + str(int(self.score)), False, "Green")
        hi_placar = self.test_font.render("HI " + str(int(self.hi_score)), False, "Green")
        self.screen.blit(placar, (850, 20))
        self.screen.blit(hi_placar, (700, 20))
        self.screen.blit(self.player.image, self.player.rect.topleft)

        pygame.display.update()

game = Game()

game.run()
