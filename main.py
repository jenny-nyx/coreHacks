import sys
import pygame

def run_game():  # Initializes game and creates screen object
  pygame.init()
  wn = pygame.display.set_mode((1200,800))
  pygame.display.set_caption("Core Boiz")

  # Main loop for game
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

    pygame.display.flip()


run_game()