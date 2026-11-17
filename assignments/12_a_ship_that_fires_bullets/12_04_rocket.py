# IM LOSING MY MINDDD




import pygame
import sys

class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load("assignments/12_a_ship_that_fires_bullets/images/character.png")
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.speed = 2

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def draw_rocket(self):
        self.screen.blit(self.image, self.rect)


pygame.init()

screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Rocket")

rocket = Rocket(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = True
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = True
            elif event.key == pygame.K_UP:
                rocket.moving_up = True
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = False
            elif event.key == pygame.K_UP:
                rocket.moving_up = False
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = False

    rocket.update()

    screen.fill((230, 230, 230))
    rocket.draw_rocket()

    pygame.display.flip()
