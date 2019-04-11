import pygame, Controller, random

class Pizza():
  def __init__(self, screen):
    self.screen = screen
    self.image = pygame.image.load('images/pizza.png')
    self.rect = self.image.get_rect()
    randx = random.randint(0, 1280)
    randy = random.randint(0, 800)
    self.rect.centerx = randx
    self.rect.centery = randy

  def blitme(self):
    self.screen.blit(self.image, self.rect)

