import time, pygame, pygame.freetype, os, buttons, char, sys, random, pizza, door, eztext
from pygame.locals import *

class Controller:
    def __init__(self, height = 1280, width=800):
        pygame.display.set_caption("The Best Core Project, No Contest")
        self.pick = ''
        self.flag = False
        self.key1 = False
        self.key2 = False
        self.health = 100
        self.counter = 0
        self.key3 = False
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
            elif (self.state == "choose"):
                self.chooseChar()
            elif (self.state == "spawn"):
                self.spawnRoom()
            elif (self.state == "first hallway"):
                self.firstHallway()
            elif (self.state == 'adam'):
                self.adamRoom()
            elif (self.state == "henry"):
                self.henryRoom()
            elif (self.state == "second hallway"):
                self.secondHallway();
            elif (self.state == "jordan"):
                self.jordansRoom()
            elif (self.state == "sam"):
                self.samsRoom()
            elif (self.state == "gameover"):
                self.gameOver()
            elif (self.state == "gamewon"):
                self.gameWon()

    def gameWon(self):
        pygame.display.set_caption("You won!")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print(":c we didnt think you'd get this far")
                    sys.exit()

    def gameOver(self):
        pygame.display.set_caption("better luck next time dork")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Gameover nerd")
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
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.startButton.rect.collidepoint(mouseLocation):
                        self.chooseChar()
                        return None
                elif self.quitButton.rect.collidepoint(mouseLocation):
                    pygame.quit
                    sys.exit()

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
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.girl_button.rect.collidepoint(mouseLocation):
                        self.pick = 'jenny'
                        self.spawnRoom(self.pick, 640, 400)
                        return None
                    elif self.boy_button.rect.collidepoint(mouseLocation):
                        self.pick = 'alex'
                        self.spawnRoom(self.pick, 640, 400)
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
                if self.health < 100:
                    self.health += 5
                self.counter += 1
                self.spawnRoom(chosen, x, y)
                return None
            elif self.collide(player, gateway) == True:
                self.firstHallway()
                return None

    def firstHallway(self):
        player = char.Char(self.screen, self.pick, 640, 575)
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
                self.spawnRoom(self.pick, 640, 400)
                return None
            elif self.collide(player, adamDoor) == True:
                self.adamRoom()
                return None
            elif self.collide(player, partyDoor) == True:
                self.henryRoom()
                return None
            elif self.collide(player, nextDoor) == True:
                if self.key1 == True and self.key2 == True:
                    self.secondHallway()
                    return None
                elif self.key1 == False or self.key2 == False:
                    lock_txt = baseFont.render("CANT PASS: HALLWAY SQUAD IN THE WAY", True, (0,0,0))
                    lock_txt_rect = lock_txt.get_rect()
                    lock_txt_rect.top = 100
                    lock_txt_rect.right = 850
                    self.screen.blit(lock_txt, lock_txt_rect)
                    pygame.display.flip()

    def adamRoom(self):
        player = char.Char(self.screen, self.pick, 300, 550)
        adam = char.Char(self.screen, 'adam', 1280, 450)
        storage_adam = char.Char(self.screen, 'adam', 20, 430)
        sleeping_adam1 = char.Char(self.screen, 'adam', 500, 100)
        working_adam = char.Char(self.screen, 'adam', 1165, 450)
        backDoor = door.Door(self.screen, 640, 800)
        baseFont = pygame.font.SysFont(None, 30)

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
                self.health -= 51
                self.spawnRoom(self.pick, 640, 400)
                return None
            elif self.collide(player, sleeping_adam1) == True:
                if self.flag == False:
                    self.health -= 51
                    self.spawnRoom(self.pick, 640, 400)
                    return None
                elif self.flag == True:
                    self.health = 100
                    self.key1 = True
                    self.firstHallway()
                    return None
            elif self.collide(player, working_adam) == True:
                self.health -= 51
                self.spawnRoom(self.pick, 640, 400)
                return None

            elif self.flag == True:
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
                self.flag = True

    def henryRoom(self):
        player = char.Char(self.screen, self.pick, 300, 700)
        henry = char.Char(self.screen, 'henry', 470, 400)
        backDoor = door.Door(self.screen, 0, 800)
        baseFont = pygame.font.SysFont(None, 30)

        while True:
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
                if self.counter == 3:
                    self.health = 100
                    self.key2 = True
                    self.firstHallway()
                    return None
                else:
                    self.health -= 49
                    self.counter = 0
                    self.spawnRoom(self.pick, 640, 400)
                    return None

    def secondHallway(self):
        player = char.Char(self.screen, self.pick, 640, 575)
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
                if self.key3 == False:
                    pass
                elif self.key3 == True:
                    self.samsRoom();
                    return None

            elif self.collide(player, jordansDoor) == True:
                self.jordansRoom();
                return None

            self.updateScreen(image, player)

    def jordansRoom(self):
        flagBoi = False
        player = char.Char(self.screen, self.pick, 100, 700)
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
            pygame.display.flip()
            if self.collide(player, backDoor) == True:
                self.secondHallway()
                return None
            elif self.collide(player, jordan) == True:
                flagBoi = True

            elif (flagBoi):

                question = baseFont.render("Given 50 bikes, each with a tank that can go 100 km: how many kms can you go? (press q to restart, press enter to submit, no numPad): ", True, (0, 0, 0))
                questionRect = question.get_rect();
                questionRect.centerx = 620
                questionRect.top = 300
                self.screen.blit(question, questionRect)
                pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        answer=""
                    elif event.key == pygame.K_1:
                        answer+="1"
                    elif event.key == pygame.K_2:
                        answer+="2"
                    elif event.key == pygame.K_3:
                        answer+="3"
                    elif event.key == pygame.K_4:
                        answer+="4"
                    elif event.key == pygame.K_5:
                        answer+="5"
                    elif event.key == pygame.K_6:
                        answer+="6";
                    elif event.key == pygame.K_7:
                        answer+="7"
                    elif event.key == pygame.K_8:
                        answer+="8"
                    elif event.key == pygame.K_9:
                        answer+="9"
                    elif event.key == pygame.K_0:
                        answer+="0"
                    elif event.key == pygame.K_RETURN:
                        if answer == check:
                            self.health = 100
                            self.key3 = True
                            self.secondHallway()
                            return None
                        else:
                            self.health -= 69
                            self.spawnRoom(self.pick, 640, 400)
                            return None

    def samsRoom(self):
        player = char.Char(self.screen, self.pick, 100, 700)
        sam = char.Char(self.screen, 'sam', 640, 200)
        backDoor = door.Door(self.screen, 0, 800)
        baseFont = pygame.font.SysFont(None, 30)
        answer = ""
        check = "69"
        flagBoi = False;

        while True:
            self.state = "sam"
            backDoor.blitme()
            sam.blitme()
            pygame.display.flip()
            self.check_events(player)
            player.update()
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/samRoom.png")), (self.height, self.width))
            self.screen.blit(image, (0, 0))
            self.updateScreen(image, player)
            pygame.display.flip()
            if self.collide(player, backDoor) == True:
                self.secondHallway()
                return None
            elif self.collide(player, sam) == True:
                flagBoi = True

            elif (flagBoi):
                question = baseFont.render("what is sam's player level in tetris?: (q to reset, enter to submit) ", True, (0, 0, 0))
                questionRect = question.get_rect();
                questionRect.centerx = 620
                questionRect.top = 300
                self.screen.blit(question, questionRect)
                pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        answer=""
                    elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        answer+="1"
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        answer+="2"
                    elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        answer+="3"
                    elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        answer+="4"
                    elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        answer+="5"
                    elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        answer+="6";
                    elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        answer+="7"
                    elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        answer+="8"
                    elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        answer+="9"
                    elif event.key == pygame.K_0 or event.key == pygame.K_KP0:
                        answer+="0"
                    elif event.key == pygame.K_RETURN:
                        if answer == check:
                            self.key3 = True
                            self.gameWon()
                            return None
                        elif answer != check:
                            self.health -= 100
                            self.spawnRoom(self.pick, 640, 400)
                            return None


    def check_events(self, player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif self.health <= 0:
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
        pygame.display.set_caption("The Best Core Project, No Contest. HP: {}% Pizza Count: {}".format(self.health, self.counter))
        pygame.display.flip()

    def blitPizza(self, wisp):
        wisp.blitme()
        pygame.display.flip()

    def collide(self, player, object):
        if player.rect.colliderect(object):
            return True;
