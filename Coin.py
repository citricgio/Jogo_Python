import pygame
from random import randint

class Coin(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('sprites/GoldCoinSprite/Coin1.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/GoldCoinSprite/Coin2.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/GoldCoinSprite/Coin3.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/GoldCoinSprite/Coin4.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/GoldCoinSprite/Coin5.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/GoldCoinSprite/Coin6.png').convert_alpha())

        self.current_sprite = 0.0
        self.image = self.sprites[int(self.current_sprite)]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        
    def animate(self):
        self.is_animating == True

    def update(self):
        self.current_sprite += 0.15
        self.rect.x -= 5
        if self.rect.x <= 0:
            self.rect.x = randint(1000,3050)

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]