
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:14:42 2019

"""
import pygame
from Class_Jogador import Jogador
from Class_Time import Time
from Funcoes import partida, minuto_partida, pontuacao, minuto
from Telas import tela1, tela2, tela3, tela4, tela5
import random
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





####################################TELAS##########################################################

 
    
telainicial=True 
teladois=True
telatres=True
telaquatro = True
telacinco = True
clock = pygame.time.Clock()


contador = 0
rodada = 0

try:
    
    # Loop principal.
    running = True
    while running:
        # Ajusta a velocidade do jogo.
        
        clock.tick(FPS)
        if telainicial == True:
            tela1()
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos <= (500,580) and event.pos >=(300,500) and teladois == True:
                telainicial = False
                teladois = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos <= (750,600) and event.pos >=(500,580):
                telainicial = False
                teladois = True
                telatres = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos <= (750,600) and event.pos >=(500,580) and rodada ==1:
                telainicial = False
                teladois = True
                telatres = True
                telaquatro = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos <= (750,600) and event.pos >=(500,580) and rodada ==2:
                telainicial = False
                teladois = True
                telatres = True
                telaquatro = True
                telacinco = False
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
        if teladois == False:
            tela2()
        if telatres == False:
            tela3(contador)
            contador += 1
        if telaquatro == False:
            tela4(contador)
            contador += 1
        if telacinco == False:
            tela5(contador)
            contador += 1
        if contador == 180:
            tela2()
            teladois = False
            telatres = True
            telainicial = False
            telaquatro = True
            telacinco = True
            contador = 0
            pontuacao(rodada)
            rodada += 1

        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
finally:
    pygame.quit()

print(rodada1[0][1].pontos)
print(rodada1[0][0].pontos)
print(rodada1[1][0].pontos)
print(rodada1[1][1].pontos)
            
    
     