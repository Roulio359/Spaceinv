import random

import pygame
from pygame import draw, Vector2

from pygame.examples.pixelarray import show

import core
from alien import Alien
from rocket import Rocket

drops = []
rocket = Rocket()
alien = Alien()
xalien = 180


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 500]
    print("Setup END-----------")


    for i in range(0, 1000):
        drops.append(Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(-400, 0)))


def run():
    #affichage
    rocket.afficher(core.screen, alien)
    model1 = pygame.image.load('Model/sma.gif').convert()
    model2 = pygame.image.load('Model/med.gif').convert()
    model3 = pygame.image.load('Model/big.gif').convert()
    alien.afficher(core.screen, model1, model2, model3, xalien)
    rocket.afficher(core.screen, None)
    modelcanon = pygame.image.load("Model/canon.png").convert()
    canon.apparaitre(core.screen, modelcanon)
    #clavier
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        rocket.position.x = canon.position.x + 14
        rocket.position.y = canon.position.y
    if keys[pygame.K_RIGHT]:
        canon.position.x = canon.position.x + 20 if canon.position.x < 720 else 720
    if keys[pygame.K_LEFT]:
        canon.position.x = canon.position.x - 20 if canon.position.x > 50 else 50

    #deplacement
    rocket.deplacement()


if __name__ == '__main__':
    core.main(setup, run)
