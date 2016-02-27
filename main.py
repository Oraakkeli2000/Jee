import pygame
import sys
import random
import os

pygame.init()

ruudun_koko = (640, 480)

screen = pygame.display.set_mode(ruudun_koko)

clock = pygame.time.Clock()

taustakirjasto = {}

taustakuvat = ["Eka.png", "Koti.png"]

for kuva in taustakuvat:
    tausta = os.path.join("Taustat", kuva)

    taustakirjasto[kuva[:-4]] = pygame.image.load(tausta)

print taustakirjasto


class Ruutu:
    tausta = None
    tausta_sijainti = (0, 0)

    def __init__(self):
       pass


    def taustan_piirto(self, ruutu, taustakuva):
        ruutu.blit(taustakuva, (0, 0))


ruutu = Ruutu()



while True:

    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()



    ruutu.taustan_piirto(screen, taustakirjasto["Eka"])

    pygame.display.flip()

