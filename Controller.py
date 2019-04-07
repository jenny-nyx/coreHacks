import time, pygame, pygame.freetype, os, buttons, char, sys, random, pizza, door, eztext
from pygame.locals import *

class Controller:
  def __init__(self, height = 1280, width=800):
    pygame.display.set_caption("The Best Core Project, No Contest")
    global question
    question = False
    global flag
    flag = False
    global key1
    key1 = False
    global key2
    key2 = False
    global health
    health = 100
    global counter
    counter = 0
    global locked
    locked = True
    global key3
    key3 = False
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
      if (self.state == "second hallway"):
        self.secondHallway();
      if (self.state == "jordan"):
        self.jordansRoom()
      if (self.state == "sam"):
        self.samsRoom()
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
    global locked
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
        global health
        if health < 100:
          health += 5
        global counter
        counter += 1
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
    baseFont = pygame.font.SysFont(None, 30)

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
      if self.collide(player, nextDoor) == True:
        if key1 == True and key2 == True:
          self.secondHallway()
          return None
        elif locked == True:
          lock_txt = baseFont.render("CANT PASS: HALLWAY SQUAD IN THE WAY", True, (0,0,0))
          lock_txt_rect = lock_txt.get_rect()
          lock_txt_rect.top = 100
          lock_txt_rect.right = 850
          self.screen.blit(lock_txt, lock_txt_rect)
          pygame.display.flip()

  def adamRoom(self):
    global flag
    global key1
    player = char.Char(self.screen, pick, 300, 550)
    adam = char.Char(self.screen, 'adam', 1280, 450)
    storage_adam = char.Char(self.screen, 'adam', 20, 430)
    sleeping_adam1 = char.Char(self.screen, 'adam', 500, 100)
    working_adam = char.Char(self.screen, 'adam', 1165, 450)
    backDoor = door.Door(self.screen, 640, 800)
    baseFont = pygame.font.SysFont(None, 30)
    question = eztext.Input(maxlength = 40, color=(0, 0, 0), prompt="what is your guess?: ")

    while True:
      global health
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
        health -= 51
        self.spawnRoom(pick, 640, 400)
        return None
      elif self.collide(player, sleeping_adam1) == True:
        if flag == False:
            health -= 51
            self.spawnRoom(pick, 640, 400)
            return None
        elif flag == True:
            key1 = True
            self.firstHallway()
            return None
      elif self.collide(player, working_adam) == True:
        health -= 51
        self.spawnRoom(pick, 640, 400)
        return None
      elif flag == True:
        whatever = baseFont.render("how dare you disturb me", True, (0, 0, 0))
        prompt = baseFont.render("what is the correct answer?", True, (0, 0, 0))

        whateverRect = whatever.get_rect()
        promptRect = prompt.get_rect()
        whateverRect.top = 500
        promptRect.top = 600
        whateverRect.right = 700
        promptRect.right = 700
        pumpernickel = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/pumpernickel.png")), (160, 150))
        self.screen.blit(pumpernickel, (410, 20))
        go = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/go.png")), (160, 150))
        self.screen.blit(go, (1065, 380))
        periwinkle = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/periwinkle.png")), (160, 150))
        self.screen.blit(periwinkle, (0, 360))

        self.screen.blit(whatever, whateverRect)
        self.screen.blit(prompt, promptRect)
        pygame.display.flip()

      elif self.collide(player, adam) == True:
        flag = True

  def henryRoom(self):
    global pick
    global health
    player = char.Char(self.screen, pick, 300, 700)
    henry = char.Char(self.screen, 'henry', 470, 400)
    backDoor = door.Door(self.screen, 0, 800)
    baseFont = pygame.font.SysFont(None, 30)

    while True:
      global question
      global counter
      global key2
      self.check_events(player)
      self.state = "henry"
      image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/henryRoom.png")), (self.height, self.width))
      self.screen.blit(image, (0, 0))
      player.update()
      self.updateScreen(image, player)
      backDoor.blitme()
      henry.blitme()
      pygame.display.flip()
      if self.collide(player, backDoor) == True:
        self.firstHallway()
        return None
      linear = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/question.png")), (790, 100))
      self.screen.blit(linear, (500, 300))
      hint = baseFont.render("Give me the amount of pizzas equal to sisters", True, (0, 0, 0))
      hintRect = hint.get_rect()
      hintRect.top = 370
      hintRect.right = 1100
      self.screen.blit(hint, hintRect)
      pygame.display.flip()
      if self.collide(player, henry) == True:
        if question == True:
          if counter == 3:
            key2 = True
            self.firstHallway()
            return None
          else:
            health -= 49
            counter = 0
            self.spawnRoom(pick, 640, 400)
            return None
        else:
          question = True

  def secondHallway(self):
    global pick
    global health
    global key3
    player = char.Char(self.screen, pick, 640, 575)
    backDoor = door.Door(self.screen, 640, 800)
    samsDoor = door.Door(self.screen, 640, 200)
    jordansDoor = door.Door(self.screen, 800, 500)
    while True:
      self.state == "second hallway"
      backDoor.blitme()
      samsDoor.blitme()
      jordansDoor.blitme()
      pygame.display.flip()
      self.check_events(player)
      player.update()
      image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/secondhallway.png")), (self.height, self.width))
      self.screen.blit(image, (0,0))
      if self.collide(player, backDoor) == True:
        self.firstHallway()
        return None
      elif self.collide(player, samsDoor) == True:
        if key3 == False:
          pass
        elif key3 == True:
          self.samsRoom();
          return None

      elif self.collide(player, jordansDoor) == True:
        self.jordansRoom();
        return None

      self.updateScreen(image, player)

  def jordansRoom(self):
    global health
    flagBoi = False
    player = char.Char(self.screen, pick, 100, 700)
    jordan = char.Char(self.screen, 'jordan', 450, 500)
    backDoor = door.Door(self.screen, 0, 800)
    baseFont = pygame.font.SysFont(None, 30)
    answer = ""
    check = "350"

    while True:
      self.state == "jordan"
      backDoor.blitme()
      jordan.blitme()
      pygame.display.flip()
      self.check_events(player)
      player.update()
      image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/jordanRoom.png")), (self.height, self.width))
      self.screen.blit(image, (0, 0))
      self.updateScreen(image, player)
      question = baseFont.render("Given 50 bikes, each with a tank that can go 100 km: how many kms can you go? (press q to restart, press enter to submit): ", True, (0, 0, 0))
      questionRect = question.get_rect();
      questionRect.centerx = 620
      questionRect.top = 300
      self.screen.blit(question, questionRect)
      pygame.display.flip()
      if self.collide(player, backDoor) == True:
        self.secondHallway()
        return None
      if self.collide(player, jordan) == True:
          flagBoi = True

      if (flagBoi):
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
              answer=""
            if event.key == pygame.K_1 or event.key == pygame.K_P1:
              answer+="1"
            if event.key == pygame.K_2 or event.key == pygame.K_P2:
              answer+="2"
            if event.key == pygame.K_3 or event.key == pygame.K_P3:
              answer+="3"
            if event.key == pygame.K_4 or event.key == pygame.K_P4:
              answer+="4"
            if event.key == pygame.K_5 or event.key == pygame.K_P5:
              answer+="5"
            if event.key == pygame.K_6 or event.key == pygame.K_P6:
              answer+="6";
            if event.key == pygame.K_7 or event.key == pygame.K_P7:
              answer+="7"
            if event.key == pygame.K_8 or event.key == pygame.K_P8:
              answer+="8"
            if event.key == pygame.K_9 or event.key == pygame.K_P9:
              answer+="9"
            if event.key == pygame.K_0 or event.key == pygame.K_P0:
              answer+="0"
            if event.key == pygame.K_RETURN:
              if answer == check:
                key3 = True;
                self.secondHallway()
                return None
              elif answer != check:
                health -= 69
                self.spawnRoom(pick, 640, 400)
                return None

  def samsRoom(self):
    player = char.Char(self.screen, pick, 640, 600)
    sam = char.Char(self.screen, pick, 500, 500)
    backDoor = door.Door(self.screen, 0, 800)
    while True:
      self.state = "sam"
      backDoor.blitme()
      sam.blitme()
      player.update()
      image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/samRoom.png")), (self.height, self.width))
      self.screen.blit(image, (0, 0))
      self.updateScreen(image, player)

  def check_events(self, player):
    for event in pygame.event.get():
      global health
      global key1
      global key2
      global locked
      if key1 == True and key2 == True:
        locked = False
      if event.type == pygame.QUIT:
        sys.exit()
      elif health <= 0:
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
    pygame.display.set_caption("The Best Core Project, No Contest. HP: {}% Pizza Count: {}".format(health, counter))
    pygame.display.flip()

  def blitPizza(self, wisp):
    wisp.blitme()
    pygame.display.flip()

  def collide(self, player, object):
    if player.rect.colliderect(object):
        return True;
