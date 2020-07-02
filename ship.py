import pygame

from settings import Settings

class Ship:
    """Gère le vaisseau spatial"""

    def __init__(self, alien_invasion_game):
        """Initialise le vaisseau et le place à son emplacement initial."""
        self.settings = alien_invasion_game.settings

        self.screen = alien_invasion_game.screen
        self.screen_rect = alien_invasion_game.screen.get_rect()

        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # Mémorise la position en x du vaisseau spatial
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Met à jour la position du vaisseau spatial."""
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # Mise à jour de la position de l'objet.
        self.rect.x = self.x

    def blitme(self):
        """Dessine le vaisseau à un endroit précis."""
        self.screen.blit(self.image, self.rect)