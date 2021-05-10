

from pygame import Vector2


class Alien:
    def __init__(self):

        self.vitesse = 0
        self.position = Vector2()


    def afficher(self, screen, model1, model2, model3, xalien):

        for i in range(11):
            screen.blit(model1, (xalien, 50))
            screen.blit(model2, (xalien, 100))
            screen.blit(model2, (xalien, 150))
            screen.blit(model3, (xalien, 200))
            screen.blit(model3, (xalien, 250))
            xalien = xalien + 40
    def checkCollision(self, game):

    def deplacer(self):
        pass

    def tirer(self):
        pass
