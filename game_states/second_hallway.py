# Misc
import pygame, pygame.freetype, os, sys, event_handler
from pygame.locals import *
# Objects
from objects import buttons, char, pizza, door
# Main class
import Controller


class Mixin:
    # Second hallway state
    def secondHallway(self):
        # Create objects in room
        player = char.Char(self.screen, self.pick, 640, 575)
        backDoor = door.Door(self.screen, 640, 800)
        jordansDoor = door.Door(self.screen, 750, 500)
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
