import pygame
import Controller
import dictionaries

class Char():
  def __init__(self, screen, char):
    self.screen = screen
    self.strength = dictionaries.char_strengths[char]
    self.real_weakness = dictionaries.char_weaknesses[char][0]
    self.fake_weakness = dictionaries.char_weaknesses[char][1]
    image = dictionaries.char_image[char]

    self.image = pygame.image.load(image)
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

    self.moving_right = False
    self.moving_left = False

  def blitme(self):
    self.screen.blit(self.image, self.rect)

  def update(self):
    if self.moving_right:
      self.rect.centerx += 25
    if self.moving_left:
      self.rect.centerx -= 25
