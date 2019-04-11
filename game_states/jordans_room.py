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
    # Jordan's State
    def jordansRoom(self):
        # Set flags
        flagBoi = False
        self.answer = ''
        self.check = '350'
        # Create objects in room
        player = char.Char(self.screen, self.pick, 100, 700)
        jordan = char.Char(self.screen, 'jordan', 450, 500)
        backDoor = door.Door(self.screen, 0, 800)
        npcs = [jordan]
        doors = [backDoor]
        # Create game state
        while True:
            self.state = "jordan"
            # Blit objects in room
            self.check_events(player)
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/jordanRoom.png")), (self.height, self.width))
            player.update()
            self.updateScreen(image, player, npcs, doors)
            # Room logic
            if self.collide(player, backDoor) == True:
                self.secondHallway()
                return None
            # Problem to solve
            elif flagBoi == True:
                # Set question
                question_p1 = self.baseFont.render("Given 50 bikes, each with a tank that can go 100 km: how many kms can you go?", True, (0, 0, 0))
                question_p2 = self.baseFont.render("(press q to restart, press enter to submit)", True, (0, 0, 0))
                # Obtain rect
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
            elif self.collide(player, jordan) == True:
                flagBoi = True
