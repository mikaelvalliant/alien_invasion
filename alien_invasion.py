import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Classe qui gère le jeu."""

    def __init__(self):
        """Initialise le jeu et gère les ressources."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run(self):
        """Boucle du jeu."""
        while True:
            # Gère les événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip()


if __name__ == '__main__':
    # Instance du jeu
    alien_invasion = AlienInvasion()
    alien_invasion.run()
