import pygame
from hero import Player
from wave import Wave


pygame.init()

clock = pygame.time.Clock()
FPS = 60

#create game window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 180


#score 
score = 0
hi_score = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tsunami Rush")



#heroi = sprite('sprites/image 1.svg')
#heroi_grupo = pygame.sprite.Group()
#heroi_grupo.add(heroi)

test_font = pygame.font.Font('font/VT323-Regular.ttf',25)


##########################
#       PLAYER VAR       #
##########################
moving_sprites = pygame.sprite.Group()
player = Player(200,150)
moving_sprites.add(player)

##########################
#       WAVE VAR       #
##########################
moving_wave = pygame.sprite.Group()
wave = Wave(-18,1)
moving_wave.add(wave)



#define game variables
scroll = 0
ground_image = pygame.image.load("Forest_tileset/Tiles/Objects/Sliced/obj_0011_Layer-12.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []


for i in range(1, 5):
    bg_image = pygame.image.load(f"Forest_tileset/BG/{i}.png").convert_alpha()
    bg_images.append(bg_image)

bg_width = bg_images[0].get_width()

def draw_bg():
    for x in range(200):
      speed = 1
      for i in bg_images:
          screen.blit(i, ((x * bg_width) - scroll * speed, 0))
          speed += 0.2

def draw_ground():
    for x in range(200):
        screen.blit(ground_image, ((x * ground_width) - scroll * 1.0, SCREEN_HEIGHT - ground_height))


#heroi = pygame.image.load('sprites/image_1.png').convert_alpha()


#game loop
run = True
while run:

    clock.tick(FPS)

    #draw world
    draw_bg()
    draw_ground()
    #screen.blit(heroi,(100,SCREEN_HEIGHT - 40))
    moving_sprites.draw(screen)
    moving_sprites.update()

    #draw wave & update
    moving_wave.draw(screen)
    moving_wave.update()
    #get keypresses
    scroll += 1.5

    #event handlers
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_SPACE:
          player.is_jumping = True
    
    score += 0.02

    player.jump()
    placar = test_font.render('SCORE:' +str(int(score)),False,'Green')
    hi_placar = test_font.render('HI:' +str(int(hi_score)),False,'Green')

    screen.blit(placar,(450,20))
    screen.blit(hi_placar,(380,20))
    screen.blit(player.image,player.rect.topleft)
    
    pygame.display.update()

    #heroi_grupo.draw(screen)
pygame.quit()