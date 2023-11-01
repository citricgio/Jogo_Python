import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('sprites/shark/image_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/shark/image_2.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/shark/image_3.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/shark/image_4.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/shark/image_5.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/shark/image_6.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/shark/image_7.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/shark/image_8.png').convert_alpha())


        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.mask = pygame.mask.from_surface(self.image)

        
    def animate(self):
        self.is_animating = True

    def update(self):
        self.current_sprite += 0.15
        self.rect.x -= 15
        if self.rect.x <= -10:
            self.rect.x = randint(1000,3050)

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        self.mask = pygame.mask.from_surface(self.image)
