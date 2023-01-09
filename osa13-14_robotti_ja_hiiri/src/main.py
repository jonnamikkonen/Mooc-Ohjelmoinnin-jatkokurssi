# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

leveys = robo.get_width()
korkeus = robo.get_height()

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEMOTION:
            kohde_x = tapahtuma.pos[0]-leveys/2
            kohde_y = tapahtuma.pos[1]-korkeus/2

            naytto.fill((0, 0, 0))
            naytto.blit(robo, (kohde_x, kohde_y))
            pygame.display.flip()

        if tapahtuma.type == pygame.QUIT:
            exit(0)


    

    kello.tick(60)