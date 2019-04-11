# Misc
import pygame, pygame.freetype, os, sys, event_handler
from pygame.locals import *
# Objects
from objects import buttons, char, pizza, door
# Main class
import Controller


class Mixin:
    # First hallway state
    def firstHallway(self):
        # Create objects in room
        player = char.Char(self.screen, self.pick, 640, 575)
        backDoor = door.Door(self.screen, 640, 800)
        adamDoor = door.Door(self.screen, 400, 320)
        partyDoor = door.Door(self.screen, 850, 320)
        nextDoor = door.Door(self.screen, 640, 0)
        npcs = []
        doors = [backDoor, adamDoor, partyDoor, nextDoor]
        # Create game state
        while True:
            self.state = "first hallway"
            # Blit objects in room
            self.check_events(player)
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/hallway.png")), (self.height, self.width))
            player.update()
            self.updateScreen(image, player, npcs, doors)
            # Room logic
            if self.collide(player, backDoor) == True:
                self.spawnRoom(640, 400)
                return None
            elif self.collide(player, adamDoor) == True:
                self.adamRoom()
                return None
            elif self.collide(player, partyDoor) == True:
                self.henryRoom()
                return None
            elif self.collide(player, nextDoor) == True:
                if self.key1 == True and self.key2 == True:
                    self.secondHallway()
                    return None
                elif self.key1 == False or self.key2 == False:
                    lock_txt = self.baseFont.render("CANT PASS: HALLWAY SQUAD IN THE WAY", True, (0,0,0))
                    lock_txt_rect = lock_txt.get_rect()
                    lock_txt_rect.top = 100
                    lock_txt_rect.right = 850
                    self.screen.blit(lock_txt, lock_txt_rect)
                    pygame.display.flip()
