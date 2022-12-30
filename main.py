import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))

from fps import FPS

fps = FPS()
clock = pygame.time.Clock()
test_font = pygame.font.Font('font\Pixeltype.ttf', 45)

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('Score: ' , False, 'white')
text_rect = text_surface.get_rect(midbottom = (60, 50))


snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snial_rect = snail_surface.get_rect(bottomleft = (600 ,300))


player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(bottomleft = (80,300))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

        # if e.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint((e.pos)):
        #         print('colided')
    screen.fill((0, 0, 0,))
    fps.render(screen)    
    
    screen.blit(ground_surface, (0, 300))
    screen.blit(sky_surface, (0 ,0))
    pygame.draw.rect(screen, 'black', text_rect)
    pygame.draw.rect(screen, 'black', text_rect,10)
    screen.blit(text_surface, text_rect)
    pygame.draw.line(screen, 'red', (0,0),pygame.mouse.get_pos(),2)
    
    if snial_rect.left < -80:
        snial_rect.right = 900
    screen.blit(snail_surface, snial_rect)
    snial_rect.left -= 2
    player_rect.left
    screen.blit(player_surface, player_rect)

    # if player_rect.colliderect(snial_rect):
    #     print('has collided')
    #     print('------------')



    pygame.display.update()
    fps.clock.tick(60)
