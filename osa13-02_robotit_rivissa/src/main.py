# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))
leveys = robo.get_width()
korkeus = robo.get_height()
naytto.blit(robo, (50, 100))
naytto.blit(robo, (50+leveys, 100))
naytto.blit(robo, (50+leveys*2, 100))
naytto.blit(robo, (50+leveys*3, 100))
naytto.blit(robo, (50+leveys*4, 100))
naytto.blit(robo, (50+leveys*5, 100))
naytto.blit(robo, (50+leveys*6, 100))
naytto.blit(robo, (50+leveys*7, 100))
naytto.blit(robo, (50+leveys*8, 100))
naytto.blit(robo, (50+leveys*9, 100))
naytto.blit(robo, (50+leveys*10, 100))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()