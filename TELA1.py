#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:39:29 2019

@author: pedro
"""

import pygame

pygame.init()
screen= pygame.display.set_mode((800, 600))
done=False
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)   
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done =True

    pygame.draw.rect(screen, GREEN,pygame.Rect(300, 450, 200, 80) )   
    pygame.display.flip()

    pygame.draw.rect(screen, BLUE,pygame.Rect(0, 0, 400, 100) )   
    pygame.display.flip()


    pygame.draw.rect(screen, BLUE,pygame.Rect(400, 0, 400, 100) )   
    pygame.display.flip()

    pygame.draw.rect(screen, GREEN,pygame.Rect(0, 450, 200, 80) )   
    pygame.display.flip()