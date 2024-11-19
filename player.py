import pygame
from constants import FLOOR_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/player.png")
        self.image =  pygame.transform.scale(self.image, (135, 135))
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH / 2) - self.image.get_width() / 2
        self.rect.y = FLOOR_HEIGHT

    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= 1
    def move_down(self):
        if self.rect.y < 475:
            self.rect.y += 1
    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= 1
    def move_right(self):
        if self.rect.x < 940:
            self.rect.x += 1
