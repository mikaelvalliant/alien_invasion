import pygame


class Ship:
    """Gère le vaisseau spatial"""

    def __init__(self, alien_invasion_game):
        """Initialise le vaisseau et le place à son emplacement initial."""
        self.screen = alien_invasion_game.screen
        self.screen_rect = alien_invasion_game.screen.get_rect()

        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Dessine le vaisseau à un endroit précis."""
        self.screen.blit(self.image, self.rect)