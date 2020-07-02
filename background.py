import pygame


class Background:
    """Gère l'image de fon du jeu."""

    def __init__(self, alien_invasion_game):

        self.screen = alien_invasion_game.screen
        self.screen_rect = alien_invasion_game.screen.get_rect()

        self.image = pygame.image.load('images/space_background.bmp')
        self.rect = self.image.get_rect()

        self.rect.topleft = self.screen_rect.topleft

    def blitme(self):
        """Dessine l'image de fond"""
        self.screen.blit(self.image, self.rect)
