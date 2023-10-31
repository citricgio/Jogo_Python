import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.is_jumping = False
        self.jumping_height = 8
        self.sprites.append(pygame.image.load('sprites/hero/image_1.png'))
        self.sprites.append(pygame.image.load('sprites/hero/image_2.png'))
        self.sprites.append(pygame.image.load('sprites/hero/image_3.png'))
        self.sprites.append(pygame.image.load('sprites/hero/image_4.png'))
        self.jump_vel = 8.5
        self.jump_sprites = []
        self.jump_sprites.append(pygame.image.load('sprites/hero/image_5.png'))
        self.jump_sprites.append(pygame.image.load('sprites/hero/image_6.png'))

        #self.sprites.append(pygame.image.load('sprites/image_5.png'))
        #self.sprites.append(pygame.image.load('sprites/image_6.png'))
    

        self.current_sprite = 0.0
        self.image = self.sprites[int(self.current_sprite)]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        
    def animate(self):
        self.is_animating == True

    def update(self):
        self.current_sprite += 0.12
    
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]


    
    def jump(self):
        # Check if mario is jumping and then execute the
        # jumping code.

        if self.is_jumping:
            self.image = self.jump_sprites[0]
            self.rect.y -= self.jump_vel * 2.5
            self.jump_vel -= 0.45
        
        if self.jump_vel <= 0:
            self.image = self.jump_sprites[1]

        if self.jump_vel < -8.5:
            self.rect.y = 500
            self.is_jumping = False
            self.jump_vel = 8.5
