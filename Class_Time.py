#!/usr/bin/env python3
# -*- coding: utf-8 -
from Class_Jogador import Jogadores


SaoPaulo = {'Tiago_Volpi': [10, 75, 42.5],
            'Hudson': [60, 60, 60.0],
            'Arboleda': [20, 70, 45.0],
            'Bruno_Alves': [10, 60, 35.0], 
            'Reinaldo': [50, 50, 50.0], 
            'Liziero': [40, 55, 47.5], 
            'Tche_Tche': [50, 50, 50.0], 
            'Everton': [55, 10, 32.5],
            'Anthony': [70, 10, 40.0], 
            'Toro': [60, 5, 32.5], 
            'Pato': [80, 5, 42.5]}

Santos = {'Vanderlei': [5, 80, 42.5], 
          'Felipe_Aguilar': [10, 70, 40.0], 
          'Lucas_Verissimo': [5, 65, 35.0], 
          'Gustavo_Henrique': [10, 70, 40.0], 
          'Victor_Ferraz': [50, 40, 45.0], 
          'Diego_Pituca': [50, 35, 42.5],
          'Carlos_Sanchez': [70, 40, 55.0], 
          'Jean_Mota': [60, 30, 45.0], 
          'Jorge': [50, 40, 45.0], 
          'Soteldo': [60, 5, 32.5], 
          'Rodrygo': [70, 10, 40.0]}

Palmeiras = {'Weverton': [5, 70, 37.5], 
             'Mayke': [40, 55, 47.5], 
             'Gustavo_Gomez': [15, 75, 45.0],
             'Luan': [10, 70, 40.0], 
             'Victor_Luis': [40, 45, 42.5],
             'Felipe_Melo': [35, 65, 50.0], 
             'Bruno_Henrique': [50, 50, 50.0], 
             'Ze_Rafael': [55, 30, 42.5], 
             'Gustavo_Scarpa': [70, 20, 45.0], 
             'Dudu': [80, 20, 50.0], 
             'Deyverson': [65, 10, 37.5]}

Corinthians = {'Cassio': [5, 70, 37.5], 
               'Fagner': [50, 50, 50.0], 
               'Henrique': [10, 60, 35.0],
               'Manoel': [5, 55, 30.0], 
               'Danilo_Avelar': [30, 30, 30.0], 
               'Ralf': [25, 55, 40.0], 
               'Richard': [30, 40, 35.0], 
               'Junior_Sornoza': [55, 25, 40.0], 
               'Clayson': [50, 5, 27.5], 
               'Pedrinho': [55, 5, 30.0], 
               'Gustavo': [55, 5, 30.0]}

class Time:
    
    ataque = 0
    defesa = 0
    overall = 0
    
    def __init__(self, ataque, defesa, overall):
        self.ataque = ataque
        self.defesa = defesa
        self.overall = overall
        
        
    def ataque_time(self):
        ataque = 0
        for k,v, in self.items():
            ataque = ataque + v[0]
        return ataque

    def defesa_time(self):
        defesa = 0
        for k,v, in self.items():
            defesa = defesa + v[1]
        return defesa
    
    def overall_time(self):
        overall = 0
        for k,v, in self.items():
            overall = overall + v[2]
        return overall

SaoPaulo = Time(505, 450, 477.5)
Palmeiras = Time(465, 510, 487.5)
Santos = Time(440, 485, 440)
Corinthians = Time(370,400,370)










