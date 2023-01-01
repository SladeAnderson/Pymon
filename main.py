import pygame
import sys
from random import randint, choice
from player import PLayer
from obstacle import Obstacle

#  functions
def dis_score():
    global currentTime
    currentTime = pygame.time.get_ticks() - start_time

    currentTime = int(currentTime)
    seconds=(currentTime/1000)%60
    currentTime = seconds

    score_sur = test_font.render(f'score: {str(int(currentTime))}', False, (64,64,64))
    score_rect = score_sur.get_rect(topleft = (60,50))
    screen.blit(score_sur ,score_rect)

    return currentTime
    
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        return obstacle_list
    else:
        return []

def sprite_collisions():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        bg_Music.stop()
        return False
    else: 
        return True



#  important varables/ initializeing pygame / imports

pygame.init()
screen = pygame.display.set_mode((800,600))
from fps import FPS

fps = FPS()
clock = pygame.time.Clock()
test_font = pygame.font.Font('font\Pixeltype.ttf', 45)
game_active = False
Title_Screen_Active = False
real_title = True
start_time = 0
Score = 0
bg_Music = pygame.mixer.Sound('audio/music.wav')
bg_Music.play(loops = -1)
bg_Music.set_volume(0.6)








player = pygame.sprite.GroupSingle()
player.add(PLayer())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
ground_rect = ground_surface.get_rect(topleft = (0 ,300))

intro_text = test_font.render('Press Space to start and to jump', False, (64, 64 ,64))
intro_text_rect = intro_text.get_rect(center = (400,400))

Title_text = test_font.render('Welcome to Runner', False, (64, 64 ,64))
Title_text_rect = Title_text.get_rect(center = (400 ,200))

Title_text_two = test_font.render('Press space to start and to jump', False, (64, 64 ,64))
Title_text_two_rect = Title_text_two.get_rect(center = (400 ,300))


#  intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400 ,300))

# Timer
obstacle_timer = pygame.USEREVENT + 1 
pygame.time.set_timer(obstacle_timer, 1500)

#  snail animation timer
bad_guy_timer_1 = pygame.USEREVENT + 2
pygame.time.set_timer(bad_guy_timer_1, 500)

#  fly animation timer
bad_guy_timer_2 = pygame.USEREVENT + 3
pygame.time.set_timer(bad_guy_timer_2, 200)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if real_title:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    start_time = pygame.time.get_ticks()
                    game_active = True
                    real_title = False
                    Title_Screen_Active = False

        if game_active == False:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    print('game loading')
                    bg_Music.play()
                    bg_Music.set_volume(0.6)
                    start_time = pygame.time.get_ticks()
                    game_active = True
                    Title_Screen_Active = False

  


    #  update/fps stuff
    screen.fill((0, 0, 0,))
    fps.render(screen)    
    
    # 
    #game_active
    # 
    if game_active == True:
        
        if e.type == obstacle_timer:
            obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))

        screen.blit(ground_surface, ground_rect)
        screen.blit(sky_surface, (0 ,0))
        
        Score = dis_score()
        
        # player
        player.draw(screen)
        player.update()

        # bad guys
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        # collisions
        game_active = sprite_collisions()

        if game_active == False:
            Score = currentTime
            Title_Screen_Active = True
            real_title = False
        
    
    # 
    #Title_Screen_Active
    # 
    if Title_Screen_Active == True:
        screen.fill((94 ,129 ,162))
        screen.blit(player_stand, player_stand_rect)

        text_surface = test_font.render('Score: ' + str(Score) , False, (64,64,64))
        text_rect = text_surface.get_rect(midbottom = (400, 500))

        screen.blit(text_surface, text_rect)
        screen.blit(intro_text,intro_text_rect)

    if real_title:
        screen.fill(((94 ,129 ,162)))

        screen.blit(Title_text, Title_text_rect)
        screen.blit(Title_text_two, Title_text_two_rect)

    pygame.display.update()
    fps.clock.tick(60)
