# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:27:38 2019

@author: Joao
"""
FPS = 20
import random
import json
from Class_Jogador import Jogador
from Class_Time import Time
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
    
    
SaoPaulo = Time(jogadores[0:11], "Sao Paulo", 0,0)
Santos = Time(jogadores[11:22], "Santos", 0,0)
Palmeiras = Time(jogadores[22:33], "Palmeiras", 0,0)
Corinthians = Time(jogadores[33:45], "Corinthians", 0,0)

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
contador = 0
rodada = 0
jogadores = []

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

def minuto_partida(time1, time2, contador):
    if contador % FPS == 0:
        if random.randint(0, (time1.calcula_ataque()+time2.calcula_defesa())) > time1.calcula_ataque():
            if random.randint(1,15)> 14:
                time1.gol += 1
        if random.randint(0, (time1.calcula_ataque()+time2.calcula_defesa())) <= time1.calcula_ataque():
            if random.randint(1,15)> 14:
                time2.gol += 1            
    return time1.gol,     time2.gol

def pontuacao(rodada):
    rodadas = [rodada1, rodada2, rodada3]
    if rodadas[rodada][0][1].gol > rodadas[rodada][0][0].gol:
        rodadas[rodada][0][1].pontos += 3
    if rodadas[rodada][0][0].gol > rodadas[rodada][0][1].gol:
        rodadas[rodada][0][0].pontos += 3
    if rodadas[rodada][0][0].gol == rodadas[rodada][0][1].gol:
        rodadas[rodada][0][0].pontos +=1
        rodadas[rodada][0][1].pontos +=1
    if rodadas[rodada][1][1].gol > rodadas[rodada][1][0].gol:
        rodadas[rodada][1][1].pontos += 3
    if rodadas[rodada][1][0].gol > rodada1[1][1].gol:
        rodadas[rodada][1][0].pontos += 3
    if rodadas[rodada][1][0].gol == rodada1[1][1].gol:
        rodadas[rodada][1][0].pontos +=1
        rodadas[rodada][1][1].pontos +=1
    rodadas[rodada][0][0].gol = 0
    rodadas[rodada][0][1].gol = 0
    rodadas[rodada][1][1].gol = 0
    rodadas[rodada][1][0].gol = 0
    
def minuto(contador):
    minuto = int(contador/2)
    return minuto  
