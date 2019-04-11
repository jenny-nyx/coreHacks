# Misc
import pygame, pygame.freetype, os, sys
import event_handler, updateScreen, collision
from pygame.locals import *
# Objects
from objects import buttons, char, pizza, door
# Main class
import Controller


class Mixin:
    # Starting menu state
    def startingMenu(self):
        # Create game state
        while True:
            self.state = "start"
            # Create interface
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/startUpMenu.png")), (self.height, self.width))
            self.screen.blit(image, (0, 0))
            # Blit buttons onto interface
            for s in self.start_buttons:
                self.screen.blit(s.image, s.rect.topleft)
                pygame.display.flip()
            # Menu logic
            mouseLocation = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.startButton.rect.collidepoint(mouseLocation):
                        self.chooseChar()
                        return None
                    elif self.quitButton.rect.collidepoint(mouseLocation):
                        sys.exit()
