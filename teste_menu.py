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
from codigo_2players import game_2player
from codigo import game_1player


pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Beto no tiro")

try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = menu(screen)
        if state == SOLO:
            state = game_1player(screen)
        if state == DUO:
            state = game_2player(screen)
        if state == QUIT:
            pygame.quit()
finally:
    pygame.quit()