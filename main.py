import random

from pygame import draw, Vector2
from pygame.examples.pixelarray import show

import core
from rocket import Rocket

drops = []
rocket = Rocket()


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    print("Setup END-----------")


    for i in range(0, 1000):
        drops.append(Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(-400, 0)))


def run():
    #affichage
    rocket.afficher(core.screen,None)

    #clavier


    #deplacement
    rocket.deplacement()


if __name__ == '__main__':
    core.main(setup, run)
