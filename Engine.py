
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:14:42 2019

"""
from Class_Jogador import Jogadores
from Class_Time import Time
import random


def partida(time1, time2):
    i = 0
    time1.gol = 0
    time2.gol = 0
    while i <= 90:
        if (time1.ataque) * random.randint(1,3) > time2.defesa * random.randint(1,3):
            if random.randint(1,15)> 14:
                time1.gol += 1
                print(i,"':","Gol do time1!")
                print(time1.gol, "x", time2.gol)
            if time2.ataque * random.randint(1,3) > time1.defesa * random.randint(1,3):
                if random.randint(1,15)> 14:
                    time2.gol += 1
                    print(i,"':","Gol do time2!")
                    print(time1.gol, "x", time2.gol)
        i = i + 1

partida(Corinthians, Santos)





            
    
     