
import pygame


class SidewaysShip:
    """Manage the ship in the sideways shooter game."""

    def __init__(self, game):
        """Initialize the ship and set its starting position."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the character image.
        self.image = pygame.image.load(
            'assignments/12_a_ship_that_fires_bullets/images/character.png'
        )
        self.rect = self.image.get_rect()

        # Start the ship on the left side, vertically centered.
        self.rect.midleft = self.screen_rect.midleft

        # Store the ship's exact vertical position.
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_up = False
        self.moving_down = False

        self.speed = 4

    def update(self):
        """Move the ship up or down."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        self.rect.y = self.y

    def blitme(self):
        """Draw the ship."""
        self.screen.blit(self.image, self.rect)
