import pygame
from pygame.math import Vector2

from alien import alien


class Rocket:
    def __init__(self):
        #self.model = pygame.image.load('.png')
        self.vitesse = 3
        self.position = Vector2(200,200)

    def afficher(self,fenetre, alien):
        if self.colliderect(alien):
            self.vitesse = 0
        if self.position.y >= 0:
            pygame.draw.rect(fenetre, (254, 52, 110), pygame.Rect(self.position.x, self.position.y, 2, 4))

    def deplacement(self):
        self.position.y = self.position.y - self.vitesse
        if self.position.y <= 0:
            self.vitesse = 0

    def colliderect(self,alien):
        pass
