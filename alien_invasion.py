import sys

import pygame

from settings import Settings
from ship import Ship
from background import Background
from bullets import Bullets


class AlienInvasion:
    """Classe qui gère le jeu."""

    def __init__(self):
        """Initialise le jeu et gère les ressources."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.background = Background(self)

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

    def run(self):
        """Boucle du jeu."""
        while True:

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    self.check_keyup_events(event)
                if event.type == pygame.KEYDOWN:
                    self.check_keydown_events(event)
                elif event.type == pygame.QUIT:
                    sys.exit()
            self.ship.update()
            self.bullets.update()

            self.update_bullets()

            self.update_screen()

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def update_screen(self):
        """Met à jour les images affichées et flip au prochain écran."""
        self.background.blitme()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

    def fire_bullet(self):
        """Créé une nouvelle balle et la lance."""
        if len(self.bullets) < self.settings.max_bullets:
            new_bullet = Bullets(self)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        """Efface les balles qui sortent du cadre du jeu. """
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


if __name__ == '__main__':
    # Instance du jeu
    alien_invasion = AlienInvasion()
    alien_invasion.run()
