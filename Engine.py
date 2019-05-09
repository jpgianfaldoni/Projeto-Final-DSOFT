
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:14:42 2019

"""
from Class_Jogador import Jogador
from Class_Time import Time
import random



jogadores = []
for jogador in lista_jogadores:
    novo_jogador = Jogador(jogador["nome"], jogador["ataque"],jogador["defesa"], jogador["overall"])
    jogadores.append(novo_jogador)
    
    
SaoPaulo = Time(jogadores[0:11], "Sao Paulo")
Santos = Time(jogadores[11:22], "Santos")
print((SaoPaulo.calcula_ataque()))
print((Santos.calcula_ataque()))

def partida(time1, time2):
    i = 0
    time1.gol = 0
    time2.gol = 0
    while i <= 90:
        if random.randint(0, (time1.calcula_ataque()+time2.calcula_defesa())) > time1.calcula_ataque():
            if random.randint(1,15)> 14:
                time1.gol += 1
                print(i,"':","Gol do", time1.nome,"!")
                print(time1.gol, "x", time2.gol)
        if random.randint(0, (time1.calcula_ataque()+time2.calcula_defesa())) <= time1.calcula_ataque():
            if random.randint(1,15)> 14:
                time2.gol += 1
                print(i,"':","Gol do", time2.nome,"!")
                print(time1.gol, "x", time2.gol)
        i = i + 1

partida(SaoPaulo, Santos)





            
    
     