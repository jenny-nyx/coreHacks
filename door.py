import pygame, Controller

class Door():
  def __init__(self, screen):
    self.screen = screen
    self.image = pygame.image.load('images/door.png')
    self.rect = self.image.get_rect()
    self.rect.centerx = 0
    self.rect.centery = 0

  def blitme(self):
    self.screen.blit(self.image, self.rect)
