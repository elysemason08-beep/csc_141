import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image.
        self.image = pygame.image.load(
            'assignments/12_a_ship_that_fires_bullets/images/character.png'
        )

        self.rect = self.image.get_rect()

        # Position the ship on the left side.
        self.rect.midleft = self.screen_rect.midleft

        # Store a float for the ship's vertical position.
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Move the ship up and down."""

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship vertically."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)