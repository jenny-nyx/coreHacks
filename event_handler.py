import pygame, pygame.freetype, os, sys
from objects import buttons, char, pizza, door
from game_states import start_menu, loss_screen, win_screen, char_select, spawn, first_hallway, adams_room, henrys_room
from pygame.locals import *

class Mixin:
    # Event handler
    def check_events(self, player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif self.health <= 0:
                self.gameOver()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.moving_right = True
                elif event.key == pygame.K_LEFT:
                    player.moving_left = True
                elif event.key == pygame.K_UP:
                    player.moving_up = True
                elif event.key == pygame.K_DOWN:
                    player.moving_down = True
                elif event.key == pygame.K_q:
                    self.answer = ""
                elif event.key == pygame.K_1:
                    self.answer += "1"
                elif event.key == pygame.K_2:
                    self.answer += "2"
                elif event.key == pygame.K_3:
                    self.answer += "3"
                elif event.key == pygame.K_4:
                    self.answer += "4"
                elif event.key == pygame.K_5:
                    self.answer += "5"
                elif event.key == pygame.K_6:
                    self.answer += "6"
                elif event.key == pygame.K_7:
                    self.answer+= "7"
                elif event.key == pygame.K_8:
                    self.answer += "8"
                elif event.key == pygame.K_9:
                    self.answer += "9"
                elif event.key == pygame.K_0:
                    self.answer += "0"
                elif event.key == pygame.K_RETURN:
                    # Checks answer for jordan's room
                    if self.state == 'jordan':
                        if self.answer == self.check:
                            self.health = 100
                            self.key3 = True
                            self.secondHallway()
                            return None
                        else:
                            self.health -= 69
                            self.spawnRoom(640, 400)
                            return None
                    # Checks answer for sam's room
                    elif self.state == 'sam':
                        if self.answer == self.check:
                            self.gameWon()
                            return None
                        else:
                            self.health -= 100
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.moving_right = False
                elif event.key == pygame.K_LEFT:
                    player.moving_left = False
                elif event.key == pygame.K_UP:
                    player.moving_up = False
                elif event.key == pygame.K_DOWN:
                    player.moving_down = False
