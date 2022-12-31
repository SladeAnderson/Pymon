import pygame
import sys
from random import randint

def dis_score():
    global currentTime
    currentTime = pygame.time.get_ticks() - start_time

    currentTime = int(currentTime)
    seconds=(currentTime/1000)%60
    currentTime = seconds

    score_sur = test_font.render(f'score: {str(int(currentTime))}', False, (64,64,64))
    score_rect = score_sur.get_rect(topleft = (60,50))
    screen.blit(score_sur ,score_rect)
    
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

            

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []
        

pygame.init()
screen = pygame.display.set_mode((800,600))
from fps import FPS
fps = FPS()
clock = pygame.time.Clock()
test_font = pygame.font.Font('font\Pixeltype.ttf', 45)
game_active = False
Title_Screen_Active = True
start_time = 0
Score = 0

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
ground_rect = ground_surface.get_rect(topleft = (0 ,300))

intro_text = test_font.render('Welcome to my game press space to start.', False, (64, 64 ,64))
intro_text_rect = intro_text.get_rect(center = (400,400))


# bad guys
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

fly_surf = pygame.image.load('graphics/fly/fly1.png').convert_alpha()

obstacle_rect_list = []


player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(bottomleft = (80,300))
player_gravity = 0
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400 ,300))


# Timer
obstacle_timer = pygame.USEREVENT + 1 
pygame.time.set_timer(obstacle_timer, 1500)


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active == False:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    print('game loading')
                    start_time = pygame.time.get_ticks()
                    game_active = True
                    Title_Screen_Active = False

        if game_active == True:            
            if player_rect.bottom >= 300:
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_SPACE:
                        print('pressed')
                        player_gravity = -20 
        
        if e.type == obstacle_timer and game_active:
             if randint(0, 2):
                obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900,1100), 300)))
             else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100), 80)))
    screen.fill((0, 0, 0,))
    fps.render(screen)    
    

    if game_active == True:
        screen.blit(ground_surface, ground_rect)
        screen.blit(sky_surface, (0 ,0))

        Score = dis_score()
        
        # if snial_rect.left < -80:
        #     snial_rect.right = 900
        # screen.blit(snail_surface, snial_rect)
        # snial_rect.left -= 5    
        


        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # bad guy movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)



        #collision
         
 
    #     if snial_rect.colliderect(player_rect):
    #         game_active = False
    #         snial_rect.right = 700
    #         Score = currentTime
    #         print (Score)
    # else:
    #     Title_Screen_Active = True

    if Title_Screen_Active == True:
        screen.fill((94 ,129 ,162))
        screen.blit(player_stand, player_stand_rect)

        text_surface = test_font.render('Score: ' + str(Score) , False, (64,64,64))
        text_rect = text_surface.get_rect(midbottom = (400, 500))

        screen.blit(text_surface, text_rect)
        screen.blit(intro_text,intro_text_rect)



    # if player_rect.colliderect(snial_rect):
    #     print('has collided')
    #     print('------------')



    pygame.display.update()
    fps.clock.tick(60)
