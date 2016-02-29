__author__ = 'olli'


import pygame
import time
import random
import pygame.event

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

white = (255,255,255)

clock = pygame.time.Clock()
FPS = 4

def mainLoop():

    main = True


    while main:
        gameDisplay.fill(white)

        get_key()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()




def get_key():


    while True:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass


mainLoop()


clock.tick(FPS)