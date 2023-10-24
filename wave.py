import pygame

class Wave(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('sprites/WAVE/image_0.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/WAVE/image_1.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/WAVE/image_2.png').convert_alpha())
        self.sprites.append(pygame.image.load('sprites/WAVE/image_3.png').convert_alpha())

        self.current_sprite = 0.0
        self.image = self.sprites[int(self.current_sprite)]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating == True

    def update(self):
        self.current_sprite += 0.05
    
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
