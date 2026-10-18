import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('Assets/images/ship.png')
        self.image = pygame.transform.scale(self.image, (90,62))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 100

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)