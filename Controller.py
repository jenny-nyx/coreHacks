# Misc
import pygame, pygame.freetype, os, sys, event_handler
from pygame.locals import *
# Objects
from objects import buttons, char, pizza, door
# Game states
from game_states import start_menu, loss_screen, win_screen, char_select, \
spawn, first_hallway, adams_room, henrys_room, second_hallway, jordans_room, \
sams_room


class Controller(event_handler.Mixin, start_menu.Mixin, loss_screen.Mixin,
                 win_screen.Mixin, char_select.Mixin, spawn.Mixin,
                 first_hallway.Mixin, adams_room.Mixin, henrys_room.Mixin,
                 second_hallway.Mixin, jordans_room.Mixin, sams_room.Mixin):

    def __init__(self, height=1280, width=800):
        # Initialize caption
        pygame.display.set_caption("The Best Core Project, No Contest")
        # Attributes/Variables
        self.pick = ''
        self.counter = 0
        self.health = 100
        self.key1 = False
        self.key2 = False
        self.key3 = False
        self.answer = ''
        self.check = ''
        self.state = ''
        # Display settings
        self.height = height
        self.width = width
        self.baseFont = pygame.font.SysFont(None, 30)
        self.screen = pygame.display.set_mode((self.height, self.width))
        # Start menu buttons
        self.start_buttons = pygame.sprite.Group()
        self.startButton = buttons.Button('startButton', (220, 450),
                                          "images/startButton.png")
        self.quitButton = buttons.Button('helpButton', (700, 450),
                                         "images/quitButton.png")
        self.start_buttons.add(self.startButton)
        self.start_buttons.add(self.quitButton)
        # Character select buttons
        self.char_buttons = pygame.sprite.Group()
        self.girl_button = buttons.Button('girl_button', (220, 450),
                                          "images/girl.png")
        self.boy_button = buttons.Button('boy_button', (700, 450),
                                         'images/boy.png')
        self.char_buttons.add(self.girl_button)
        self.char_buttons.add(self.boy_button)

    # Handles blitting and flipping
    def updateScreen(self, image, player, npcs, doors):
        self.screen.blit(image, (0, 0))
        player.blitme()
        for npc in npcs:
            npc.blitme()
        for door in doors:
            door.blitme()
        pygame.display.set_caption("The Best Core Project, No Contest. HP: " +
                                   "{}% Pizza Count: {}".format(self.health,
                                                                self.counter))
        pygame.display.flip()

    # Checks for collisions
    def collide(self, player, object):
        if player.rect.colliderect(object):
            return True
