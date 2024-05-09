import pygame

pygame.init()
screen = pygame.display.set_mode((400,400))
status = False

while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = True
    pygame.display.flip()
