import pygame


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 180

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


scroll = 0
ground_image = pygame.image.load(
    "Forest_tileset/Tiles/Objects/Sliced/obj_0011_Layer-12.png"
).convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []


for i in range(1, 5):
    bg_image = pygame.image.load(f"Forest_tileset/BG/{i}.png").convert_alpha()
    bg_images.append(bg_image)

bg_width = bg_images[0].get_width()


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