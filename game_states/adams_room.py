# Misc
import pygame, pygame.freetype, os, sys, event_handler
from pygame.locals import *
# Objects
from objects import buttons, char, pizza, door
# Main class
import Controller


class Mixin:
    # Adam's state
    def adamRoom(self):
        # Set flags
        flag = False
        # Create objects in room
        player = char.Char(self.screen, self.pick, 300, 550)
        adam = char.Char(self.screen, 'adam', 1280, 450)
        storage_adam = char.Char(self.screen, 'adam', 20, 430)
        sleeping_adam1 = char.Char(self.screen, 'adam', 500, 100)
        working_adam = char.Char(self.screen, 'adam', 1165, 450)
        backDoor = door.Door(self.screen, 640, 800)
        npcs = [adam, storage_adam, sleeping_adam1, working_adam]
        doors = [backDoor]
        # Create game state
        while True:
            self.state = "adam"
            # Blit objects in room
            self.check_events(player)
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/adamsRoom.png")), (self.height, self.width))
            player.update()
            self.updateScreen(image, player, npcs, doors)
            # Room logic
            if self.collide(player, backDoor) == True:
                self.firstHallway()
                return None
            elif self.collide(player, storage_adam) == True:
                self.health -= 51
                self.spawnRoom(640, 400)
                return None
            elif self.collide(player, sleeping_adam1) == True:
                if flag == False:
                    self.health -= 51
                    self.spawnRoom(640, 400)
                    return None
                elif flag == True:
                    self.health = 100
                    self.key1 = True
                    self.firstHallway()
                    return None
            elif self.collide(player, working_adam) == True:
                self.health -= 51
                self.spawnRoom(640, 400)
                return None
            # Problem to solve
            elif flag == True:
                # Set question/answer
                whatever = self.baseFont.render("how dare you disturb me", True, (0, 0, 0))
                prompt = self.baseFont.render("what is the correct answer?", True, (0, 0, 0))
                # Obtain rects
                whateverRect = whatever.get_rect()
                promptRect = prompt.get_rect()
                whateverRect.top = 500
                promptRect.top = 600
                whateverRect.right = 700
                promptRect.right = 700
                # Blit question/answer
                self.screen.blit(whatever, whateverRect)
                self.screen.blit(prompt, promptRect)
                pygame.display.flip()
                # Blit objects
                pumpernickel = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/pumpernickel.png")), (160, 150))
                self.screen.blit(pumpernickel, (410, 20))
                go = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/go.png")), (160, 150))
                self.screen.blit(go, (1065, 380))
                periwinkle = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/periwinkle.png")), (160, 150))
                self.screen.blit(periwinkle, (0, 360))
                pygame.display.flip()
            # Raise flag
            elif self.collide(player, adam) == True:
                flag = True
