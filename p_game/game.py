# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:35:29 2019

@author: Naman
"""

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
bRed = (255, 0, 0)
bGreen = (0, 255, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')




def things(thingX, thingY, thingW, thingH, color ):
    pygame.draw.rect(gameDisplay, color, [thingX, thingY, thingW, thingH])

def text_objects(text, font, color = red):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text):
    font = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = (display_width/2), (display_height/2)
    gameDisplay.blit(TextSurf, TextRect)

def displayScore(dodge, crash):
    font = pygame.font.Font('freesansbold.ttf', 20)
    if not crash:
        TextSurf, TextRect = text_objects("Score: " + str(dodge), font, blue)
        TextRect.center = (display_width - 100), (10)
    else:
        TextSurf, TextRect = text_objects("Final Score: " + str(dodge), font, blue)
        TextRect.center = (display_width/2 - 30), (display_height/2 - 80)  
    gameDisplay.blit(TextSurf, TextRect)
        
def crash(dodge):
    
    pygame.display.update()
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()
            print(event)
            
        gameDisplay.fill(white)
        message_display('You Crashed !!!')
        displayScore(dodge, True)
        mouse = pygame.mouse.get_pos()
        
        #red button
        #def button(x,y,w,h,text,i,a):
        button(550,400,100,50,"Quit?",red,bRed,mouse,pygame.quit)
        #green button 
        button(150,400,100,50,"Play Again!!!",green,bGreen,mouse,gameLoop)
    
        
        pygame.display.update()
        clock.tick(15)

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def button(x,y,w,h,text,i,a,mouse, func):
     mouse = pygame.mouse.get_pos()
        
        #red button
     click = pygame.mouse.get_pressed()
     if x + w > mouse[0] > x and y + h > mouse[1] > y:  
         pygame.draw.rect(gameDisplay, a, (x , y , w , h))
         if click[0] == 1:
             func()
     else:
         pygame.draw.rect(gameDisplay, i, (x , y , w , h))
     font = pygame.font.Font('freesansbold.ttf', 15)
     TextSurf, TextRect = text_objects(text, font, black)
     TextRect.center = x+w/2, y+h/2
     gameDisplay.blit(TextSurf, TextRect)
def gameIntro():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()
            print(event)
            
        gameDisplay.fill(white)
        font = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Dodger", font)
        TextRect.center = (display_width/2), (display_height/2)
        gameDisplay.blit(TextSurf, TextRect)
        mouse = pygame.mouse.get_pos()
        
        #red button
        #def button(x,y,w,h,text,i,a):
        button(550,400,100,50,"Quit?",red,bRed,mouse,pygame.quit)
        #green button 
        button(150,400,100,50,"Go!!!",green,bGreen,mouse,gameLoop)
    
        
        pygame.display.update()
        clock.tick(15)
    
def gameLoop():

    x = (display_width *0.45)
    y = (display_height * 0.8)
    
    x_change = 0
    thingStartX = random.randrange(0,display_width-100)
    thingStartY = -600
    thingSpeed = 7
    thingW = 100
    thingH = 100 
    gameExit = False
    down = 0
    dodge = 0
    while not gameExit:
        for event in pygame.event.get():
            
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LEFT):
                    x_change = -7
                    down += 1
                if event.key == pygame.K_RIGHT:
                    x_change = +7
                    down += 1
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    down -= 1
                    if down < 0:
                        down = 0
                    if down == 0:
                        x_change = 0
            print(event)
            
        x += x_change
        
        if(x < 0 ) or x > display_width-73:
            crash(dodge)
        
        
        gameDisplay.fill(white)
        
        displayScore(dodge, False)
        
        things(thingStartX, thingStartY, thingW, thingH, blue)
        thingStartY += thingSpeed
        
        if(thingStartY > display_height):
            dodge = dodge + 1
            thingStartY = -600
            thingStartX = random.randrange(0,display_width-thingW)
        
        if y < thingStartY+thingH :
            print('y crossover')

            if x > thingStartX and x < thingStartX + thingW or x+73 > thingStartX and x + 73 < thingStartX +thingW:
                print('x crossover')
                crash(dodge)
        car(x, y)
        pygame.display.update()
        clock.tick(200)


gameIntro()

pygame.quit()
quit()






