# -*- coding: utf-8 -*-
"""
Created on Wed May 22 14:05:14 2019

@author: W10
"""
#eficiencia energetica da geotermica
import pygame
from os import path
import time
import random
from configuracoes import INIT,SOLO,DUO,QUIT, menu, WIDTH,HEIGHT,FPS
from teste_2players_projeto import game_2player
from teste_local_projeto import game_1player


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Beto no tiro")

try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = menu(screen)
        elif state == SOLO:
            state = game_1player(screen)
        elif state == DUO:
            state = game_2player(screen)
        else:
            state = QUIT
finally:
    pygame.quit()