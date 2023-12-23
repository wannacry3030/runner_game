import pygame
from sys import exit
from random import randint

#definindo o score do jogo
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = reserve_font.render(f'Pontos: {current_time}',False,(151, 117, 166))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

#definindo movimentos dos objetos
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= obstacle_speed

            if obstacle_rect.bottom == 300:  screen.blit(raptor_surf,obstacle_rect)
            else: screen.blit(pterodactyl_surf,obstacle_rect)
            
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x >-100]
        
        return obstacle_list
    else: return []

#definindo colisões
def collisions(trex, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if trex.colliderect(obstacle_rect): return False
    return True

#definindo animações de movimento
def trex_animation():
    global trex_surf, trex_index

    if trex_rect.bottom <300:
        trex_surf = trex_jump
    else:
        trex_index += 0.1
        if trex_index >= len(trex_walk): trex_index =0
        trex_surf = trex_walk[int(trex_index)]
       
#definindo tamanho da tela, fonte, etc      
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('BloodKnight')
clock = pygame.time.Clock()
reserve_font = pygame.font.Font('Images/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
fase = 1
pygame.mixer.music.load('music/bg.mp3')
pygame.mixer.music.play(-1, 0.0)
obstacle_speed = 13

#sky
bg_surface = pygame.image.load('Images/bg.png').convert()
bg_surface1 = pygame.image.load('Images/bg1.png').convert()
bg_frames = [bg_surface, bg_surface1]
bg_frame_index = 0
bg_surf = bg_frames[bg_frame_index]
sky_x = 0
current_bg_surface = bg_surface

#chao
ground_surface = pygame.image.load('Images/JurassicGround.png').convert()
ground_x  = 0

# raptor
raptor_1 = pygame.image.load('Images/dog.png').convert_alpha()
raptor_2 = pygame.image.load('Images/dog1.png').convert_alpha()
raptor_3 = pygame.image.load('Images/dog2.png').convert_alpha()
raptor_frames = [raptor_1, raptor_2, raptor_3]
raptor_frame_index = 0
raptor_surf = raptor_frames[raptor_frame_index]

# pterodactyl
pterodactyl_1 = pygame.image.load('Images/fly.png').convert_alpha()
pterodactyl_2 = pygame.image.load('Images/fly1.png').convert_alpha()

pterodactyl_frames = [pterodactyl_1, pterodactyl_2]
pterodactyl_frame_index = 0
pterodactyl_surf = pterodactyl_frames[pterodactyl_frame_index]

obstacle_rect_list = []

#definindo animação de movimentação do personagem
trex_walk_1 = pygame.image.load('Images/TRex_Walk1.png').convert_alpha()
trex_walk_2 = pygame.image.load('Images/TRex_Walk2.png').convert_alpha()
trex_walk = [trex_walk_1, trex_walk_2]
trex_index = 0
trex_jump = pygame.image.load('Images/TRex_Jump2.png').convert_alpha()

trex_surf = trex_walk[trex_index]
trex_rect = trex_surf.get_rect(midbottom = (200,300))
trex_gravity = 0

#tela inicial
trex_stand = pygame.image.load('Images/TRex_Stand1.png').convert_alpha()
trex_stand = pygame.transform.rotozoom(trex_stand,0,2)
trex_stand_rect = trex_stand.get_rect(center = (400,200))

game_name = reserve_font.render('Runner', False, (151,117,166))
game_name_rect = game_name.get_rect(center = (400,80)) 

game_message = reserve_font.render('Aperte ESPACO para comecar', False, (151,117,166))
game_message_rect = game_name.get_rect(center = (340,340))

#timer dos objetos na tela
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

raptor_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(raptor_animation_timer, 10)

pterodactyl_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(pterodactyl_animation_timer, 10)

bg_animation_timer = pygame.USEREVENT + 4
pygame.time.set_timer(bg_animation_timer, 10) 

#loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and trex_rect.bottom >= 300: 
                    trex_gravity = -21
                    
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
   
        if game_active:
            # Verifica se é o momento de mudar para a segunda fase
            if score <= 10:
                fase = 1
                
            if score >= 10 and fase == 1:  
                fase = 2
                obstacle_speed = 15
            
            if score >= 20 and fase == 2:
                fase = 3 
                obstacle_speed = 17
                
            if score >= 30 and fase == 3:
                fase = 4
                obstacle_speed = 19
                    
   
        if game_active:
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(raptor_surf.get_rect(
                                        bottomright = (randint(900,1100), 300)))
                else:
                    obstacle_rect_list.append(pterodactyl_surf.get_rect(
                                        bottomright = (randint(900,1100), 150))) 
     
        
#ANIMAÇÕES
            if event.type == raptor_animation_timer:
                raptor_frame_index += 0.1
                if raptor_frame_index >= len(raptor_frames): 
                    raptor_frame_index = 0
                raptor_surf = raptor_frames[int(raptor_frame_index)]
                            
            if event.type == pterodactyl_animation_timer:
                pterodactyl_frame_index += 0.1
                if pterodactyl_frame_index >= len(pterodactyl_frames): 
                    pterodactyl_frame_index = 0
                pterodactyl_surf = pterodactyl_frames[int(pterodactyl_frame_index)]       
                
                
              
 #MOVIMENTAÇÃO DO CHAO E CEU
    if game_active:       
        ground_x -= 5
        if ground_x <= -ground_surface.get_width():
            ground_x = 0
            
    if game_active:
        sky_x -=5
        if sky_x <= -current_bg_surface.get_width():
            sky_x = 0
            

        
        for i in range(screen.get_width() // ground_surface.get_width() + 1):
            screen.blit(ground_surface, (ground_x + i * ground_surface.get_width(), 300))
            
            screen.blit(current_bg_surface, (sky_x,0))
            screen.blit(current_bg_surface, (sky_x + current_bg_surface.get_width(),0))
            score = display_score()
        
        #T Rex
        trex_gravity += 1
        trex_rect.y += trex_gravity
        if trex_rect.bottom >= 300: trex_rect.bottom = 300
        trex_animation()
        screen.blit(trex_surf, trex_rect)
        
        #Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        #Collision
        game_active = collisions(trex_rect, obstacle_rect_list)

#tela de game over
    else:
        screen.fill((26, 33, 41))
        screen.blit(trex_stand, trex_stand_rect)
        obstacle_rect_list.clear()
        trex_rect.midbottom = (200,300)
        trex_gravity = 0
      
        score_message = reserve_font.render(f'Seus pontos: {score}', False, (151, 117, 166))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_name,game_name_rect)
                
        if score == 0: screen.blit(game_message,game_message_rect)
        else: screen.blit(score_message, score_message_rect)
        
   
    

        
    pygame.display.update()
    clock.tick(60) 