import sys
import pygame
from settings import Settings

def run_game():  # Initializes game and creates screen object
  pygame.init()
  game_settings = Settings()
  wn = pygame.display.set_mode((game_settings.width, game_settings.height))

  # Main loop for game
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

    pygame.display.flip()


run_game()
