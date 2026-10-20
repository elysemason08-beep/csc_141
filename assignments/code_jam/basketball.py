''''''


import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480))
my_image = pygame.image.load("code_jam/media/basketball.png").convert_alpha()
image_rect = my_image.get_rect(center=(320,240))




screen = pygame.display.set_mode((1900,1050))
                                  
                                  
running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False


    screen.fill((100,200,150))
    screen.blit(my_image, image_rect)
    pygame.display.flip() 
