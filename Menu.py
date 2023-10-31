import pygame
import sys
from scenario import Background

class PygameMenu:
    def __init__(self, screen, menu_options):
        self.screen = screen
        self.SCREEN_WIDTH = 1100
        self.SCREEN_HEIGHT = 600
        self.menu_options = menu_options
        self.selected_option = 0
        self.font = pygame.font.Font(None, 36)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.FPS = 60
        self.scroll = 0
        self.background = Background(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.screen)

    def draw_menu(self):
        self.screen.fill(self.WHITE)
        self.background.draw_bg(self.scroll)
        self.background.draw_ground(self.scroll)

        title_text = self.font.render("Menu", True, self.BLACK)
        self.screen.blit(title_text, (250, 30))

        for i, option in enumerate(self.menu_options):
            text = self.font.render(option, True, self.BLACK)
            text_rect = text.get_rect(center=(200 + i * 100, 90))
            self.screen.blit(text, text_rect)

            if i == self.selected_option:
                pygame.draw.rect(self.screen, self.BLACK, text_rect, 2)

    def run(self):
        menu_active = True

        while menu_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.selected_option = (self.selected_option + 1) % len(self.menu_options)
                    if event.key == pygame.K_LEFT:
                        self.selected_option = (self.selected_option - 1) % len(self.menu_options)
                    if event.key == pygame.K_RETURN:
                        if self.selected_option == 0:  # Start
                            menu_active = False
                            # Call a function to start the game
                        elif self.selected_option == 1:  # Level
                            # Call a function to go to the level selection
                            pass
                        elif self.selected_option == 2:  # Options
                            # Call a function to open the options menu
                            pass

            self.draw_menu()
            pygame.display.flip()
            pygame.time.Clock().tick(self.FPS)

pygame.init()
# Example usage
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600

test_font = pygame.font.Font("font/VT323-Regular.ttf", 25)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
menu = PygameMenu(screen, ["Start", "Level", "Options"])
menu.run()
