import pygame, os

class Button(pygame.sprite.Sprite):
    def __init__(self, name, coords, filename):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load(os.path.join(os.getcwd(),filename)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.topleft = coords
