
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:14:42 2019

@author: Joao
"""
from Class_Jogador import Jogadores
import random

S




i = 0
while i <= 90:
    if (Santos.ataque) * random.randint(1,3) > Santos2.defesa * random.randint(1,3):
        if random.randint(1,15)> 14:
            Santos.gol += 1
            print(i,"':","Gol do Santos!")
            print(Santos.gol, "x", Santos2.gol)
    if Santos2.ataque * random.randint(1,3) > Santos.defesa * random.randint(1,3):
        if random.randint(1,15)> 14:
            Santos2.gol += 1
            print(i,"':","Gol do Santos 2!")
            print(Santos.gol, "x", Santos2.gol)
    i = i + 1






            
    
     