# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))
leveys = robo.get_width()
korkeus = robo.get_height()

from random import randint

for i in range(1000):
    arvo_leveys = randint(0, 640-leveys)
    arvo_korkeus = randint(0, 480-korkeus)
    naytto.blit(robo, (arvo_leveys, arvo_korkeus))
    pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()