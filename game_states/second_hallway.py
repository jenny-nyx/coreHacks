# Misc
import pygame, pygame.freetype, os, sys
import event_handler, updateScreen, collision
from pygame.locals import *
# Objects
from objects import buttons, char, pizza, door
# Game states
from game_states import start_menu, loss_screen, win_screen, char_select, \
spawn, first_hallway, adams_room, henrys_room, second_hallway, jordans_room, \
sams_room

class Mixin:
    # Second hallway state
    def secondHallway(self):
        # Create objects in room
        player = char.Char(self.screen, self.pick, 640, 575)
        backDoor = door.Door(self.screen, 640, 800)
        jordansDoor = door.Door(self.screen, 800, 500)
        samsDoor = door.Door(self.screen, 640, 200)
        npcs = []
        doors = [backDoor, jordansDoor, samsDoor]
        # Create game state
        while True:
            self.state = "second hallway"
            # Blit objects in room
            self.check_events(player)
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/secondhallway.png")), (self.height, self.width))
            player.update()
            self.updateScreen(image, player, npcs, doors)
            # Room logic
            if self.collide(player, backDoor) == True:
                self.firstHallway()
                return None
            elif self.collide(player, samsDoor) == True:
                if self.key3 == False:
                    pass
                elif self.key3 == True:
                    self.samsRoom()
                    return None
            elif self.collide(player, jordansDoor) == True:
                self.jordansRoom()
                return None
