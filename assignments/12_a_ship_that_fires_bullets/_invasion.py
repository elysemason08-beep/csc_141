
import pygame
class AlienInvasion: """Overall class to manage game assets and behavior."""
def __init__(self): """Initialize the game, and create game resources."""

1 pygame.init() 

2 self.screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Alien Invasion")
def run_game(self): """Start the main loop for the game."""
3 while True:
# Watch for keyboard and mouse events.
4 for event in pygame.event.get():
5 if event.type == pygame.QUIT:
sys.exit()
# Make the most recently drawn screen visible.
6 pygame.display.flip()
if __name__ == '__main__':
# Make a game instance, and run the game.
ai = AlienInvasion()
ai.run_game()