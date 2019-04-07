import pygame
import Controller
import dictionaries

class Char():
  def __init__(self, screen, char, x, y):
    self.screen = screen
    self.strength = dictionaries.char_strengths[char]
    self.real_weakness = dictionaries.char_weaknesses[char][0]
    self.fake_weakness = dictionaries.char_weaknesses[char][1]
    image = dictionaries.char_image[char]

    self.image = pygame.image.load(image)
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    self.rect.centerx = x
    self.rect.centery = y

    self.moving_right = False
    self.moving_left = False
    self.moving_up = False
    self.moving_down = False

  def blitme(self):
    self.screen.blit(self.image, self.rect)

  def update(self):
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.rect.centerx += 25
    if self.moving_left and self.rect.left > 0:
      self.rect.centerx -= 25
    if self.moving_up and self.rect.top > 0:
      self.rect.centery -= 25
    if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
      self.rect.centery += 25
