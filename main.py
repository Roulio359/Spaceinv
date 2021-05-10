import random

import pygame
from pygame import draw, Vector2

from pygame.examples.pixelarray import show

import canon
import core
from alien import Alien
from rocket import Rocket

drops = []
rocket = None
alien = Alien()
xalien = 180
canon = canon.Canon()

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 500]
    print("Setup END-----------")


    for i in range(0, 1000):
        drops.append(Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(-400, 0)))


def run():
    global rocket
    #affichage
    model1 = pygame.image.load('Model/sma.gif').convert()
    model2 = pygame.image.load('Model/med.gif').convert()
    model3 = pygame.image.load('Model/big.gif').convert()
    modelcanon = pygame.image.load("Model/canon.png").convert()
    alien.afficher(core.screen, model1, model2, model3, xalien)
    if rocket != None:
        rocket.afficher(core.screen, None)
    canon.Apparaitre(core.screen, modelcanon)
    #clavier
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if rocket==None:
            rocket = Rocket()
            rocket.position.x = canon.position.x + 14
            rocket.position.y = canon.position.y
    if keys[pygame.K_RIGHT]:
        canon.position.x = canon.position.x + 10 if canon.position.x < 720 else 720
    if keys[pygame.K_LEFT]:
        canon.position.x = canon.position.x - 10 if canon.position.x > 50 else 50

    #deplacement
    if rocket != None:
        rocket.deplacement()
        if rocket.position.y < 0:
            rocket = None
    alien.checkCollision()

if __name__ == '__main__':
    core.main(setup, run)
