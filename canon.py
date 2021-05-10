import pygame
from pygame.math import Vector2

from pygame import Vector2
from pygame import Vector3

class Canon:
    def __init__(self):
        #self.modelcanon = pygame.image.load('Model/canon.png')
        self.vitesse = 0
        self.position = Vector2(400, 450)
        self.direction = Vector2()
        self.couleur = Vector3()
        self.pointdevie = 3

    def Apparaitre(self, screen, modelcanon):
        screen.blit(modelcanon, self.position)


