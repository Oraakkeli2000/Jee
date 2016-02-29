# Tän pelin idea on ollu tekstipeli, mutta jonkinlaisella piirretyllä taustalla,
# Homman nimi on näyttää alareunassa syötettä, kuten ohjeet ja vaihtoehdot jne
# ja piirtää taustaksi joku kuva. Mahdollisesti tekstin taustaksi joku laatikko tms.

import pygame

from pygame.locals import *
import sys, eztext

import time
import random

pygame.init()

clock = pygame.time.Clock()
FPS = 30

red = (255, 0, 0)
black = (0, 0, 0)
iho = (255,178,102)

titleFont = pygame.font.SysFont(None, 100)
normFont = pygame.font.SysFont(None, 30)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Peli")

txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='type here: ')

intro = True

def tekstiBoksi():

    while True:
        events = pygame.event.get()
        # process other events
        for event in events:
            # close it x button si pressed
            if event.type == QUIT: return
        txtbx.update(events)
            # blit txtbx on the sceen
        txtbx.draw(gameDisplay)
            # refresh the display
        pygame.display.update()

def quittaus():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



def text_objects(text, color, kind):
    if kind == "title":
        textSurface = titleFont.render(text, True, color)
    if kind == "norm":
        textSurface = normFont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def teksti_Laatikossa(teksti, x, y):

    leveys, korkeus = normFont.size(teksti)

    pygame.draw.rect(gameDisplay, iho, (x,y,leveys,korkeus))
    tekstiLaatikossa = normFont.render(teksti, True, black)
    gameDisplay.blit(tekstiLaatikossa, (x, y))


def teksti_Naytolle(teksti, x, y):

    tekstiNaytolle = normFont.render(teksti, True, black)
    gameDisplay.blit(tekstiNaytolle, (x, y))



def message_to_screen(msg, color, x_displace=0, y_displace=0, kind="title"):
    textSurf, textRect = text_objects(msg, color, kind)

    textRect.center = (display_width / 2) + x_displace, (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    global intro
    intro = True

    while intro:

        quittaus()



        startScreenBackg = pygame.image.load("Backg.png")
        gameDisplay.blit(startScreenBackg, (0, 0))

        pygame.display.update()

        time.sleep(3)

        quittaus()




        message_to_screen("PELI",
                          red,
                          x_displace=0,
                          y_displace=-200,
                          kind="title")

        pygame.display.update()

        time.sleep(3)

        quittaus()

        message_to_screen("Paina ENTER, kun haluat aloittaa",
                          black,
                          x_displace=200,
                          y_displace=200,
                          kind="norm")
        pygame.display.update()



        alkuEnter()


def alkuEnter():
    global intro
    alkukysymys = True

    while alkukysymys:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
                    alkukysymys = False

def alku():

    alkuTausta = pygame.image.load("alkuTausta.png")
    gameDisplay.blit(alkuTausta, (0, 0))

    pygame.display.update()

    time.sleep(3)

    teksti_Laatikossa("Olet kämpässäsi. Kaikkialla on paskaista ja vituttaa", 20, 20)

    pygame.display.update()

    time.sleep(2)

    teksti_Laatikossa("Mitä teet?", 20, 60)

    tekstiBoksi()





    pygame.display.update()





def alkuLoop():

    alku = True

    while alku:

        x = input("kysymys")

        if x == "tutki":
            teksti_Laatikossa("Joka paikka on likainen, vihaat itseäsi ja asuntoasi.", 300, 300)
            alku = False
        else:
            teksti_Laatikossa()



        quittaus()




def splash():

    gameDisplay.fill(black)

    pygame.display.update()


    time.sleep(3)

    message_to_screen("Tervetuloa helevettiin",
                      red,
                      x_displace=0,
                      y_displace=0,
                      kind="title")

    pygame.display.update()

    time.sleep(3)




clock.tick(FPS)


game_intro()

splash()

alku()

alkuLoop()

time.sleep(3)

teksti_Laatikossa("Päätät nousta ylös ja tehdä jotain", 600,200)

input()
