import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    """Classe qui gère les balles tirées."""

    def __init__(self, alien_invasion_game):
        """"Créé une balle lancée à partir de la position courante du vaisseau."""
        super().__init__()
        self.screen = alien_invasion_game.screen
        self.settings = alien_invasion_game.settings
        self.color = self.settings.bullet_color

        # Créer un rectangle de balle à (0,0) et ensuite corriger la position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = alien_invasion_game.ship.rect.midtop

        # Mémorise la position de la balle tirée.
        self.y = float(self.rect.y)

    def update(self):
        """Déplacement vers le haut."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Dessine la ballr sur l'écran de jeu."""
        pygame.draw.rect(self.screen, self.color, self.rect)
