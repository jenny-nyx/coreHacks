import pygame, pygame.freetype, os, sys
from objects import buttons, char, pizza, door
from game_states import start_menu, loss_screen, win_screen, char_select, spawn, first_hallway, adams_room, henrys_room
from pygame.locals import *

class Mixin:
    # Checks for collisions
    def collide(self, player, object):
        if player.rect.colliderect(object):
            return True
