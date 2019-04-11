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
    # Spawn room state
    def spawnRoom(self, x, y):
        # Create objects in room
        player = char.Char(self.screen, self.pick, x, y)
        wisp = pizza.Pizza(self.screen)
        gateway = door.Door(self.screen, 0, 0)
        npcs = [wisp]
        doors = [gateway]
        # Create game state
        while True:
            self.state = "spawn"
            # Blit objects in room
            self.check_events(player)
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/spawn.png")), (self.height, self.width))
            player.update()
            self.updateScreen(image, player, npcs, doors)
            # Continuous player rect
            x = player.rect.centerx
            y = player.rect.centery
            # Room logic
            if self.collide(player, wisp) == True:
                if self.health < 100:
                    self.health += 5
                self.counter += 1
                self.spawnRoom(x, y)
                return None
            elif self.collide(player, gateway) == True:
                self.firstHallway()
                return None
