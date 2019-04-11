import pygame, pygame.freetype, os, sys
from objects import buttons, char, pizza, door
from game_states import start_menu, loss_screen, win_screen, char_select, spawn, first_hallway, adams_room, henrys_room
from pygame.locals import *

class Mixin:
    # Handles blitting and flipping
    def updateScreen(self, image, player, npcs, doors):
        self.screen.blit(image, (0,0))
        player.blitme()
        for npc in npcs:
          npc.blitme()
        for door in doors:
          door.blitme()
        pygame.display.set_caption("The Best Core Project, No Contest. HP: {}% Pizza Count: {}".format(self.health, self.counter))
        pygame.display.flip()
