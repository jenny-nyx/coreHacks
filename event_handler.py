# Misc
import pygame, pygame.freetype, os, sys
from pygame.locals import *
# Objects
from objects import buttons, char, pizza, door
# Main class
import Controller

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
                elif event.key == pygame.K_BACKQUOTE: # ` or tilda
                    self.answer = ""
                elif event.key == pygame.BACKSPACE:
                    self.answer -= self.answer[answer.length-1]
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
                elif event.key == pygame.K_a:
                    self.answer += "a"
                elif event.key == pygame.K_b:
                    self.answer += "b"
                elif event.key == pygame.K_c:
                    self.answer += "c"
                elif event.key == pygame.K_d:
                    self.answer += "d"
                elif event.key == pygame.K_e:
                    self.answer += "e"
                elif event.key == pygame.K_f:
                    self.answer += "f"
                elif event.key == pygame.K_g:
                    self.answer += "g"
                elif event.key == pygame.K_h:
                    self.answer += "h"
                elif event.key == pygame.K_i:
                    self.answer += "i"
                elif event.key == pygame.K_j:
                    self.answer += "j"
                elif event.key == pygame.K_k:
                    self.answer += "k"
                elif event.key == pygame.K_l:
                    self.answer += "l"
                elif event.key == pygame.K_m:
                    self.answer += "m"
                elif event.key == pygame.K_n:
                    self.answer += "n"
                elif event.key == pygame.K_o:
                    self.answer += "o"
                elif event.key == pygame.K_p:
                    self.answer += "p"
                elif event.key == pygame.K_q:
                    self.answer += "q"
                elif event.key == pygame.K_r:
                    self.answer += "r"
                elif event.key == pygame.K_s:
                    self.answer += "s"
                elif event.key == pygame.K_t:
                    self.answer += "t"
                elif event.key == pygame.K_u:
                    self.answer += "u"
                elif event.key == pygame.K_v:
                    self.answer += "v"
                elif event.key == pygame.K_w:
                    self.answer += "w"
                elif event.key == pygame.K_x:
                    self.answer += "x"
                elif event.key == pygame.K_y:
                    self.answer += "y"
                elif event.key == pygame.K_z:
                    self.answer += "z"
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
