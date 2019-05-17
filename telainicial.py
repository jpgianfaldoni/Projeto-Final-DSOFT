#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:39:29 2019

@author: pedro
"""

import pygame
import random

pygame.init()
screen= pygame.display.set_mode((800, 600))
pygame.display.set_caption("ELIFOOT")
done=False
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)  
LEFT=1 
def tela1():
        
    pygame.mouse.set_visible(True)
    pygame.draw.rect(screen, GREEN,pygame.Rect(300, 500, 200, 80) )   

    pygame.draw.rect(screen, RED,pygame.Rect(0, 0, 400, 100) )   


    pygame.draw.rect(screen, RED,pygame.Rect(400, 0, 400, 100) )   

   
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(0, 100, 400, 60) )   
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(0, 220, 400, 60) )   
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(0, 340, 400, 60) )   
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(400, 160, 400, 60) )   
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(400, 280, 400, 60) )   
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(400, 400, 400, 60) )   
    pygame.display.flip()
    
    
    
    #textos
    font = pygame.font.SysFont(None, 50)
    text = font.render('INICIAR', True, WHITE)    
    screen.blit(text, [335, 520])
    pygame.display.flip()
    text = font.render('Pedro', True, BLACK)    
    screen.blit(text, [120, 114])
    pygame.display.flip()
   
    
def tela2():    
    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 800, 600))
    pygame.draw.rect(screen, WHITE, pygame.Rect(500, 0, 600, 800))
    
    
    pygame.draw.rect(screen, GREEN,pygame.Rect(550, 500, 200, 80) )   
    
    
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 500, 600))
        
    
    pygame.draw.rect(screen, BLACK,pygame.Rect(550, 50, 200, 50) )   
        
    
    pygame.draw.rect(screen, RED,pygame.Rect(550, 150, 200, 300) )   
   
    pygame.draw.rect(screen, BLACK,pygame.Rect(0, 0, 800, 30) )   
   
    
    pygame.draw.rect(screen, RED,pygame.Rect(550, 150, 200, 300) ) 
    pygame.display.flip()


def tela3():
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 800, 600))
    
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 10, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 10, 250, 20)) 
    
     
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 50, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 50, 250, 20)) 
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 90, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 90, 250, 20))   
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 130, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300,130, 250, 20)) 
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 170, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 170, 250, 20)) 
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 210, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 210, 250, 20)) 
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 250, 250,20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 250, 250, 20)) 
   
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 290, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 290, 250, 20)) 
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 330, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 330, 250, 20)) 
   
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 370, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 370, 250, 20))
    
    #time 1
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 10, 20, 20))
    #time 2
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 10, 20, 20))
    
    #time 1
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 50, 20, 20))
    #time 2
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 50, 20, 20))
        
    #time 1
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 90, 20, 20))
    #time 2
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 90, 20, 20))

    #time 1
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 130, 20, 20))
    #time 2
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 130, 20, 20))

    #time 1
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 170, 20, 20))
    #time 2
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 170, 20, 20))

    #time 1
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 210, 20, 20))
    #time 2
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 210, 20, 20))

    #time 1
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 250, 20, 20))
    #time 2
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 250, 20, 20))

    #time 1
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 290, 20, 20))
    #time 2
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 290, 20, 20))

    #time 1
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 330, 20, 20))
    #time 2
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 330, 20, 20))

    #time 1
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 370, 20, 20))
    #time 2
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 370, 20, 20))
    #Tempo de jogo
    pygame.draw.rect(screen, BLACK,pygame.Rect(620, 20, 120, 40))
    #Texto de lances
    pygame.draw.rect(screen, BLACK,pygame.Rect(600, 100, 160, 140))
    font = pygame.font.SysFont(None, 35)
    text = font.render('Corinthians', True, BLACK)
    screen.blit(text, [20, 12])
#    tempo=pygame.time.Clock(1000)
#    text = font.render(tempo, True, BLACK)
#    screen.blit(text, [20, 12])
#    
    pygame.display.flip()
    
def sorteiotimes():
    font = pygame.font.SysFont(None, 50)
    time=['corinthians', 'sao paulo']
    x=random.randint(0,1)
    text = font.render(time[x], True, BLACK)    
    screen.blit(text, [400, 160])
    pygame.display.flip()
    
telainicial=True 
teladois=True
telatres=False
 
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done =True
        
        if telainicial==True:
            tela1()
            sorteiotimes()
                    
   
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos <= (500,580) and event.pos >=(300,500) and teladois == True:
            telainicial=False
            teladois = False
            tela2()
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos <= (750,600) and event.pos >=(500,580):
            telainicial=False
            
            tela3()
            


    