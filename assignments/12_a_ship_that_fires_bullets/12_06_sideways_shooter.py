
import sys
import pygame

from sideways_ship import SidewaysShip
from sideways_bullet import SidewaysBullet


class AlienInvasion:
    """Overall class to manage the sideways shooter."""

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 700))
        pygame.display.set_caption("Sideways Shooter")

        self.ship = SidewaysShip(self)
        self.bullets = pygame.sprite.Group()

        self.bg_color = (0, 100, 100)

    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()

            self.ship.update()
            self.bullets.update()

            # Remove bullets that leave the screen.
            for bullet in self.bullets.copy():
                if bullet.rect.left >= self.screen.get_rect().right:
                    self.bullets.remove(bullet)

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
                elif event.key == pygame.K_q:
                    sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a bullet and add it to the group."""
        new_bullet = SidewaysBullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Redraw the screen."""
        self.screen.fill(self.bg_color)

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
