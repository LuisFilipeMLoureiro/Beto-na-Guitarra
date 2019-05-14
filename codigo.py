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
WIDTH = 846 # Largura da tela
HEIGHT = 469 # Altura da tela
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
        self.image=pygame.transform.scale(zumbie_img,(30,30))
        
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
        
        self.image=mob_img
        
        #Definindo tamanho do Mob
        self.image=pygame.transform.scale(mob_img,(30,30))
        
        #Definindo posição do mob
        self.rect=self.image.get_rect()
        
        #Deixando Transparente
        self.image.set_colorkey(WHITE)
        
        #Centraliza na tela.
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        
        #Estabelecendo velocidades iniciais
        self.speedx=0
        self.speedy=0
        
     
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top= 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

# Classe Bullet que representa os tiros
class Bullet(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y, bullet_img):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        self.image = bullet_img

        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.y += self.speedy
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
#Iniciação do Pygame
pygame.init()
#Carrega a tela com esse tamanho
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Posições dos soldados
mob_img=pygame.image.load(path.join(img_dir, "sold_up.png")).convert()

mob_baixo=pygame.image.load(path.join(img_dir, "sold_bottom.png")).convert()
mob_esq=pygame.image.load(path.join(img_dir, "sold_left.png")).convert()
mob_dir=pygame.image.load(path.join(img_dir, "sold_right.png")).convert()
bullet_image=pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()

# Nome do jogo
pygame.display.set_caption("BetoField")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, "imagem_fundo.png")).convert()




# Comando para evitar travamentos.
background_rect=background.get_rect()

all_sprites=pygame.sprite.Group()
bullets = pygame.sprite.Group()

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
                    shooter.speedx -= 5
                    shooter.image=pygame.transform.rotate(mob_img,90)
                if event.key == pygame.K_RIGHT:
                    shooter.speedx += 5
                    shooter.image=pygame.transform.rotate(mob_img,270)
                if event.key == pygame.K_UP:
                    shooter.speedy -= 5
                    shooter.image=pygame.transform.rotate(mob_img,0)
                if event.key == pygame.K_DOWN:
                    shooter.speedy += 5
                    shooter.image=pygame.transform.rotate(mob_img,180)
                # Se for um espaço atira!
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(shooter.rect.centerx, shooter.rect.top, bullet_image)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    shooter.speedx += 5
                    
                if event.key == pygame.K_RIGHT:
                    shooter.speedx -= 5
                if event.key == pygame.K_UP:
                    shooter.speedy += 5
                if event.key == pygame.K_DOWN:
                    shooter.speedy -= 5
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




