import pygame
pygame.init()

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

# Loading images
bg_imgs = [pygame.image.load(f'Images/bg{i}.png') for i in range(2)]
ground_img = pygame.image.load('Images/JurassicGround.png').convert()
p_imgs = [pygame.image.load(f'Images/p{p}.png') for p in range(2)]
p_jump = pygame.image.load('Images/pjump.png').convert()

# Position and state variables
jumping = False
p = 0
px = 50
py = 170
jump_count = 10
gx = 0
x = 0
i = 0

# Animation variables
animation_counter = 0
animation_speed = 30  # Update every 30 frames (60 FPS / 30 = 2 FPS)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            py -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10

    # Update animations at a lower rate
    animation_counter += 1
    if animation_counter >= animation_speed:
        p += 1
        p = p % len(p_imgs)
        i += 1
        i = i % len(bg_imgs)
        animation_counter = 0  # Reset the counter after updating animations

    # Display elements on the screen
    screen.blit(bg_imgs[i], (x, 0))
    screen.blit(ground_img, (0, 300))
    screen.blit(p_imgs[p], (px, py))
    pygame.display.update()
    clock.tick(30)  # Maintain the game running at 60 FPS

pygame.quit()
