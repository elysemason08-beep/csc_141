
import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
       
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        # Set the background color.
        self.bg_color = (0,100,100)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    self.ship.update()
                elif event.type == pygame.KEYDOWN:
                  self._check_keydown_events(event)
                  if event.key == pygame.K_RIGHT:
                     self.ship.moving_right = True
                     self._check_keyup_events(event)
                  elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                # Move the ship to the right.
                    self.ship.rect.x += 1


                    def _check_keydown_events(self, event):
                        """Respond to keypresses."""

                  self.ship.moving_right = True
                elif event.key == pygame.K_q:
                 sys.exit()
                elif event.type == pygame.KEYUP:

                        def _check_keyup_events(self, event):
                          """Respond to key releases."""

                if event.key == pygame.K_RIGHT:
                   self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                   self.ship.moving_left = False

            # Redraw the screen during each pass through the loop.
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()

            # Make the most recently drawn screen visible.
    pygame.display.flip()
    self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
    












# class AlienInvasion:
#     """Overall class to manage game assets and behavior."""

#     def __init__(self):
#         """Initialize the game, and create game resources."""
#         pygame.init()
#         self.screen = pygame.display.set_mode((1200, 800))
#         pygame.display.set_caption("Alien Invasion")

#         # Set the background color.
#         self.bg_color = (135, 206, 250)

#     def run_game(self):
#         """Start the main loop for the game."""
#         while True:
#             # Watch for keyboard and mouse events.
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()

#             # Redraw the screen during each pass through the loop.
#             self.screen.fill(self.bg_color)

#             # Make the most recently drawn screen visible.
#             pygame.display.flip()


# if __name__ == '__main__':
#     ai = AlienInvasion()
#     ai.run_game()
