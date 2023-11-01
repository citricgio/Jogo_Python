import pygame
import sys
from scenario import Background

class GameOver:
    def __init__(self, screen, score, high_score):
        self.screen = screen
        self.SCREEN_WIDTH = 1100
        self.SCREEN_HEIGHT = 600
        self.score = score
        self.high_score = high_score
        self.font = pygame.font.Font("font/8-BIT_WONDER.TTF", 25)
        self.font_title = pygame.font.Font("font/8-BIT_WONDER.TTF", 50)
        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 255, 0)
        self.BLACK = (0, 0, 0)
        self.FPS = 60
        self.scroll = 0
        self.background = Background(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.screen)

    def draw_game_over_screen(self):
        self.screen.fill(self.WHITE)
        self.background.draw_bg(self.scroll)
        self.background.draw_ground(self.scroll)
        #self.screen.fill(self.BLACK)

        game_over_text = self.font_title.render("Game Over", True, self.YELLOW)
        self.screen.blit(game_over_text, (300, 220))

        score_text = self.font.render(f"Score  {int(self.score)}", True, self.YELLOW)
        self.screen.blit(score_text, (390, 320))

        high_score_text = self.font.render(f"High Score  {self.high_score}", True, self.YELLOW)
        self.screen.blit(high_score_text, (385, 370))

        if self.score > self.high_score:
            new_record_text = self.font.render("New Record ", True, self.YELLOW)
            self.screen.blit(new_record_text, (480, 420))

    def run(self):
        game_over_active = True

        while game_over_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw_game_over_screen()
            pygame.display.flip()
            pygame.time.Clock().tick(self.FPS)


