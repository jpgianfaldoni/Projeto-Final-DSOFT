
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:14:42 2019

@author: Joao
"""
from Class_Jogador import Jogadores
import random
class Time:
    
    def __init__(self, ataque, defesa, gol):
        self.ataque = ataque
        self.defesa = defesa
        self.gol = gol
        
    def read_number(self):
        print(self.ataque)
        print(self.defesa)
        
Santos = Time(((Felipe_Aguilar.ataque + Vanderlei.ataque + Lucas_Verissimo.ataque)/3 ),((Vanderlei.defesa + Felipe_Aguilar.defesa + Lucas_Verissimo.defesa)/3),0)
Santos2 = Time(((Gustavo_Henrique.ataque +Victor_Ferraz.ataque + Diego_Pituca.ataque)/3),((Gustavo_Henrique.defesa +Victor_Ferraz.defesa + Diego_Pituca.defesa)/3),0)




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






            
    
     