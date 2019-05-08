#!/usr/bin/env python3
# -*- coding: utf-8 -
from Class_Jogador import Jogadores


SaoPaulo = {
        Tiago_Volpi : [Tiago_Volpi.ataque, Tiago_Volpi.defesa, Tiago_Volpi.overall],
        Hudson : [Hudson.ataque, Hudson.defesa, Hudson.overall],
        Arboleda : [Arboleda.ataque, Arboleda.defesa, Arboleda.overall],
        Bruno_Alves : [Bruno_Alves.ataque, Bruno_Alves.defesa, Bruno_Alves.overall],
        Reinaldo : [Reinaldo.ataque, Reinaldo.defesa, Reinaldo.overall],
        Liziero : [Liziero.ataque, Liziero.defesa, Liziero.overall],
        Tche_Tche : [Tche_Tche.ataque, Tche_Tche.defesa, Tche_Tche.overall],
        Everton : [Everton.ataque, Everton.defesa, Everton.overall],
        Anthony : [Anthony.ataque, Anthony.defesa, Anthony.overall],
        Toro : [Toro.ataque, Toro.defesa, Toro.overall],
        Pato : [Pato.ataque, Pato.defesa, Pato.overall]
        }

Santos = {
        Vanderlei : [Vanderlei.ataque, Vanderlei.defesa, Vanderlei.overall],
        Felipe_Aguilar : [Felipe_Aguilar.ataque, Felipe_Aguilar.defesa, Felipe_Aguilar.overall],
        Lucas_Verissimo : [Lucas_Verissimo.ataque, Lucas_Verissimo.defesa, Lucas_Verissimo.overall],
        Gustavo_Henrique : [Gustavo_Henrique.ataque, Gustavo_Henrique.defesa, Gustavo_Henrique.overall],
        Victor_Ferraz : [Victor_Ferraz.ataque, Victor_Ferraz.defesa, Victor_Ferraz.overall],
        Diego_Pituca : [Diego_Pituca.ataque, Diego_Pituca.defesa, Diego_Pituca.overall],
        Carlos_Sanchez : [Carlos_Sanchez.ataque, Carlos_Sanchez.defesa, Carlos_Sanchez.overall],
        Jean_Mota : [Jean_Mota.ataque, Jean_Mota.defesa, Jean_Mota.overall],
        Jorge : [Jorge.ataque, Jorge.defesa, Jorge.overall],
        Soteldo : [Soteldo.ataque, Soteldo.defesa, Soteldo.overall],
        Rodrygo : [Rodrygo.ataque, Rodrygo.defesa, Rodrygo.overall],
        }

Palmeiras = {
        Weverton : [Weverton.ataque, Weverton.defesa, Weverton.overall],
        Mayke : [Mayke.ataque, Mayke.defesa, Mayke.overall],
        Gustavo_Gomez : [Gustavo_Gomez.ataque, Gustavo_Gomez.defesa, Gustavo_Gomez.overall],
        Luan : [Luan.ataque, Luan.defesa, Luan.overall],
        Victor_Luis : [Victor_Luis.ataque, Victor_Luis.defesa, Victor_Luis.overall],
        Felipe_Melo : [Felipe_Melo.ataque, Felipe_Melo.defesa, Felipe_Melo.overall],
        Bruno_Henrique : [Bruno_Henrique.ataque, Bruno_Henrique.defesa, Bruno_Henrique.overall],
        Ze_Rafael : [Ze_Rafael.ataque, Ze_Rafael.defesa, Ze_Rafael.overall],
        Gustavo_Scarpa : [Gustavo_Scarpa.ataque, Gustavo_Scarpa.defesa, Gustavo_Scarpa.overall],
        Dudu : [Dudu.ataque, Dudu.defesa, Dudu.overall],
        Deyverson : [Deyverson.ataque, Deyverson.defesa, Deyverson.overall],
        }

Corinthians = {
        Cassio : [Cassio.ataque, Cassio.defesa, Cassio.overall],
        Fagner : [Fagner.ataque, Fagner.defesa, Fagner.overall],
        Henrique : [Henrique.ataque, Henrique.defesa, Henrique.overall],
        Manoel : [Manoel.ataque, Manoel.defesa, Manoel.overall],
        Danilo_Avelar : [Danilo_Avelar.ataque, Danilo_Avelar.defesa, Danilo_Avelar.overall],
        Ralf : [Ralf.ataque, Ralf.defesa, Ralf.overall],
        Richard : [Richard.ataque, Richard.defesa, Richard.overall],
        Junior_Sornoza : [Junior_Sornoza.ataque, Junior_Sornoza.defesa, Junior_Sornoza.overall],
        Clayson : [Clayson.ataque, Clayson.defesa, Clayson.overall],
        Pedrinho : [Pedrinho.ataque, Pedrinho.defesa, Pedrinho.overall],
        Gustavo : [Gustavo.ataque, Gustavo.defesa, Gustavo.overall],
        }

class Time:
    
    ataque = 0
    defesa = 0
    overall = 0
    
    def __init__(self, ataque, defesa, gol):
        self.ataque = ataque
        self.defesa = defesa
        self.gol = gol
        
        
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
    
SaoPaulo = Time((ataque_time(SaoPaulo)),(defesa_time(SaoPaulo)),(overall_time(SaoPaulo)))
Palmeiras = Time((ataque_time(Palmeiras)),(defesa_time(Palmeiras)),(overall_time(Palmeiras)))
Santos = Time((ataque_time(Santos)),(defesa_time(Santos)),(overall_time(Santos)))
Corinthians = Time((ataque_time(Corinthians)),(defesa_time(Corinthians)),(overall_time(Corinthians)))





