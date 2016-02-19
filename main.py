import os
import pygame

pygame.init()

window_size = (640, 480)

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

    def set_tausta(self, tausta):
        self.tausta = tausta

    def get_tausta(self):
        return self.tausta

    def set_teksti(self, teksti):
        teksti = teksti
        self.teksti = teksti

    def get_teksti(self):
        return self.teksti

    def set_teksti_pinta(self, teksti_pinta_ja_sijainti):
        teksti_pinta, sijainti = teksti_pinta_ja_sijainti
        self.teksti_pinta = teksti_pinta
        self.teksti_sijainti = sijainti

    def get_teksti_pinta(self):
        return self.teksti_pinta, self.teksti_sijainti


class Pen:
    def __init__(self):
        pass

    def draw(self, screen, teksti, teksti_pinta_ja_sijainti, tausta):
        teksti_pinta = teksti_pinta_ja_sijainti[0]
        teksti_sijainti = teksti_pinta_ja_sijainti[1]
        screen.blit(tausta, (0, 0))
        screen.blit(teksti_pinta, teksti_sijainti)
    def render_teksti(self, fontti, teksti, vari=(0, 0, 0)):
        teksti_pinta = fontti.render(teksti, True, (vari))
        return teksti_pinta


ruutu = Ruutu(window_size)
oletus_fontti = pygame.font.get_default_font()
fontti = pygame.font.Font(oletus_fontti, 22)

punainen = (255, 0 , 0)

pen = Pen()

kuvien_tiedostonimet = {"eka": "Eka.png", "koti": "Koti.png"}
kuvat = {}

ruutu.set_teksti("jee")
ruutu.set_teksti_pinta((pen.render_teksti(fontti, ruutu.get_teksti(), punainen), (250, 250)))

print kuvien_tiedostonimet.items()

for avain, arvo in kuvien_tiedostonimet.items():
    tiedostonimi = os.path.join("Taustat", arvo)
    ladattu_kuva = pygame.image.load(tiedostonimi)
    kuvat[avain] = ladattu_kuva

print kuvat

ruutu.set_tausta(kuvat["eka"])

while True:

    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            elif event.key == pygame.K_RETURN:
                ruutu.set_tausta(kuvat["koti"])

    pen.draw(screen, ruutu.get_teksti(), ruutu.get_teksti_pinta(), ruutu.get_tausta())

    pygame.display.flip()
