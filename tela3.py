#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:04:46 2019

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
    
  
    
    
    
    
    
    pygame.display.flip()