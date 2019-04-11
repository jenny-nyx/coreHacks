import pygame, pygame.freetype, os, sys
import buttons, char, pizza, door
from pygame.locals import *

class Controller:
    def __init__(self, height = 1280, width=800):
        # Initialize caption
        pygame.display.set_caption("The Best Core Project, No Contest")
        # Attributes/Variables
        self.pick = ''
        self.counter = 0
        self.health = 100
        self.key1 = False
        self.key2 = False
        self.key3 = False
        self.answer = ''
        self.check = ''
        self.state = ''
        # Display settings
        self.height = height
        self.width = width
        self.baseFont = pygame.font.SysFont(None, 30)
        self.screen = pygame.display.set_mode((self.height, self.width))
        # Start menu buttons
        self.start_buttons = pygame.sprite.Group()
        self.startButton = buttons.Button('startButton', (220, 450), "images/startButton.png")
        self.quitButton = buttons.Button('helpButton', (700, 450), "images/quitButton.png")
        self.start_buttons.add(self.startButton)
        self.start_buttons.add(self.quitButton)
        # Character select buttons
        self.char_buttons = pygame.sprite.Group()
        self.girl_button = buttons.Button('girl_button', (220, 450), "images/girl.png")
        self.boy_button = buttons.Button('boy_button', (700, 450), 'images/boy.png')
        self.char_buttons.add(self.girl_button)
        self.char_buttons.add(self.boy_button)

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
    # Starting menu state
    def startingMenu(self):
        # Create game state
        while True:
            self.state = "start"
            # Create interface
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/startUpMenu.png")), (self.height, self.width))
            self.screen.blit(image, (0, 0))
            # Blit buttons onto interface
            for s in self.start_buttons:
                self.screen.blit(s.image, s.rect.topleft)
                pygame.display.flip()
            # Menu logic
            mouseLocation = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.startButton.rect.collidepoint(mouseLocation):
                        self.chooseChar()
                        return None
                    elif self.quitButton.rect.collidepoint(mouseLocation):
                        sys.exit()
    # Character select state
    def chooseChar(self):
        # Create game state
        while True:
            self.state = "choose"
            # Create interface
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/choose.png")), (self.height, self.width))
            self.screen.blit(image, (0,0))
            # Blit buttons onto interface
            for s in self.char_buttons:
                self.screen.blit(s.image, s.rect.topleft)
                pygame.display.flip()
            # Select screen logic
            mouseLocation = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.girl_button.rect.collidepoint(mouseLocation):
                        self.pick = 'jenny'
                        self.spawnRoom(640, 400)
                        return None
                    elif self.boy_button.rect.collidepoint(mouseLocation):
                        self.pick = 'alex'
                        self.spawnRoom(640, 400)
                        return None
    # Spawn room state
    def spawnRoom(self, x, y):
        # Create objects in room
        player = char.Char(self.screen, self.pick, x, y)
        wisp = pizza.Pizza(self.screen)
        gateway = door.Door(self.screen, 0, 0)
        npcs = [wisp]
        doors = [gateway]
        # Create game state
        while True:
            self.state = "spawn"
            # Blit objects in room
            self.check_events(player)
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/spawn.png")), (self.height, self.width))
            player.update()
            self.updateScreen(image, player, npcs, doors)
            # Continuous player rect
            x = player.rect.centerx
            y = player.rect.centery
            # Room logic
            if self.collide(player, wisp) == True:
                if self.health < 100:
                    self.health += 5
                self.counter += 1
                self.spawnRoom(x, y)
                return None
            elif self.collide(player, gateway) == True:
                self.firstHallway()
                return None
    # First hallway state
    def firstHallway(self):
        # Create objects in room
        player = char.Char(self.screen, self.pick, 640, 575)
        backDoor = door.Door(self.screen, 640, 800)
        adamDoor = door.Door(self.screen, 400, 320)
        partyDoor = door.Door(self.screen, 850, 320)
        nextDoor = door.Door(self.screen, 640, 0)
        npcs = []
        doors = [backDoor, adamDoor, partyDoor, nextDoor]
        # Create game state
        while True:
            self.state = "first hallway"
            # Blit objects in room
            self.check_events(player)
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/hallway.png")), (self.height, self.width))
            player.update()
            self.updateScreen(image, player, npcs, doors)
            # Room logic
            if self.collide(player, backDoor) == True:
                self.spawnRoom(640, 400)
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
                    lock_txt = self.baseFont.render("CANT PASS: HALLWAY SQUAD IN THE WAY", True, (0,0,0))
                    lock_txt_rect = lock_txt.get_rect()
                    lock_txt_rect.top = 100
                    lock_txt_rect.right = 850
                    self.screen.blit(lock_txt, lock_txt_rect)
                    pygame.display.flip()
    # Adam's state
    def adamRoom(self):
        # Set flags
        flag = False
        # Create objects in room
        player = char.Char(self.screen, self.pick, 300, 550)
        adam = char.Char(self.screen, 'adam', 1280, 450)
        storage_adam = char.Char(self.screen, 'adam', 20, 430)
        sleeping_adam1 = char.Char(self.screen, 'adam', 500, 100)
        working_adam = char.Char(self.screen, 'adam', 1165, 450)
        backDoor = door.Door(self.screen, 640, 800)
        npcs = [adam, storage_adam, sleeping_adam1, working_adam]
        doors = [backDoor]
        # Create game state
        while True:
            self.state = "adam"
            # Blit objects in room
            self.check_events(player)
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/adamsRoom.png")), (self.height, self.width))
            player.update()
            self.updateScreen(image, player, npcs, doors)
            # Room logic
            if self.collide(player, backDoor) == True:
                self.firstHallway()
                return None
            elif self.collide(player, storage_adam) == True:
                self.health -= 51
                self.spawnRoom(640, 400)
                return None
            elif self.collide(player, sleeping_adam1) == True:
                if flag == False:
                    self.health -= 51
                    self.spawnRoom(640, 400)
                    return None
                elif flag == True:
                    self.health = 100
                    self.key1 = True
                    self.firstHallway()
                    return None
            elif self.collide(player, working_adam) == True:
                self.health -= 51
                self.spawnRoom(640, 400)
                return None
            # Problem to solve
            elif flag == True:
                # Set question/answer
                whatever = self.baseFont.render("how dare you disturb me", True, (0, 0, 0))
                prompt = self.baseFont.render("what is the correct answer?", True, (0, 0, 0))
                # Obtain rects
                whateverRect = whatever.get_rect()
                promptRect = prompt.get_rect()
                whateverRect.top = 500
                promptRect.top = 600
                whateverRect.right = 700
                promptRect.right = 700
                # Blit question/answer
                self.screen.blit(whatever, whateverRect)
                self.screen.blit(prompt, promptRect)
                pygame.display.flip()
                # Blit objects
                pumpernickel = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/pumpernickel.png")), (160, 150))
                self.screen.blit(pumpernickel, (410, 20))
                go = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/go.png")), (160, 150))
                self.screen.blit(go, (1065, 380))
                periwinkle = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/periwinkle.png")), (160, 150))
                self.screen.blit(periwinkle, (0, 360))
                pygame.display.flip()
            # Raise flag
            elif self.collide(player, adam) == True:
                flag = True
    # Henry's state
    def henryRoom(self):
        # Create objects in room
        player = char.Char(self.screen, self.pick, 300, 700)
        henry = char.Char(self.screen, 'henry', 470, 400)
        backDoor = door.Door(self.screen, 0, 800)
        npcs = [henry]
        doors = [backDoor]
        # Create game state
        while True:
            self.state = "henry"
            # Blit objects in room
            self.check_events(player)
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/henryRoom.png")), (self.height, self.width))
            player.update()
            self.updateScreen(image, player, npcs, doors)
            # Room logic
            if self.collide(player, backDoor) == True:
                self.firstHallway()
                return None
            elif self.collide(player, henry) == True:
                if self.counter == 3:
                    self.health = 100
                    self.key2 = True
                    self.firstHallway()
                    return None
                else:
                    self.health -= 49
                    self.counter = 0
                    self.spawnRoom(640, 400)
                    return None
            # Problem to solve
            linear = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/question.png")), (790, 100))
            # Set question
            hint = self.baseFont.render("Give me the amount of pizzas equal to sisters", True, (0, 0, 0))
            # Obtain rect
            hintRect = hint.get_rect()
            hintRect.top = 370
            hintRect.right = 1100
            # Blit question
            self.screen.blit(linear, (500, 300))
            self.screen.blit(hint, hintRect)
            pygame.display.flip()
    # Second hallway state
    def secondHallway(self):
        # Create objects in room
        player = char.Char(self.screen, self.pick, 640, 575)
        backDoor = door.Door(self.screen, 640, 800)
        jordansDoor = door.Door(self.screen, 800, 500)
        samsDoor = door.Door(self.screen, 640, 200)
        npcs = []
        doors = [backDoor, jordansDoor, samsDoor]
        # Create game state
        while True:
            self.state = "second hallway"
            # Blit objects in room
            self.check_events(player)
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/secondhallway.png")), (self.height, self.width))
            player.update()
            self.updateScreen(image, player, npcs, doors)
            # Room logic
            if self.collide(player, backDoor) == True:
                self.firstHallway()
                return None
            elif self.collide(player, samsDoor) == True:
                if self.key3 == False:
                    pass
                elif self.key3 == True:
                    self.samsRoom()
                    return None
            elif self.collide(player, jordansDoor) == True:
                self.jordansRoom()
                return None
    # Jordan's State
    def jordansRoom(self):
        # Set flags
        flagBoi = False
        self.answer = ''
        self.check = '350'
        # Create objects in room
        player = char.Char(self.screen, self.pick, 100, 700)
        jordan = char.Char(self.screen, 'jordan', 450, 500)
        backDoor = door.Door(self.screen, 0, 800)
        npcs = [jordan]
        doors = [backDoor]
        # Create game state
        while True:
            self.state = "jordan"
            # Blit objects in room
            self.check_events(player)
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/jordanRoom.png")), (self.height, self.width))
            player.update()
            self.updateScreen(image, player, npcs, doors)
            # Room logic
            if self.collide(player, backDoor) == True:
                self.secondHallway()
                return None
            # Problem to solve
            elif flagBoi == True:
                # Set question
                question_p1 = self.baseFont.render("Given 50 bikes, each with a tank that can go 100 km: how many kms can you go?", True, (0, 0, 0))
                question_p2 = self.baseFont.render("(press q to restart, press enter to submit)", True, (0, 0, 0))
                # Obtain rect
                p1Rect = question_p1.get_rect()
                p1Rect.centerx = 620
                p1Rect.bottom = 300
                p2Rect = question_p2.get_rect()
                p2Rect.centerx = 620
                p2Rect.top = 300
                # Blit question
                self.screen.blit(question_p1, p1Rect)
                self.screen.blit(question_p2, p2Rect)
                pygame.display.flip()
            # Raise flag
            elif self.collide(player, jordan) == True:
                flagBoi = True
    # Sam's state
    def samsRoom(self):
        # Set flags
        flagBoi = False
        self.answer = ''
        self.check = '69'
        # Create objects in room
        player = char.Char(self.screen, self.pick, 100, 700)
        sam = char.Char(self.screen, 'sam', 640, 200)
        backDoor = door.Door(self.screen, 0, 800)
        npcs = [sam]
        doors = [backDoor]
        # Create game state
        while True:
            self.state = "sam"
            # Blit objects inroom
            self.check_events(player)
            image = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(), "images/samRoom.png")), (self.height, self.width))
            player.update()
            self.updateScreen(image, player, npcs, doors)
            # Room logic
            if self.collide(player, backDoor) == True:
                self.secondHallway()
                return None
            # Problem to solve
            elif flagBoi == True:
                # Set question
                question_p1 = self.baseFont.render("What is sam's player level in tetris?", True, (0, 0, 0))
                question_p2 = self.baseFont.render("(press q to restart, press enter to submit)", True, (0, 0, 0))
                # Obtain rects
                p1Rect = question_p1.get_rect()
                p1Rect.centerx = 620
                p1Rect.bottom = 300
                p2Rect = question_p2.get_rect()
                p2Rect.centerx = 620
                p2Rect.top = 300
                # Blit question
                self.screen.blit(question_p1, p1Rect)
                self.screen.blit(question_p2, p2Rect)
                pygame.display.flip()
            # Raise flag
            elif self.collide(player, sam) == True:
                flagBoi = True
    # Event handler
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
                elif event.key == pygame.K_q:
                    self.answer = ""
                elif event.key == pygame.K_1:
                    self.answer += "1"
                elif event.key == pygame.K_2:
                    self.answer += "2"
                elif event.key == pygame.K_3:
                    self.answer += "3"
                elif event.key == pygame.K_4:
                    self.answer += "4"
                elif event.key == pygame.K_5:
                    self.answer += "5"
                elif event.key == pygame.K_6:
                    self.answer += "6"
                elif event.key == pygame.K_7:
                    self.answer+= "7"
                elif event.key == pygame.K_8:
                    self.answer += "8"
                elif event.key == pygame.K_9:
                    self.answer += "9"
                elif event.key == pygame.K_0:
                    self.answer += "0"
                elif event.key == pygame.K_RETURN:
                    # Checks answer for jordan's room
                    if self.state == 'jordan':
                        if self.answer == self.check:
                            self.health = 100
                            self.key3 = True
                            self.secondHallway()
                            return None
                        else:
                            self.health -= 69
                            self.spawnRoom(640, 400)
                            return None
                    # Checks answer for sam's room
                    elif self.state == 'sam':
                        if self.answer == self.check:
                            self.gameWon()
                            return None
                        else:
                            self.health -= 100
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.moving_right = False
                elif event.key == pygame.K_LEFT:
                    player.moving_left = False
                elif event.key == pygame.K_UP:
                    player.moving_up = False
                elif event.key == pygame.K_DOWN:
                    player.moving_down = False
    # Handles blitting and flipping
    def updateScreen(self, image, player, npcs, doors):
        self.screen.blit(image, (0,0))
        player.blitme()
        for npc in npcs:
          npc.blitme()
        for door in doors:
          door.blitme()
        pygame.display.set_caption("The Best Core Project, No Contest. HP: {}% Pizza Count: {}".format(self.health, self.counter))
        pygame.display.flip()
    # Checks for collisions
    def collide(self, player, object):
        if player.rect.colliderect(object):
            return True
