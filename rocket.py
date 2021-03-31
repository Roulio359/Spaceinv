import pygame
from pygame.math import Vector2

class Rocket:
    def __init__(self):
        #self.model = pygame.image.load('.png')
        self.vitesse = 6
        self.position = Vector2(200,450)

    def afficher(self,screen, alien):
        if self.position.y != 0:
            if self.colliderect(alien):
                self.vitesse = 3
            if self.position.y >= 0:
                pygame.draw.rect(screen, (123, 52, 110), pygame.Rect(self.position.x, self.position.y,2 , 6))

    def deplacement(self):
        self.position.y = self.position.y - self.vitesse


    def colliderect(self,alien):
        pass
