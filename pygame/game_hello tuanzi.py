#coding:utf-8
import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((394,393),0,32)
pygame.display.set_caption("hello tuanzi")
background = pygame.image.load(r"C:\Users\sunnan\Desktop\20170220102558.jpg").convert()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background,(0,0))
    pygame.display.update()