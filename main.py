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

  def startingMenu():
    image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "startUpMenu.png")), (game_settings.width, game_settings.height))
    screen.blit(image, (0, 0))

run_game()
