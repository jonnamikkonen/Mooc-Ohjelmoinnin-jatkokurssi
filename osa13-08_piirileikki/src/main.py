# TEE RATKAISUSI TÄHÄN:
import pygame
import math

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

kulma = 0
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    x = 320+math.cos(kulma)*100-robo.get_width()/2
    y = 240+math.sin(kulma)*100-robo.get_height()/2

    naytto.fill((0, 0, 0))
    for i in range(10):
        naytto.blit(robo, (x, y))
        pygame.display.flip()

        kulma += 0.01
        kello.tick(60)