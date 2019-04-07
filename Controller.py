import time, pygame, os, buttons, char, sys, random, pizza, door

class Controller:
  def __init__(self, height = 1280, width=800):
    pygame.display.set_caption("The Best Core Project, No Contest")
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
      if (self.state == "first hallway"):
        self.firstHallway()
      if (self.state == 'adam'):
        self.adamRoom()
      if (self.state == "henry"):
        self.henryRoom()
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

  def chooseChar(self):
    global pick
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
            pick = 'jenny'
            self.spawnRoom(pick, 640, 400)
            return None
          elif self.boy_button.rect.collidepoint(mouseLocation):
            pick = 'alex'
            self.spawnRoom(pick, 640, 400)
            return None

  def spawnRoom(self, chosen, x, y):
    self.chosen = chosen
    player = char.Char(self.screen, self.chosen, x, y)
    wisp = pizza.Pizza(self.screen)
    gateway = door.Door(self.screen, 0, 0)
    while True:
      self.check_events(player)
      self.state = "spawn"
      image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/spawn.png")), (self.height, self.width))
      self.screen.blit(image, (0,0))
      player.update()
      self.updateScreen(image, player)
      gateway.blitme()
      self.blitPizza(wisp)
      x = player.rect.centerx
      y = player.rect.centery
      if self.collide(player, wisp) == True:
        self.spawnRoom(chosen, x, y)
        return None
      if self.collide(player, gateway) == True:
        self.firstHallway()
        return None

  def firstHallway(self):
    player = char.Char(self.screen, pick, 640, 575)
    backDoor = door.Door(self.screen, 640, 800)
    adamDoor = door.Door(self.screen, 400, 320)
    partyDoor = door.Door(self.screen, 850, 320)
    nextDoor = door.Door(self.screen, 640, 0)

    while True:
      self.check_events(player)
      self.state = "first hallway"
      image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/hallway.png")), (self.height, self.width))
      self.screen.blit(image, (0, 0))
      player.update()
      self.updateScreen(image, player)
      backDoor.blitme()
      adamDoor.blitme()
      partyDoor.blitme()
      nextDoor.blitme()
      pygame.display.flip()
      if self.collide(player, backDoor) == True:
        self.spawnRoom(pick, 640, 400)
        return None
      if self.collide(player, adamDoor) == True:
        self.adamRoom()
        return None
      if self.collide(player, partyDoor) == True:
        self.henryRoom()
        return None

  def adamRoom(self):
    player = char.Char(self.screen, pick, 300, 550)
    adam = char.Char(self.screen, 'adam', 1280, 450)
    storage_adam = char.Char(self.screen, 'adam', 20, 430)
    sleeping_adam1 = char.Char(self.screen, 'adam', 500, 100)
    working_adam = char.Char(self.screen, 'adam', 1190, 450)
    backDoor = door.Door(self.screen, 640, 800)

    while True:
      self.check_events(player)
      self.state = "adam"
      image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/adamsRoom.png")), (self.height, self.width))
      self.screen.blit(image, (0, 0))
      player.update()
      self.updateScreen(image, player)
      backDoor.blitme()
      adam.blitme()
      storage_adam.blitme()
      sleeping_adam1.blitme()
      working_adam.blitme()
      pygame.display.flip()
      if self.collide(player, backDoor) == True:
        self.firstHallway()
        return None
      elif self.collide(player, storage_adam) == True:
        self.spawnRoom(pick, 640, 400)
        return None
      elif self.collide(player, sleeping_adam1) == True:
        self.spawnRoom(pick, 640, 400)
        return None
      elif self.collide(player, working_adam) == True:
        self.spawnRoom(pick, 640, 400)
        return None
      #elif self.collide(player, adam) == True:

  def henryRoom(self):
    player = char.Char(self.screen, pick, 300, 700)
    #henry = char.Char(self.screen, 'henry', 470, 400)
    backDoor = door.Door(self.screen, 0, 800)

    while True:
      self.check_events(player)
      self.state = "henry"
      image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/henryRoom.png")), (self.height, self.width))
      self.screen.blit(image, (0, 0))
      player.update()
      self.updateScreen(image, player)
      backDoor.blitme()
      #henry.blitme()
      if self.collide(player, backDoor) == True:
        self.firstHallway()
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


  def updateScreen(self, image, object):
    self.screen.blit(image, (0,0))
    object.blitme()
    pygame.display.flip()

  def blitPizza(self, wisp):
    wisp.blitme()
    pygame.display.flip()

  def collide(self, player, object):
    if player.rect.colliderect(object):
        return True;
