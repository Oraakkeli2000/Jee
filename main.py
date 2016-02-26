# coding=utf-8
import os
import pygame

pygame.init()

# Pygame -ikkunan koko
window_size = (640, 480)

# Luodaan ikkuna.
screen = pygame.display.set_mode(window_size)

clock = pygame.time.Clock()


class Ruutu:
    tausta = None
    teksti = ""
    teksti_sijainti = (0, 0)
    teksti_pinta = None

    def __init__(self, ruudun_koko):
        self.tausta = pygame.Surface(ruudun_koko)
        self.tausta.fill((255, 255, 255))
        self.teksti_pinta = pygame.Surface(ruudun_koko)


class Pen:
    def __init__(self):
        pass

    def draw(self, screen, teksti_pinta, teksti_sijainti, tausta):
        screen.blit(tausta, (0, 0))
        screen.blit(teksti_pinta, teksti_sijainti)

    def render_teksti(self, fontti, teksti, vari=(0, 0, 0)):
        teksti_pinta = fontti.render(teksti, True, (vari))
        return teksti_pinta

# Luodaan ruutuobjekti
ruutu = Ruutu(window_size)

# Fonttimääritykset
oletus_fontti = pygame.font.get_default_font()
fontti = pygame.font.Font(oletus_fontti, 22)

punainen = (255, 0, 0)

pen = Pen()

kuvien_tiedostonimet = {"eka": "Eka.png",
                        "koti": "Koti.png"}
kuvat = {}

ruutu.teksti = "jee"
ruutu.teksti_pinta = pen.render_teksti(fontti, ruutu.teksti, punainen)
ruutu.teksti_sijainti = (250, 250)

# --------------------------------------------------------
print kuvien_tiedostonimet.items()

for avain, arvo in kuvien_tiedostonimet.items():
    tiedostonimi = os.path.join("Taustat", arvo)
    ladattu_kuva = pygame.image.load(tiedostonimi)
    kuvat[avain] = ladattu_kuva

print kuvat

# --------------------------------------------------------

ruutu.tausta = kuvat["eka"]

while True:

    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            elif event.key == pygame.K_RETURN:
                ruutu.tausta = kuvat["koti"]

    pen.draw(screen, ruutu.teksti_pinta, ruutu.teksti_sijainti, ruutu.tausta)

    pygame.display.flip()
