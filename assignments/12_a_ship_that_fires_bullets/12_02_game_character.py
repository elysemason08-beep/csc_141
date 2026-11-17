
import pygame
import sys
# I got help with this aye ! 

class GameCharacter:
    def __init__(self, screen):
        self.screen = screen

        # Load the character image
        self.image = pygame.image.load("character.png")

        # Resize the image
        self.image = pygame.transform.scale(
            self.image, (300, 450)  )        

        # Get the rectangle around the image
        self.rect = self.image.get_rect()

        # Put the character in the center
        self.rect.center = screen.get_rect().center

    def draw_character(self):
        self.screen.blit(self.image, self.rect)


# Start Pygame
pygame.init()

# Create the game screen
screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("My Game Character")

# Create the character
character = GameCharacter(screen)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Background color
    screen.fill((230, 230, 230))

    # Display the character
    character.draw_character()

    pygame.display.flip()
