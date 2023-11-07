import pygame
import sys
from random import randint
from scenario import Background
from hero import Player
from gameOver import GameOver
from time import sleep
from agent import AIPlayer
from gameOver import GameOver
from sprites import Sprites
import torch
class Game:
    def __init__(self):
        self.test_font = pygame.font.Font("font/8-BIT_WONDER.TTF", 25)
        self.SCREEN_WIDTH = 1100
        self.SCREEN_HEIGHT = 600
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.ORANGE = (255,181,2)
        self.BROWN = (128,90,0)

        #Grupo de sprites do jogador
        self.moving_sprites = pygame.sprite.Group()
        self.player = Player(300, 500, 'sprites/hero', 0.05,0)
        self.moving_sprites.add(self.player)

        #Grupo de sprites da onda
        self.moving_wave = pygame.sprite.Group()
        self.wave = Sprites(-9, 320, 'sprites/WAVE', 0.05, 0)
        self.moving_wave.add(self.wave)

        #Grupo de sprites da moeda
        self.moving_coin = pygame.sprite.Group()
        self.coin = Sprites(randint(600, 1000), 500, 'sprites/GoldCoinSprite', 0.15, 5)
        self.moving_coin.add(self.coin)

        #Grupo de sprites do tubarao
        self.moving_shark = pygame.sprite.Group()
        self.shark = Sprites(2500, 430, 'sprites/shark', 0.15, 10)
        self.moving_shark.add(self.shark)


        self.moving_ai = pygame.sprite.Group()
        self.agent = AIPlayer(400,520,'sprites/ai_player', 0.05,0)
        self.moving_ai.add(self.agent)

        # Pontuação do jogo
        self.score = 0  
        self.hi_score = 0
        
        self.scroll = 0
        self.background = Background(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.screen)
        
    

    ####################################
    #           METODOS DO JOGO        #
    ####################################


    def run(self):
        while True:
            self.scroll += 4
            self.background.draw_bg(self.scroll)
            self.background.draw_ground(self.scroll)
            self.draw_game_elements()
            self.handle_events()
            self.step()
            self.render_scores()
            pygame.display.update()


    def draw_game_elements(self):
        self.moving_sprites.draw(self.screen)
        self.moving_sprites.update()
        self.moving_coin.draw(self.screen)
        self.moving_coin.update()
        self.moving_wave.draw(self.screen)
        self.moving_wave.update()
        self.moving_shark.draw(self.screen)
        self.moving_shark.update()
        self.moving_ai.draw(self.screen)
        self.moving_ai.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.is_jumping = True


    def step(self,action):
        self.scroll += 4
        self.background.draw_bg(self.scroll)
        self.background.draw_ground(self.scroll)
        self.draw_game_elements()
        self.handle_events()
        self.render_scores()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.is_jumping = True

        if self.player.is_jumping:
            self.player.jump()

        self.score += 0.02  # Increment the score over time


        #action = self.agent.select_action([self.shark.rect[1],self.shark.rect[1], (self.agent.rect[0] - self.shark.rect[0]), self.agent.rect[1], self.agent.rect[1]])


        # Perform AI action
        if action == 1:
            self.agent.is_jumping = True

        # Handle jumping for Player 1


        if self.agent.is_jumping:
            self.agent.jump()
        

        # Check if the player collides with the coin
        if self.player.rect.colliderect(self.coin):
            self.score += 10  # Increase the score when the player collects a coin
            # Move the coin to a new position
            self.coin.rect.x = randint(1000, 3000)  
            self.coin.rect.y = randint(350,500)


        # Check for collisions with the shark and update the score accordingly
        if (
            pygame.sprite.spritecollide(self.player, self.moving_shark, False, pygame.sprite.collide_mask)
            or pygame.sprite.spritecollide(self.shark, self.moving_sprites, False, pygame.sprite.collide_mask)
        ):
            self.score -= 10
            if self.score < 0:
                self.score = 0
            self.shark.rect.x = randint(1000, 2000)  # Move the shark to a new position
            
            #self.gameOver = GameOver(self.screen,self.score,self.hi_score)   
            #gameOver.run()


        #return self.get_state(), self.calculate_reward(), self.is_game_over()


    def render_scores(self):


        placar = self.test_font.render("SCORE " + str(int(self.score)), False, self.ORANGE)
        placar_shadow = self.test_font.render("SCORE " + str(int(self.score)), False, self.BROWN)
        hi_placar = self.test_font.render("HI " + str(int(self.hi_score)), False, self.ORANGE)
        hi_placar_shadow = self.test_font.render("HI " + str(int(self.hi_score)), False, self.BROWN)
        self.screen.blit(hi_placar_shadow, (20, 24))
        self.screen.blit(hi_placar, (20, 20))

        self.screen.blit(placar_shadow, (hi_placar.get_rect().right +100, 24))
        self.screen.blit(placar, (hi_placar.get_rect().right +100, 20))
    
        #self.screen.blit(self.player.image, self.player.rect.topleft)

    ####################################
    #           METODOS DA IA          #
    ####################################

    def reset(self):
        #initialize game state
        self.agent = AIPlayer(400,520,'sprites/ai_player', 0.05,0)
        self.moving_ai = pygame.sprite.Group()
        self.moving_ai.add(self.agent)
        
        self.moving_wave = pygame.sprite.Group()
        self.wave = Sprites(-9, 320, 'sprites/WAVE', 0.05, 0)
        self.moving_wave.add(self.wave)

        #Grupo de sprites da moeda
        self.moving_coin = pygame.sprite.Group()
        self.coin = Sprites(randint(600, 1000), 500, 'sprites/GoldCoinSprite', 0.15, 5)
        self.moving_coin.add(self.coin)

        #Grupo de sprites do tubarao
        self.moving_shark = pygame.sprite.Group()
        self.shark = Sprites(2500, 430, 'sprites/shark', 0.15, 10)
        self.moving_shark.add(self.shark)



    def get_state(self):
        return [self.shark.rect[1],self.shark.rect[1], (self.agent.rect[0] - self.shark.rect[0]), self.agent.rect[1], self.agent.rect[1]]

    def calculate_reward(self):
        reward = 0
        if pygame.sprite.spritecollide(self.player, self.moving_shark, False, pygame.sprite.collide_mask):
            reward =-10
        else: 
            reward = 10 
        return reward

    def is_game_over(self):
        if pygame.sprite.spritecollide(self.agent, self.moving_shark, False, pygame.sprite.collide_mask):
            return True
        return False




    def train(self, num_episodes):

        for episode in range(num_episodes):
            self.reset()  # Reset the game state at the beginning of each episode
            done = False  # Flag to indicate if the episode is finished
            state = self.get_state()

            while not done:
                action = self.agent.select_action(state)
                print(f'acao tomada; {action}')
                self.step(action)  # Take the selected action and update the game state
                reward = self.calculate_reward()
                next_state = self.get_state()
                done = self.is_game_over()
                print(f'reward')
                print(done)
                self.agent.learn(state, action, reward, next_state, done)
                state = next_state



pygame.init()
game = Game()
game.train(10)  # Train for 100 episodes
