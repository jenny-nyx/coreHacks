import pygame
import Controller

class Char():
  def __init__(self, screen, strength, weakness, blessing):
    self.screen = screen
    self.strength = strength
    self.weakness = weakness
    self.blessing = blessing

    self.image = pygame.image.load('char.png')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

  def blitme(self):
    self.screen.blit(self.image, self.rect)