import pygame, sys

class Mixin:
    # Lost game state
    def gameOver(self):
        # Set caption
        pygame.display.set_caption("better luck next time dork")
        # Create game state
        while True:
            # Logic
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Gameover nerd")
                    sys.exit()
