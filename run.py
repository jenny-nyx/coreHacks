import Controller
import pygame

def runGame():
    pygame.init()
    main_window = Controller.Controller()
    main_window.mainLoop()
runGame()
