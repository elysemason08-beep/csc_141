#Ciani Mason

# Ciani Mason
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create the bullet.
        self.rect = pygame.Rect(
            0, 0,
            self.settings.bullet_width,
            self.settings.bullet_height
        )

        # Position the bullet at the right side of the ship.
        self.rect.midleft = ai_game.ship.rect.midright

        # Store the bullet's position as a float.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet to the right."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
