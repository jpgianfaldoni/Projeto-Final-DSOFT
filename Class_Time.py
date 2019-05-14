#!/usr/bin/env python3
# -*- coding: utf-8 -
class Time:
        
    def __init__(self, jogadores, nome, pontos):
        self.jogadores = jogadores
        self.nome = nome
        self.pontos = pontos
        
    def calcula_ataque(self):
        ataque = 0
        for i in self.jogadores:
            ataque = ataque + i.ataque
        return ataque
    def calcula_defesa(self):
        defesa = 0
        for i in self.jogadores:
            defesa = defesa + i.defesa
        return defesa
    











