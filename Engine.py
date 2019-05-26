
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:14:42 2019

"""
import pygame
from Class_Jogador import Jogador
from Class_Time import Time
from itertools import cycle , islice, chain
import random
import json
with open('dicionariocompleto.txt','r') as arquivo:
    conteudo = arquivo.read()

dicionario = json.loads(conteudo)
for k, v, in dicionario.items():
    lista_jogadores = v

jogadores = []
for jogador in lista_jogadores:
    novo_jogador = Jogador(jogador["nome"], jogador["ataque"],jogador["defesa"], jogador["overall"])
    jogadores.append(novo_jogador)
    
    
SaoPaulo = Time(jogadores[0:11], "Sao Paulo", 0,0,0,0)
Santos = Time(jogadores[11:22], "Santos", 0,0,0,0)
Palmeiras = Time(jogadores[22:33], "Palmeiras", 0,0,0,0)
Corinthians = Time(jogadores[33:44], "Corinthians", 0,0,0,0)
AtleticoMG = Time(jogadores[44:55], "Atletico MG", 0,0,0,0)
Cruzeiro = Time(jogadores[55:66], "Cruzeiro", 0,0,0,0)
Internacional = Time(jogadores[66:77], "Internacional", 0,0,0,0)
Gremio = Time(jogadores[77:88], "Gremio", 0,0,0,0)
CSA = Time(jogadores[88:99], "CSA", 0,0,0,0)
Fortaleza = Time(jogadores[99:110], "Fortaleza", 0,0,0,0)

time=[SaoPaulo, Corinthians, Palmeiras, Santos, AtleticoMG, Internacional, Cruzeiro, CSA, Fortaleza, Gremio]
def calcula_ataque_defesa(time):
    ataques = []
    defesas = []
    for i in time:
        i.ataque = i.calcula_ataque()
        ataques.append(i.ataque)
        i.defesa = i.calcula_defesa()
        defesas.append(i.defesa)
    return ataques, defesas
calcula_ataque_defesa(time)
print(calcula_ataque_defesa(time))

ataques_iniciais = [495, 365, 460, 440, 380, 385, 375, 340, 350, 395] 
defesas_iniciais = [460, 410, 515, 485, 385, 385, 420, 415, 410, 390]



def cria_lista_rodadas(time):
    items = list(time)
    if len(items) % 2 != 0:
        items.append(None)
    fixed = items[:1]
    cyclers = cycle(items[1:])
    rounds = len(items) - 1
    npairs = len(items) // 2
    return [
        list(zip(
            chain(fixed, islice(cyclers, npairs-1)),
            reversed(list(islice(cyclers, npairs)))
        ))
        for _ in range(rounds)
        for _ in [next(cyclers)]
    ]


def minuto_partida(time1, time2, contador):
    if contador % FPS == 0:
        if random.randint(0, (time1.ataque+time2.defesa)) > time1.ataque:
            if random.randint(1,15)> 12:
                time1.gol += 1
        if random.randint(0, (time1.ataque+time2.defesa)) <= time1.ataque:
            if random.randint(1,15)> 12:
                time2.gol += 1            
    return time1.gol,     time2.gol

def pontuacao(rodada):
    rodadas = [rodada1, rodada2, rodada3, rodada4, rodada5]
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
    if rodadas[rodada][2][1].gol > rodadas[rodada][1][0].gol:
        rodadas[rodada][2][1].pontos += 3
    if rodadas[rodada][2][0].gol > rodada1[1][1].gol:
        rodadas[rodada][2][0].pontos += 3
    if rodadas[rodada][2][0].gol == rodada1[1][1].gol:
        rodadas[rodada][2][0].pontos +=1
        rodadas[rodada][2][1].pontos +=1
    if rodadas[rodada][3][1].gol > rodadas[rodada][1][0].gol:
        rodadas[rodada][3][1].pontos += 3
    if rodadas[rodada][3][0].gol > rodada1[1][1].gol:
        rodadas[rodada][3][0].pontos += 3
    if rodadas[rodada][3][0].gol == rodada1[1][1].gol:
        rodadas[rodada][3][0].pontos +=1
        rodadas[rodada][3][1].pontos +=1
    if rodadas[rodada][4][1].gol > rodadas[rodada][1][0].gol:
        rodadas[rodada][4][1].pontos += 3
    if rodadas[rodada][4][0].gol > rodada1[1][1].gol:
        rodadas[rodada][4][0].pontos += 3
    if rodadas[rodada][4][0].gol == rodada1[1][1].gol:
        rodadas[rodada][4][0].pontos +=1
        rodadas[rodada][4][1].pontos +=1

        
    rodadas[rodada][0][0].gol = 0
    rodadas[rodada][0][1].gol = 0
    rodadas[rodada][1][1].gol = 0
    rodadas[rodada][1][0].gol = 0
    rodadas[rodada][2][1].gol = 0
    rodadas[rodada][2][0].gol = 0
    rodadas[rodada][3][1].gol = 0
    rodadas[rodada][3][0].gol = 0
    rodadas[rodada][4][1].gol = 0
    rodadas[rodada][4][0].gol = 0
    




####################################TELAS##########################################################



FPS = 20
pygame.init()
screen= pygame.display.set_mode((800, 600))
pygame.display.set_caption("ELIFOOT")
done=False
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  100,  100, 255)
BLUE1=(  0,  100, 255)
BLUE2=(  1,  100, 255)
BLUE3=(  10,  100, 255)
BLUE4=(  100,  0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)  
LEFT=1
x=random.randint(0,9)
pontos_times = [SaoPaulo.pontos, Corinthians.pontos, Santos.pontos, Palmeiras.pontos, Gremio.pontos, Internacional.pontos, AtleticoMG.pontos, Cruzeiro.pontos, Fortaleza.pontos, CSA.pontos]     
classificacao = sorted(pontos_times)
lista_rodadas = cria_lista_rodadas(time)
rodada1 = lista_rodadas[0]
rodada2 = lista_rodadas[1]
rodada3 = lista_rodadas[2]
rodada4 = lista_rodadas[3]
rodada5= lista_rodadas[4]
rodada6 = lista_rodadas[5]
rodada7 = lista_rodadas[6]
rodada8 = lista_rodadas[7]
rodada9 = lista_rodadas[8]
todas_rodadas = [rodada1, rodada2, rodada3, rodada4, rodada5, rodada6, rodada7, rodada8, rodada9]
rodada = 0


def relaciona(classificacao):
    pontostimes = []
    for i in classificacao:
        if SaoPaulo.nome not in pontostimes and SaoPaulo.pontos == i:
            pontostimes.append(SaoPaulo.nome)
        if Palmeiras.nome not in pontostimes and Palmeiras.pontos == i:
            pontostimes.append(Palmeiras.nome)
        if Corinthians.nome not in pontostimes and Corinthians.pontos == i:
            pontostimes.append(Corinthians.nome)
        if Santos.nome not in pontostimes and Santos.pontos == i:
            pontostimes.append(Santos.nome)
        if AtleticoMG.nome not in pontostimes and AtleticoMG.pontos == i:
            pontostimes.append(AtleticoMG.nome)
        if Internacional.nome not in pontostimes and Internacional.pontos == i:
            pontostimes.append(Internacional.nome)
        if Cruzeiro.nome not in pontostimes and Cruzeiro.pontos == i:
            pontostimes.append(Cruzeiro.nome)
        if CSA.nome not in pontostimes and CSA.pontos == i:
            pontostimes.append(CSA.nome)
        if Fortaleza.nome not in pontostimes and Fortaleza.pontos == i:
            pontostimes.append(Fortaleza.nome)
        if Gremio.nome not in pontostimes and Gremio.pontos == i:
            pontostimes.append(Gremio.nome)
        
    return pontostimes
        
classificacao_times = relaciona(classificacao)


        
        
        
def minuto(contador):
    minuto = int(contador/2)
    return minuto   
        
        
def tela1():
        
    pygame.mouse.set_visible(True)
    screen.fill(BLUE2)
    pygame.draw.rect(screen, GREEN,pygame.Rect(300, 500, 200, 80) )   

    pygame.draw.rect(screen, BLACK,pygame.Rect(0, 0, 400, 100) )   


    pygame.draw.rect(screen, BLACK,pygame.Rect(400, 0, 400, 100) )   

   
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(0, 100, 400, 60) )   
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(0, 220, 400, 60) )   
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(0, 340, 400, 60) )   
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(400, 100, 400, 60) )   
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(400, 220, 400, 60) )   
    
    pygame.draw.rect(screen, WHITE,pygame.Rect(400, 340, 400, 60) )   
    pygame.display.flip()

    
    #textos
    font = pygame.font.SysFont(None, 50)
    text = font.render('INICIAR', True, WHITE)    
    screen.blit(text, [335, 520])
    pygame.display.flip()
    text = font.render('Pedro', True, BLACK)    
    screen.blit(text, [120, 114])
    pygame.display.flip()
   
    text = font.render('PLAYER', True, WHITE)    
    screen.blit(text, [100, 50])
    pygame.display.flip()
    
    text = font.render('TIME', True, WHITE)    
    screen.blit(text, [500, 50])
    text = font.render(str(time[x].nome), True, BLACK)    
    screen.blit(text, [500, 120])
    pygame.display.flip()
    pygame.display.flip()
        
def tela2(classificacao, classificacao_times):    
    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 800, 600))
    pygame.draw.rect(screen, WHITE, pygame.Rect(500, 0, 600, 800))   
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 500, 600))
    pygame.draw.rect(screen, BLUE3,pygame.Rect(550, 50, 200, 50) )   
    pygame.draw.rect(screen, BLUE4,pygame.Rect(550, 150, 200, 300) )   
    pygame.draw.rect(screen, BLACK,pygame.Rect(0, 0, 800, 30) )   
    pygame.draw.rect(screen, BLUE1,pygame.Rect(550, 150, 200, 300) ) 
    pygame.draw.rect(screen, GREEN,pygame.Rect(10, 500, 100, 60) )
    pygame.draw.rect(screen, GREEN,pygame.Rect(180, 500, 100, 60) )
    pygame.draw.rect(screen, GREEN,pygame.Rect(360, 500, 100, 60) )

    font = pygame.font.SysFont(None, 40)
    text = font.render(str(time[x].nome), True, WHITE)
    screen.blit(text, [300, 8])
    
    font = pygame.font.SysFont(None, 40)
    text = font.render("Jogadores", True, RED)
    screen.blit(text, [10, 30])
    
    font = pygame.font.SysFont(None, 40)
    text = font.render("Atq", True, RED)
    screen.blit(text, [265, 30])
    
    
    font = pygame.font.SysFont(None, 40)
    text = font.render("Def", True, RED)
    screen.blit(text, [350, 30])
    
    font = pygame.font.SysFont(None, 40)
    text = font.render("OV", True, RED)
    screen.blit(text, [420, 30])
    


    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[0].nome), True, WHITE)
    screen.blit(text, [10, 80])
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[1].nome), True, WHITE)
    screen.blit(text, [10, 100])
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[2].nome), True, WHITE)
    screen.blit(text, [10, 120])
         
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[3].nome), True, WHITE)
    screen.blit(text, [10, 140])
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[4].nome), True, WHITE)
    screen.blit(text, [10, 160])
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[5].nome), True, WHITE)
    screen.blit(text, [10, 180])
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[6].nome), True, WHITE)
    screen.blit(text, [10, 200])
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[7].nome), True, WHITE)
    screen.blit(text, [10, 220])
    
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[8].nome), True, WHITE)
    screen.blit(text, [10, 240])
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[9].nome), True, WHITE)
    screen.blit(text, [10, 260])    
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[10].nome), True, WHITE)
    screen.blit(text, [10, 280])
        #ATQ
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[0].ataque), True, WHITE)
    
    screen.blit(text, [280, 80])
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[1].ataque), True, WHITE)
    screen.blit(text, [280, 100])
        
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[2].ataque), True, WHITE)
    screen.blit(text, [280, 120])
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[3].ataque), True, WHITE)
    screen.blit(text, [280, 140])
    
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[4].ataque), True, WHITE)
    screen.blit(text, [280, 160])
    
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[5].ataque), True, WHITE)
    screen.blit(text, [280, 180])    
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[6].ataque), True, WHITE)
    screen.blit(text, [280, 200])    
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[7].ataque), True, WHITE)
    screen.blit(text, [280, 220])    
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[8].ataque), True, WHITE)
    screen.blit(text, [280, 240])    
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[9].ataque), True, WHITE)
    screen.blit(text, [280, 260])    
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[10].ataque), True, WHITE)
    screen.blit(text, [280, 280])    
        
    
        #DEF
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[0].defesa), True, WHITE)
    screen.blit(text, [350, 80])

    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[1].defesa), True, WHITE)
    screen.blit(text, [350, 100])
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[2].defesa), True, WHITE)
    screen.blit(text, [350, 120])
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[3].defesa), True, WHITE)
    screen.blit(text, [350, 140])
        
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[4].defesa), True, WHITE)
    screen.blit(text, [350, 160])
        
    
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[5].defesa), True, WHITE)
    screen.blit(text, [350, 180])
    
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[6].defesa), True, WHITE)
    screen.blit(text, [350, 200])
    
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[7].defesa), True, WHITE)
    screen.blit(text, [350, 220])
    
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[8].defesa), True, WHITE)
    screen.blit(text, [350, 240])
    
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[9].defesa), True, WHITE)
    screen.blit(text, [350, 260])
    
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[10].defesa), True, WHITE)
    screen.blit(text, [350, 280])
        
    #OV
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[0].overall), True, WHITE)
    screen.blit(text, [420, 80])
    
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[1].overall), True, WHITE)
    screen.blit(text, [420, 100])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[2].overall), True, WHITE)
    screen.blit(text, [420, 120])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[3].overall), True, WHITE)
    screen.blit(text, [420, 140])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[4].overall), True, WHITE)
    screen.blit(text, [420, 160])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[5].overall), True, WHITE)
    screen.blit(text, [420, 180])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[6].overall), True, WHITE)
    screen.blit(text, [420, 200])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[7].overall), True, WHITE)
    screen.blit(text, [420, 220])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[8].overall), True, WHITE)
    screen.blit(text, [420, 240])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[9].overall), True, WHITE)
    screen.blit(text, [420, 260])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(time[x].jogadores[10].overall), True, WHITE)
    screen.blit(text, [420, 280])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(classificacao[0]), True, BLACK)
    screen.blit(text, [700, 430])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(classificacao_times[0]), True, BLACK)
    screen.blit(text, [560, 430])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(classificacao[1]), True, BLACK)
    screen.blit(text, [700, 400])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(classificacao_times[1]), True, BLACK)
    screen.blit(text, [560, 400])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(classificacao[2]), True, BLACK)
    screen.blit(text, [700, 370])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(classificacao_times[2]), True, BLACK)
    screen.blit(text, [560, 370])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(classificacao[3]), True, BLACK)
    screen.blit(text, [700, 340])
    text = font.render(str(classificacao_times[3]), True, BLACK)
    screen.blit(text, [560, 340])
    text = font.render(str(classificacao[4]), True, BLACK)
    screen.blit(text, [700, 310])
    text = font.render(str(classificacao_times[4]), True, BLACK)
    screen.blit(text, [560, 310])
    text = font.render(str(classificacao[5]), True, BLACK)
    screen.blit(text, [700, 280])
    text = font.render(str(classificacao_times[5]), True, BLACK)
    screen.blit(text, [560, 280])
    text = font.render(str(classificacao[6]), True, BLACK)
    screen.blit(text, [700, 250])
    text = font.render(str(classificacao_times[6]), True, BLACK)
    screen.blit(text, [560, 250])
    text = font.render(str(classificacao[7]), True, BLACK)
    screen.blit(text, [700, 220])
    text = font.render(str(classificacao_times[7]), True, BLACK)
    screen.blit(text, [560, 220])
    text = font.render(str(classificacao[8]), True, BLACK)
    screen.blit(text, [700, 190])
    text = font.render(str(classificacao_times[8]), True, BLACK)
    screen.blit(text, [560, 190])
    text = font.render(str(classificacao[9]), True, BLACK)
    screen.blit(text, [700, 160])
    text = font.render(str(classificacao_times[9]), True, BLACK)
    screen.blit(text, [560, 160])

    pygame.draw.rect(screen, GREEN,pygame.Rect(10, 500, 100, 60) )
    pygame.draw.rect(screen, GREEN,pygame.Rect(180, 500, 100, 60) )
    pygame.draw.rect(screen, GREEN,pygame.Rect(360, 500, 100, 60) )
    
    font = pygame.font.SysFont(None, 50)
    text = font.render("4-4-2", True, WHITE)
    screen.blit(text, [180, 510])
    pygame.display.flip()
    
    font = pygame.font.SysFont(None, 50)
    text = font.render("4-5-1", True, WHITE)
    screen.blit(text, [360, 510])
    pygame.display.flip()
  
    font = pygame.font.SysFont(None, 50)
    text = font.render("4-3-3", True, WHITE)
    screen.blit(text, [10, 510])
    pygame.display.flip()
    
    font = pygame.font.SysFont(None, 30)
    text = font.render("Clique na formacao escolhida para iniciar o jogo", True, WHITE)
    screen.blit(text, [10, 450])
    pygame.display.flip()
    

def tela3(todas_rodadas, rodada, contador):
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 800, 600))
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 10, 240, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 10, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 50, 240, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 50, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 90, 240, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 90, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 130, 240, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300,130, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 170, 240, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 170, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 210, 240, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 210, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 250, 240,20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 250, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 290, 240, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 290, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 330, 240, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 330, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 370, 240, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 370, 250, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(240, 10, 60, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(240, 50, 60, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(240, 90, 60, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(240, 130, 60, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(240, 170, 60, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(240, 210, 60, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(240, 250, 60, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(240, 290, 60, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(240, 330, 60, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(240, 370, 60, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(640, 20, 55, 50))
    pygame.draw.rect(screen, BLACK,pygame.Rect(600, 100, 160, 140))
    
    font = pygame.font.SysFont(None, 25)
    text = font.render("X", True, GREEN)
    screen.blit(text, [263, 15])
    screen.blit(text, [263, 55])
    
    
    font = pygame.font.SysFont(None, 50)
    text = font.render(str(minuto(contador)), True, WHITE)
    screen.blit(text, [650, 30])
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(todas_rodadas[rodada][0][0].nome), True, BLACK)
    screen.blit(text, [20, 9])
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(todas_rodadas[rodada][0][1].nome), True, BLACK)
    screen.blit(text, [350, 9])
    font = pygame.font.SysFont(None, 30)  
    text = font.render(str(minuto_partida(todas_rodadas[rodada][0][0], todas_rodadas[rodada][0][1], contador)), True, GREEN)
    screen.blit(text, [245, 10])
    
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(todas_rodadas[rodada][1][0].nome), True, BLACK)
    screen.blit(text, [20, 50])
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(todas_rodadas[rodada][1][1].nome), True, BLACK)
    screen.blit(text, [350, 50])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(minuto_partida(todas_rodadas[rodada][1][0], todas_rodadas[rodada][1][1], contador)), True, GREEN)
    screen.blit(text, [245, 50])
    
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(todas_rodadas[rodada][2][0].nome), True, BLACK)
    screen.blit(text, [20, 90])
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(todas_rodadas[rodada][2][1].nome), True, BLACK)
    screen.blit(text, [350, 90])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(minuto_partida(todas_rodadas[rodada][2][0], todas_rodadas[rodada][2][1], contador)), True, GREEN)
    screen.blit(text, [245, 90])
    
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(todas_rodadas[rodada][3][0].nome), True, BLACK)
    screen.blit(text, [20, 130])
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(todas_rodadas[rodada][3][1].nome), True, BLACK)
    screen.blit(text, [350, 130])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(minuto_partida(todas_rodadas[rodada][3][0], todas_rodadas[rodada][3][1], contador)), True, GREEN)
    screen.blit(text, [245, 130])
    
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(todas_rodadas[rodada][4][0].nome), True, BLACK)
    screen.blit(text, [20, 170])
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(todas_rodadas[rodada][4][1].nome), True, BLACK)
    screen.blit(text, [350, 170])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(minuto_partida(todas_rodadas[rodada][4][0], todas_rodadas[rodada][4][1], contador)), True, GREEN)
    screen.blit(text, [245, 170])
    
  
    pygame.display.flip()
    
    
    

def telaFINAL():
    screen.fill(BLUE4)
    pygame.draw.rect(screen, WHITE,pygame.Rect(100, 80, 600, 400)) 
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(classificacao[0]), True, BLACK)
    screen.blit(text, [600, 400])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(classificacao_times[0]), True, BLACK)
    screen.blit(text, [460, 400])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(classificacao[1]), True, BLACK)
    screen.blit(text, [600, 350])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(classificacao_times[1]), True, BLACK)
    screen.blit(text, [460, 350])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(classificacao[2]), True, BLACK)
    screen.blit(text, [600, 300])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(classificacao_times[2]), True, BLACK)
    screen.blit(text, [460, 300])
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(classificacao[3]), True, BLACK)
    screen.blit(text, [600, 250])
    text = font.render(str(classificacao_times[3]), True, BLACK)
    screen.blit(text, [460, 250])
    font=pygame.font.SysFont(None, 60)
    text = font.render("CAMPEAO - {}".format(classificacao_times[3]), True, GREEN)
    screen.blit(text, [120, 100])
    font=pygame.font.SysFont(None, 20)
    text = font.render("VICE-CAMPEAO - {}".format(classificacao_times[2]), True, BLACK)
    screen.blit(text, [123, 140])
    pygame.display.flip()
    
    
telainicial=True 
teladois=True
telatres=True
telaquatro = True
telacinco = True
telafinal=True
clock = pygame.time.Clock()
contador = 0
print(calcula_ataque_defesa(time))
escolha_tatica = True
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
                print(time[x].ataque)
                print(time[x].defesa)

                
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
        if teladois == False:
            tela2(classificacao, classificacao_times)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos <= (110,560) and event.pos >=(10,500):
                    time[x].ataque += 50
                    time[x].defesa -= 30
                    print(time[x].ataque)
                    print(time[x].defesa)
                    telainicial = False
                    teladois = True
                    telatres = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos <= (280,560) and event.pos >=(180,500):
                    time[x].ataque += 15
                    time[x].defesa -= 0
                    print(time[x].ataque)
                    print(time[x].defesa)
                    telainicial = False
                    teladois = True
                    telatres = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos <= (460,560) and event.pos >=(360,500):
                    time[x].ataque -= 10
                    time[x].defesa += 60
                    print(time[x].ataque)
                    print(time[x].defesa)
                    telainicial = False
                    teladois = True
                    telatres = False
                    
        if telatres == False:
            tela3(todas_rodadas, rodada, contador)
            contador += 1
        if telafinal ==False:
            telaFINAL()
            
        if contador == 180:
            teladois = False
            telatres = True
            telainicial = False
            contador = 0
            pontuacao(rodada)
            pontos_times = [SaoPaulo.pontos, Corinthians.pontos, Santos.pontos, Palmeiras.pontos, Gremio.pontos, Internacional.pontos, AtleticoMG.pontos, Cruzeiro.pontos, Fortaleza.pontos, CSA.pontos]     
            classificacao = sorted(pontos_times)
            time[x].ataque = ataques_iniciais[x]
            time[x].defesa = defesas_iniciais[x]
            print(time[x].ataque)
            print(time[x].defesa)
            classificacao_times = relaciona(classificacao)
            tela2(classificacao, classificacao_times)
            
            rodada += 1
            if rodada ==5: 
                telafinal=False
                teladois = True




        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
finally:
    pygame.quit()



     