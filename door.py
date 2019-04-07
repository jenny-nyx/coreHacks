import pygame, Controller

class Door():
  def __init__(self, screen, x, y):
    self.screen = screen
    self.image = pygame.image.load('images/door.png')
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y

  def blitme(self):
    self.screen.blit(self.image, self.rect)
