
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:14:42 2019

"""
from Class_Jogador import Jogador
from Class_Time import Time
import random
from itertools import permutations 
import json
with open('dicionario.txt','r') as arquivo:
    conteudo = arquivo.read()

dicionario = json.loads(conteudo)
for k, v, in dicionario.items():
    lista_jogadores = v

jogadores = []
for jogador in lista_jogadores:
    novo_jogador = Jogador(jogador["nome"], jogador["ataque"],jogador["defesa"], jogador["overall"])
    jogadores.append(novo_jogador)
    
    
SaoPaulo = Time(jogadores[0:11], "Sao Paulo", 0)
Santos = Time(jogadores[11:22], "Santos", 0)
Palmeiras = Time(jogadores[22:33], "Palmeiras", 0)
Corinthians = Time(jogadores[33:45], "Corinthians", 0)


def partida(time1, time2):
    i = 0
    time1.gol = 0
    time2.gol = 0
    vencedor = 0
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
        
    if time1.gol > time2.gol:
        vencedor = time1
    elif time2.gol > time1.gol:
        vencedor = time2
    else:
        vencedor = "empate"
    return vencedor






def minuto_partida(time1, time2):
    time1.gol = 0
    time2.gol = 0
    if random.randint(0, (time1.calcula_ataque()+time2.calcula_defesa())) > time1.calcula_ataque():
        if random.randint(1,15)> 14:
            time1.gol += 1
    if random.randint(0, (time1.calcula_ataque()+time2.calcula_defesa())) <= time1.calcula_ataque():
        if random.randint(1,15)> 14:
            time2.gol += 1
    placar = (time1.gol, "x" ,time2.gol)
    return placar


times=[SaoPaulo, Corinthians, Santos, Palmeiras]
rodada1 = []
rodada2 = []
rodada3 = []
rodada1.append([times[0], times[3]])
rodada1.append([times[1], times[2]])
rodada2.append([times[3], times[1]])
rodada2.append([times[2], times[0]])
rodada3.append([times[0], times[1]])
rodada3.append([times[2], times[3]])

def matchups(times):
    
    rod1=[]
    j1=[]
    j2=[]
   
    j1.append(times[0])
    j1.append(times[3])
    j2.append(times[1])
    j2.append(times[2])
    
    rod1.append(j1)
    rod1.append(j2)
    
    rod2=[]

    j3=[]
    j4=[]
    j3.append(times[3])
    j3.append(times[1])
    j4.append(times[2])
    j4.append(times[0])
    
    rod2.append(j3)
    rod2.append(j4)

    
    rod3=[]
    j5=[]
    j6=[]
    
    j5.append(times[0])
    j5.append(times[1])
    j6.append(times[2])
    j6.append(times[3])
    
    rod3.append(j5)
    rod3.append(j6)
     
    return rod1, rod2, rod3


def rodada(y):
    jogo1 = minuto_partida(y[0][0],y[0][1])
    jogo2 = minuto_partida(y[1][0], y[1][1])
    return jogo1, jogo2

print(minuto_partida(Santos, Corinthians))




            
    
     