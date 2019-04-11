# Misc
import pygame, pygame.freetype, os, sys, event_handler
from pygame.locals import *
# Objects
from objects import buttons, char, pizza, door
# Main class
import Controller


class Mixin:
    # Sam's state
    def samsRoom(self):
        # Set flags
        flagBoi = False
        self.answer = ''
        self.check = '69'
        # Create objects in room
        player = char.Char(self.screen, self.pick, 100, 700)
        sam = char.Char(self.screen, 'sam', 640, 200)
        backDoor = door.Door(self.screen, 0, 800)
        npcs = [sam]
        doors = [backDoor]
        # Create game state
        while True:
            self.state = "sam"
            # Blit objects inroom
            self.check_events(player)
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/samRoom.png")), (self.height, self.width))
            player.update()
            self.updateScreen(image, player, npcs, doors)
            # Room logic
            if self.collide(player, backDoor) == True:
                self.secondHallway()
                return None
            # Problem to solve
            elif flagBoi == True:
                # Set question
                question_p1 = self.baseFont.render("What is sam's player level in tetris?", True, (0, 0, 0))
                question_p2 = self.baseFont.render("(press ` to restart, press enter to submit, press backspace/delete/return to go back one character)", True, (0, 0, 0))
                # Obtain rects
                p1Rect = question_p1.get_rect()
                p1Rect.centerx = 620
                p1Rect.bottom = 300
                p2Rect = question_p2.get_rect()
                p2Rect.centerx = 620
                p2Rect.top = 300
                # Blit question
                self.screen.blit(question_p1, p1Rect)
                self.screen.blit(question_p2, p2Rect)
                pygame.display.flip()
            # Raise flag
            elif self.collide(player, sam) == True:
                flagBoi = True
