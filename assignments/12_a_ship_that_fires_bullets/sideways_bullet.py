
import pygame
from pygame.sprite import Sprite


class SidewaysBullet(Sprite):
    """Manage bullets that travel to the right."""

    def __init__(self, game):
        """Create a bullet at the ship's current position."""
        super().__init__()

        self.screen = game.screen
        self.color = (60, 60, 60)
        self.speed = 7

        # Create the bullet.
        self.rect = pygame.Rect(0, 0, 15, 5)

        # Start the bullet at the right side of the ship.
        self.rect.midleft = game.ship.rect.midright

        # Store the bullet's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet to the right."""
        self.x += self.speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet."""
        pygame.draw.rect(self.screen, self.color, self.rect)
