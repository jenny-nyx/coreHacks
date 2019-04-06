import sys, pygame, os

class Controller:
  def __init__(self, height = 1920, width=1080):
    self.state = "game";
    self.height = height;
    self.width = width;
    self.screen = pygame.display.set_mode((self.height, self.width));

  def mainLoop(self):
    while True:
      if (self.state == "game"):
        self.gameLoop();
      if (self.state == "gameover"):
        self.gameOver()
      if (self.state == "gamewon"):
        self.gameWon()

  def gameLoop(self):
    while self.state == "game":
      for event in pygame.event.get()

  def gameWon(self):
    #self.state == gamewon
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit();

  def gameOver(self):
    #self.state == gameover
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit();
