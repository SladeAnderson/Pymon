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
text_surface = test_font.render('Score: ' , False, 'black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600
snail_y_pos = 250

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
# player_rect = player_surface.get_rect(bottom = (80,200))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill((0, 0, 0,))
    fps.render(screen)    
    
    screen.blit(ground_surface, (0, 300))
    screen.blit(sky_surface, (0 ,0))
    screen.blit(text_surface, (80, 70))
    snail_x_pos -= 3
    
    if snail_x_pos < -80:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos ,snail_y_pos))
    # screen.blit(player_surface, player_rect)

    pygame.display.update()
    fps.clock.tick(60)
