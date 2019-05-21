
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:14:42 2019

"""
from Class_Jogador import Jogador
from Class_Time import Time
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




def minuto_partida(time1, time2, contador):
    if contador % FPS == 0:
        if random.randint(0, (time1.calcula_ataque()+time2.calcula_defesa())) > time1.calcula_ataque():
            if random.randint(1,15)> 14:
                time1.gol += 1
        if random.randint(0, (time1.calcula_ataque()+time2.calcula_defesa())) <= time1.calcula_ataque():
            if random.randint(1,15)> 14:
                time2.gol += 1
    x = "x"
    placar = (time1.gol, x ,time2.gol)
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
time=["SP", "COR", "PAL", "SAN"]
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
        text = font.render(time[0], True, BLACK)    
        screen.blit(text, [500, 120])
        pygame.display.flip()
    
    if x==1:
        text = font.render(time[1], True, BLACK)    
        screen.blit(text, [500, 120])
        pygame.display.flip()     
        
    if x==2:
        text = font.render(time[2], True, BLACK)    
        screen.blit(text, [500, 120])
        pygame.display.flip()  
        
    if x==3: 
        text = font.render(time[3], True, BLACK)    
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
    pygame.display.flip()



def tela3(contador):
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
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 800, 600))
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 10, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 10, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 50, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 50, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 90, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 90, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 130, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300,130, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 170, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 170, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 210, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 210, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 250, 250,20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 250, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 290, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 290, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 330, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 330, 250, 20)) 
    pygame.draw.rect(screen, WHITE,pygame.Rect(10, 370, 250, 20))   
    pygame.draw.rect(screen, WHITE,pygame.Rect(300, 370, 250, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 10, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 10, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 50, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 50, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 90, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 90, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 130, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 130, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 170, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 170, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 210, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 210, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 250, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 250, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 290, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 290, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 330, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 330, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(260, 370, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(280, 370, 20, 20))
    pygame.draw.rect(screen, BLACK,pygame.Rect(620, 20, 120, 40))
    pygame.draw.rect(screen, BLACK,pygame.Rect(600, 100, 160, 140))
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(rodada1[0][0].nome), True, BLACK)
    screen.blit(text, [20, 9])
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(rodada1[0][1].nome), True, BLACK)
    screen.blit(text, [350, 9])
    font = pygame.font.SysFont(None, 20)
    text = font.render(str(minuto_partida(rodada1[0][0], rodada1[0][1], contador)), True, GREEN)
    screen.blit(text, [260, 12])
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(rodada1[1][0].nome), True, BLACK)
    screen.blit(text, [20, 50])
    font = pygame.font.SysFont(None, 35)
    text = font.render(str(rodada1[1][1].nome), True, BLACK)
    screen.blit(text, [350, 50])
    font = pygame.font.SysFont(None, 20)
    text = font.render(str(minuto_partida(rodada1[1][0], rodada1[1][1], contador)), True, GREEN)
    screen.blit(text, [260, 53])
#    
    pygame.display.flip()
    


    
    
telainicial=True 
teladois=True
telatres=True
clock = pygame.time.Clock()



contador = 0

try:
    
    # Loop principal.
    running = True
    while running:
        # Ajusta a velocidade do jogo.
        
        contador += 1
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
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
        if teladois == False:
            tela2()
        if telatres == False:
            tela3(contador)

        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
finally:
    pygame.quit()



            
    
     