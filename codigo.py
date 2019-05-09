#Beto na Guitarra
    
# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path
import time
# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'imagens')

# Dados gerais do jogo.
WIDTH = 600 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, "imagem_fundo.png")).convert()
background_rect = background.get_rect()



class Player(pygame.sprite.Sprite):
    
    #Construtor de classe
    def __init__(self):
        
        #Construtor da classe pai (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando a imagem de fundo
        player_img=pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()
        self.image = player_img
        
        #Diminuindo o tamanho da imagem
        self.image=pygame.transform.scale(player_img,(50,38))
        
        #Deixando transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhes sobre o posicionamento
        self.rect=self.image.get_rect()
        
        #Centraliza embaixo da tela
        self.rect.centerx= WIDTH / 2
        self.rect.bottom= HEIGHT - 10
        
        

        self.speedx=0
        
        #Melhora a colisão, trocando a colisão de retângulo para círculo
        self.radius=25
        
    def update(self):
        self.rect.x += self.speedx
        
        if self.rect.right> WIDTH:
            self.rect.right =WIDTH
        if self.rect.left<0:
            self.rect.left=0 

try:
    
    # Loop principal.
    running = True
    while running:
        
    
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()




