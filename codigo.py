#Beto na Guitarra
    
# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path
import time
import random
# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'imagens')

# Dados gerais do jogo.
WIDTH = 840 # Largura da tela
HEIGHT = 450 # Altura da tela
FPS = 60 # Frames por segundo

#pega tempo inicial
tempo_inicial = pygame.time.Clock()
# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Zumbie(pygame.sprite.Sprite):
    
    #Construtor
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        zumbie_img=pygame.image.load(path.join(img_dir, "zumbie.png")).convert()
        self.image=zumbie_img
        
        #Definindo posição do zumbie
        self.rect=self.image.get_rect()
        
        #Definindo tamanho do zumbie
        self.image=pygame.transform.scale(zumbie_img,(10,10))
        
        #Deixando Transparente
        self.image.set_colorkey(BLACK)
        
        #Definindo posição do zumbie como aleatório
        self.rect.x=random.randrange(WIDTH- self.rect.width)
        self.rect.bottom=random.randrange(-100,-40)
        self.rect.y=random.randrange(HEIGHT- self.rect.height)
        self.rect.bottom=random.randrange(-100,-40)
        #Definindo velociada do Zumbie
        self.speedx=random.randrange(-1,1)
        self.speedy=random.randrange(2,5)
        
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
class Shooter(pygame.sprite.Sprite):
    
    #Construtor
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        mob_img=pygame.image.load(path.join(img_dir, "soldier.jpg")).convert()
        mob_baixo=pygame.image.load(path.join(img_dir, "soldier_baixo.jpg")).convert()
        mob_esq=pygame.image.load(path.join(img_dir, "soldier_esquerda.jpg")).convert()
        mob_dir=pygame.image.load(path.join(img_dir, "soldier_direita.jpg")).convert()
       
        self.image=mob_img
        
        #Definindo posição do mob
        self.rect=self.image.get_rect()
        
        #Definindo tamanho do Mob
        self.image=pygame.transform.scale(mob_img,(10,10))
        
        #Deixando Transparente
        self.image.set_colorkey(BLACK)
        
        #Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        
        #Estabelecendo velocidades iniciais
        self.speedx=0
        self.speedy=0
        
     
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top= 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


#Iniciação do Pygame
pygame.init()

#Tamanho da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("BetoField")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, "imagem_fundo.png")).convert()
background_rect = background.get_rect()


# Comando para evitar travamentos.
background_rect=background.get_rect()

all_sprites=pygame.sprite.Group()


# Cria um grupo só dos meteoros
zumbies = Zumbie()
shooter=Shooter()
all_sprites.add(zumbies)
all_sprites.add(shooter)
try:
    #carregando sprites e cenário para o loop principal
        
    running = True
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    #Invertendo o display
    pygame.display.flip()
    # Loop principal.
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
        
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
         # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    Shooter.speedx = -5
                    Shooter.image= mob_esq
                if event.key == pygame.K_RIGHT:
                    Shooter.speedx = 5
                    Shooter.image= mob_dir
                if event.key == pygame.K_UP:
                    Shooter.speedy = -5
                    Shooter.image= mob_img
                if event.key == pygame.K_DOWN:
                    Shooter.speedx = 5
                    Shooter.image= mob_baixo
                # Se for um espaço atira!
                
                    
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    Shooter.speedx = 0
                if event.key == pygame.K_RIGHT:
                    Shooter.speedx = 0
                if event.key == pygame.K_UP:
                    Shooter.speedx = 0
                if event.key == pygame.K_DOWN:
                    Shooter.speedx = 0
        # A cada loop, redesenha o fundo e os sprites
        all_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)

        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()




