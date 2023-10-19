import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.is_jumping = False
        self.jumping_height = 10
        self.sprites.append(pygame.image.load('sprites/image_1.png'))
        self.sprites.append(pygame.image.load('sprites/image_2.png'))
        self.sprites.append(pygame.image.load('sprites/image_3.png'))
        self.sprites.append(pygame.image.load('sprites/image_4.png'))
        #self.sprites.append(pygame.image.load('sprites/image_5.png'))
        #self.sprites.append(pygame.image.load('sprites/image_6.png'))
        
        # Additional attributes for jumping
        self.jump_pixels = 0
        self.jump_power = 10    

        self.current_sprite = 0.0
        self.image = self.sprites[int(self.current_sprite)]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        
    def animate(self):
        self.is_animating == True

    def update(self):
        self.current_sprite += 0.15
    
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]


    
    def jump(self):
        # Check if mario is jumping and then execute the
        # jumping code.
        if self.is_jumping:
            if self.jumping_height >= -10:
                neg = 1
                if self.jumping_height < 0:
                    neg = -1
                self.rect.y -= self.jumping_height**2 * 0.3 * neg
                self.jumping_height -= 1
            else:
                self.is_jumping = False
                self.rect.y=150
                self.jumping_height = 10