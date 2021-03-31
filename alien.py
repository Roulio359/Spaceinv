from pygame import Vector2


class alien:
    def __init__(self):
        self.model1 = pygame.image.load('Model\big.gif')
        self.model2 = pygame.image.load('Model\med.gif')
        self.model3 = pygame.image.load('Model\sma.gif')
        self.vitesse = 30
        self.position = Vector2()

    def afficher(self):
        pass

    def deplacer(self):
        pass

    def tirer(self):
        pass
