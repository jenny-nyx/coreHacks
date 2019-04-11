import pygame, sys

class Mixin:
    # Won game state
    def gameWon(self):
        # Set caption
        pygame.display.set_caption("You won!")
        # Create game state
        while True:
            # Logic
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(":c we didnt think you'd get this far")
                    sys.exit()
