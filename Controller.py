import time, pygame, os, buttons, char, sys, random, pizza, door

class Controller:
  def __init__(self, height = 1280, width=800):
    self.state = "start"
    self.height = height
    self.width = width
    self.screen = pygame.display.set_mode((self.height, self.width))
    self.char_buttons = pygame.sprite.Group()
    self.start_buttons = pygame.sprite.Group()
    self.startButton = buttons.Button('startButton', (220, 450), "images/startButton.png")
    self.quitButton = buttons.Button('helpButton', (700, 450), "images/quitButton.png")
    self.start_buttons.add(self.startButton)
    self.start_buttons.add(self.quitButton)
    self.girl_button = buttons.Button('girl_button', (220, 450), "images/girl.png")
    self.boy_button = buttons.Button('boy_button', (700, 450), 'images/boy.png')
    self.char_buttons.add(self.girl_button)
    self.char_buttons.add(self.boy_button)

  def mainLoop(self):
    while True:
      if (self.state == "start"):
        self.startingMenu()
      if (self.state == "choose"):
        self.chooseChar()
      if (self.state == "spawn"):
        self.spawnRoom()
      if (self.state == "gameover"):
        self.gameOver()
      if (self.state == "gamewon"):
        self.gameWon()

  def gameWon(self):
    #self.state == gamewon
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

  def gameOver(self):
    #self.state == gameover
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

  def startingMenu(self):
    while True:
      mouseLocation = pygame.mouse.get_pos()
      image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/startUpMenu.png")), (self.height, self.width))
      self.screen.blit(image, (0, 0))
      for s in self.start_buttons:
        self.screen.blit(s.image, s.rect.topleft)
      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          if self.startButton.rect.collidepoint(mouseLocation):
            self.chooseChar()
            return None
          elif self.quitButton.rect.collidepoint(mouseLocation):
            pygame.quit
            sys.exit()

  def spawnRoom(self, chosen):
    self.chosen = chosen
    player = char.Char(self.screen, self.chosen)
    wisp = pizza.Pizza(self.screen)
    gateway = door.Door(self.screen, 0, 0)
    while True:
      self.check_events(player)
      self.state = "spawn"
      image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/spawn.png")), (self.height, self.width))
      self.screen.blit(image, (0,0))
      coreLounge = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/coreLounge.png")), (400, 300))
      self.screen.blit(coreLounge, (700, 300))
      player.update()
      self.updateScreen(image, player, gateway)
      self.blitPizza(wisp)

  def chooseChar(self):
    while True:
      mouseLocation = pygame.mouse.get_pos()
      self.state = "choose"
      image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/choose.png")), (self.height, self.width))
      self.screen.blit(image, (0,0))
      for s in self.char_buttons:
        self.screen.blit(s.image, s.rect.topleft)
      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.quit:
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          if self.girl_button.rect.collidepoint(mouseLocation):
            chosen = 'jenny'
            self.spawnRoom(chosen)
            return None
          elif self.boy_button.rect.collidepoint(mouseLocation):
            chosen = 'alex'
            self.spawnRoom(chosen)
            return None

  def check_events(self, player):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          player.moving_right = True
        elif event.key == pygame.K_LEFT:
          player.moving_left = True
        elif event.key == pygame.K_UP:
          player.moving_up = True
        elif event.key == pygame.K_DOWN:
          player.moving_down = True
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
          player.moving_right = False
        elif event.key == pygame.K_LEFT:
          player.moving_left = False
        elif event.key == pygame.K_UP:
          player.moving_up = False
        elif event.key == pygame.K_DOWN:
          player.moving_down = False


  def updateScreen(self, image, object, door):
    self.screen.blit(image, (0,0))
    object.blitme()
    door.blitme()
    pygame.display.flip()

  def blitPizza(self, wisp):
    wisp.blitme()
    pygame.display.flip()

