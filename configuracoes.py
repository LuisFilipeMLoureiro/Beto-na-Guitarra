# -*- coding: utf-8 -*-
"""
Created on Thu May 23 14:36:16 2019

@author: W10
"""
import pygame
from os import path
import time
import random
#pygame.init()   
#pygame.font.init()
QUIT=3
INIT=10
SOLO=1
DUO=2
WIDTH = 846 # Largura da tela
HEIGHT = 469 # Altura da tela
FPS = 60 # Frames por segundo
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
#screen = pygame.display.set_mode((WIDTH,HEIGHT))
MENU=0
state=MENU
img_dir = path.join(path.dirname(__file__), 'imagens')
fnt_dir = path.join(path.dirname(__file__), 'font')
    # Comando para evitar travamentos.
def menu(screen):
    background = pygame.image.load(path.join(img_dir, "imagem_fundo.png")).convert()
    background_rect = background.get_rect()
    state=MENU
    while state == MENU:
        screen.blit(background,background_rect)
        score_font = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 50)
        text_surface = score_font.render("Beto no tiro", True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (150,  HEIGHT/2)
        screen.blit(text_surface, text_rect)
        score_font = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
        text_surface = score_font.render("Aperte 1 para jogar solo", True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (50,  HEIGHT- 68)
        screen.blit(text_surface, text_rect)
        score_font = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
        text_surface = score_font.render("Aperte 2 para jogar duo", True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (50,  HEIGHT- 35)
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    state = SOLO
                if event.key == pygame.K_2:
                    state = DUO
        pygame.display.flip()
    return(state)
#try:
   # menu(screen)
#finally:
   # pygame.quit()