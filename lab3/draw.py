import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

# polygon(screen, (255, 255, 0), [(100,100), (200,50), (300,100), (100,100)])
circle(screen, (255, 255, 0), (220, 210), 150)
circle(screen, (0, 0, 0), (220, 210), 150, 5)

circle(screen, (0, 0, 0), (165, 175), 10)
circle(screen, (255, 0, 0), (165, 175), 20, 10)

circle(screen, (0, 0, 0), (280, 175), 10)
circle(screen, (255, 0, 0), (280, 175), 20, 10)

rect(screen, (0, 0, 0), (140, 280, 160, 20))

line(screen, (0, 0, 0), [50, 30], [200,150], 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()