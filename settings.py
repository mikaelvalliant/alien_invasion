class Settings:
    """Classe qui stocke les paramètres du jeu."""

    def __init__(self):
        """Initialise les paramètres du jeu"""
        # Écran
        self.screen_width = 800
        self.screen_height = 531

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_color = (255, 0, 0)
        self.max_bullets = 5
