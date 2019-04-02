# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 18:06:44 2019

@author: Naman
"""
import pygame

pygame.init()


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(black)


pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green

pygame.draw.line(gameDisplay, blue, (100,200), (500, 500), 10)

pygame.draw.rect(gameDisplay, red, (40,40,199,199))

pygame.draw.circle(gameDisplay, white, (90,500),75 )

pygame.draw.polygon(gameDisplay, green, ((25,75) , (760,123) , (231,312) , (552,231)))

while(True):
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    pygame.display.update()
