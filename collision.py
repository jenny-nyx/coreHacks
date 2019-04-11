# Misc
import pygame, pygame.freetype, os, sys
from pygame.locals import *
# Objects
from objects import buttons, char, pizza, door
# Main class
import Controller

class Mixin:
    # Checks for collisions
    def collide(self, player, object):
        if player.rect.colliderect(object):
            return True
