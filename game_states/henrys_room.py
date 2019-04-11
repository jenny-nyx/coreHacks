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
    # Henry's state
    def henryRoom(self):
        # Create objects in room
        player = char.Char(self.screen, self.pick, 300, 700)
        henry = char.Char(self.screen, 'henry', 470, 400)
        backDoor = door.Door(self.screen, 0, 800)
        npcs = [henry]
        doors = [backDoor]
        # Create game state
        while True:
            self.state = "henry"
            # Blit objects in room
            self.check_events(player)
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/henryRoom.png")), (self.height, self.width))
            player.update()
            self.updateScreen(image, player, npcs, doors)
            # Room logic
            if self.collide(player, backDoor) == True:
                self.firstHallway()
                return None
            elif self.collide(player, henry) == True:
                if self.counter == 3:
                    self.health = 100
                    self.key2 = True
                    self.firstHallway()
                    return None
                else:
                    self.health -= 49
                    self.counter = 0
                    self.spawnRoom(640, 400)
                    return None
            # Problem to solve
            linear = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/question.png")), (790, 100))
            # Set question
            hint = self.baseFont.render("Give me the amount of pizzas equal to sisters", True, (0, 0, 0))
            # Obtain rect
            hintRect = hint.get_rect()
            hintRect.top = 370
            hintRect.right = 1100
            # Blit question
            self.screen.blit(linear, (500, 300))
            self.screen.blit(hint, hintRect)
            pygame.display.flip()
