from pygame import Vector2


class alien:
    def __init__(self):
        self.model1 = pygame.image.load('.png')
        self.model2 = pygame.image.load('.png')
        self.model3 = pygame.image.load('.png')
        self.vitesse = 30
        self.position = Vector2()

    def afficher(self):
        pass

    def deplacer(self):
        pass

    def tirer(self):
        pass
