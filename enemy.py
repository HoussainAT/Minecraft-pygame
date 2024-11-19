import pygame

from constants import FLOOR_HEIGHT, SCREEN_WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy.png")
        self.image = pygame.transform.scale(self.image, (135, 135))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + self.image.get_width()
        self.rect.y = FLOOR_HEIGHT

    def move(self):
        if self.rect.x > 0:
            self.rect.x -= 1
