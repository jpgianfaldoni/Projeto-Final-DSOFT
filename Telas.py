# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:28:25 2019

@author: Joao
"""
FPS = 20
import pygame
import random
import json
from Class_Jogador import Jogador
from Class_Time import Time
from Funcoes import partida, minuto_partida, pontuacao, minuto
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
time=[SaoPaulo, Corinthians, Palmeiras, Santos]
x=random.randint(0,3)


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
    if x == 0:
        text = font.render(str(time[0].nome), True, BLACK)    
        screen.blit(text, [500, 120])
        pygame.display.flip()
    
    if x==1:
        text = font.render(str(time[1].nome), True, BLACK)    
        screen.blit(text, [500, 120])
        pygame.display.flip()     
        
    if x==2:
        text = font.render(str(time[2].nome), True, BLACK)    
        screen.blit(text, [500, 120])
        pygame.display.flip()  
        
    if x==3: 
        text = font.render(str(time[3].nome), True, BLACK)    
        screen.blit(text, [500, 120])
        pygame.display.flip()
    pygame.display.flip()

        
def tela2():    
    pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 800, 600))
    pygame.draw.rect(screen, WHITE, pygame.Rect(500, 0, 600, 800))
    pygame.draw.rect(screen, GREEN,pygame.Rect(550, 500, 200, 80) )   
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 500, 600))
    pygame.draw.rect(screen, BLUE3,pygame.Rect(550, 50, 200, 50) )   
    pygame.draw.rect(screen, BLUE4,pygame.Rect(550, 150, 200, 300) )   
    pygame.draw.rect(screen, BLACK,pygame.Rect(0, 0, 800, 30) )   
    pygame.draw.rect(screen, BLUE1,pygame.Rect(550, 150, 200, 300) ) 

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
    
    pygame.display.flip()
    

def tela3(contador):
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
    text = font.render(str(rodada1[0][0].nome), True, BLACK)
    screen.blit(text, [20, 9])
    
    
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(rodada1[0][1].nome), True, BLACK)
    screen.blit(text, [350, 9])
    
    
    font = pygame.font.SysFont(None, 30)  
    text = font.render(str(minuto_partida(rodada1[0][0], rodada1[0][1], contador)), True, GREEN)
    screen.blit(text, [245, 10])
    
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(rodada1[1][0].nome), True, BLACK)
    screen.blit(text, [20, 50])
    
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(rodada1[1][1].nome), True, BLACK)
    screen.blit(text, [350, 50])
    
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(minuto_partida(rodada1[1][0], rodada1[1][1], contador)), True, GREEN)
    screen.blit(text, [245, 50])
  
    pygame.display.flip()
    
def tela4(contador):
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
    text = font.render(str(rodada2[0][0].nome), True, BLACK)
    screen.blit(text, [20, 9])
    
    
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(rodada2[0][1].nome), True, BLACK)
    screen.blit(text, [350, 9])
    
    
    font = pygame.font.SysFont(None, 30)  
    text = font.render(str(minuto_partida(rodada2[0][0], rodada2[0][1], contador)), True, GREEN)
    screen.blit(text, [245, 10])
    
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(rodada2[1][0].nome), True, BLACK)
    screen.blit(text, [20, 50])
    
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(rodada2[1][1].nome), True, BLACK)
    screen.blit(text, [350, 50])
    
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(minuto_partida(rodada2[1][0], rodada2[1][1], contador)), True, GREEN)
    screen.blit(text, [245, 50])
  
    pygame.display.flip()
    
def tela5(contador):
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
    text = font.render(str(rodada3[0][0].nome), True, BLACK)
    screen.blit(text, [20, 9])
    
    
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(rodada3[0][1].nome), True, BLACK)
    screen.blit(text, [350, 9])
    
    
    font = pygame.font.SysFont(None, 30)  
    text = font.render(str(minuto_partida(rodada3[0][0], rodada3[0][1], contador)), True, GREEN)
    screen.blit(text, [245, 10])
    
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(rodada3[1][0].nome), True, BLACK)
    screen.blit(text, [20, 50])
    
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(rodada3[1][1].nome), True, BLACK)
    screen.blit(text, [350, 50])
    
    font = pygame.font.SysFont(None, 30)
    text = font.render(str(minuto_partida(rodada3[1][0], rodada3[1][1], contador)), True, GREEN)
    screen.blit(text, [245, 50])
  
    pygame.display.flip()