#Beto na Guitarra
    
# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'imagens')


# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, '"imagem_de_fundo.jpg"')).convert()
background_rect = background.get_rect()


