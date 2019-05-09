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
HEIGHT = 400 # Altura da tela
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



class Zumbie(pygame.sprite.Sprite):
    
    #Construtor
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        mob_img=pygame.image.load(path.join(img_dir, "zumbie.png")).convert()
        self.image=mob_img
        
        #Definindo posição do mob
        self.rect=self.image.get_rect()
        
        #Definindo tamanho do Mob
        self.image=pygame.transform.scale(mob_img,(50,38))
        
        #Deixando Transparente
        self.image.set_colorkey(BLACK)
        
        #Definindo posição do mob como aleatório
        self.rect.x=random.randrange(WIDTH- self.rect.width)
        self.rect.bottom=random.randrange(-100,-40)

        #Definindo velociada do MOB
        self.speedx=random.randrange(-3,3)
        self.speedy=random.randrange(2,9)
        
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

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




