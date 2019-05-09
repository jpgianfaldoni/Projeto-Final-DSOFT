#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:21:34 2019

@author: pedro
"""

import pygame

pygame.init()
screen= pygame.display.set_mode((800, 600))
done=False
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (24,116,205,255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)   
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done =True

   
    
    pygame.draw.rect(screen, WHITE, pygame.Rect(500, 0, 600, 800))
    
    
    pygame.draw.rect(screen, GREEN,pygame.Rect(550, 500, 200, 80) )   
    
    
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 500, 600))
    
    
    pygame.draw.rect(screen, BLACK,pygame.Rect(550, 50, 200, 50) )   
    
    
    pygame.draw.rect(screen, RED,pygame.Rect(550, 150, 200, 300) )   
   

    pygame.draw.rect(screen, BLACK,pygame.Rect(0, 0, 800, 30) )   
    pygame.display.flip()
    
    pygame.draw.rect(screen, RED,pygame.Rect(550, 150, 200, 300) ) 
    pygame.display.flip()
    