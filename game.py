from player import Player
from enemy import Enemy
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

class Game:
    def __init__(self):
        # fenetre du jeu
        self.screen = pygame.display.set_mode((1080 ,720))

        # Window name
        pygame.display.set_caption("mon premier jeu")

        # Pour charger l'image de fond
        self.background = pygame.image.load("assets/images/bg.jpg")

        # Compteure de points
        self.score = 0
        self.gameFont = pygame.font.SysFont("Verdana", 55)
        self.gameText = self.gameFont.render(f'Score : {self.score}', True, (255, 255, 255))

        # Charger image du joueur
        self.player = Player()
        self.enemy = Enemy()

        self.started = True

    def movements(self):
        self.check_collision()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and not self.check_collision():
            self.player.move_right()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_UP]:
            self.player.move_up()
        if keys[pygame.K_DOWN]:
            self.player.move_down()

    def check_collision(self):
            if self.player.rect.colliderect(self.enemy.rect):
                self.enemy.rect.x = SCREEN_WIDTH + self.enemy.image.get_width()
                self.score += 1
                self.gameText = self.gameFont.render(f'Score {self.score}', True,'red')

    def run(self):
        while self.started:
            # changer la couleur de fond
            self.screen.blit(self.background, (0, -400))

            # ajouter le score
            self.screen.blit(self.gameText, (50, 50))

            # ajouter joueur
            self.screen.blit(self.player.image, self.player.rect)

            self.screen.blit(self.enemy.image, self.enemy.rect)

            # ajouter ennemi
            self.movements()
            self.enemy.move()

            # actualiser l'ecran
            pygame.display.flip()
            # parcourir liste evevenement
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Game Stopped")
                    self.started = False
                    pygame.quit()
