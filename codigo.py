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
        self.speedx=1
        self.speedy=1
        
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        if shooter.rect.x > self.rect.x:
            self.rect.x += self.speedx
        if shooter.rect.x < self.rect.x:
            self.rect.x -= self.speedx
        if shooter.rect.y > self.rect.y:
            self.rect.y += self.speedy
        if shooter.rect.y < self.rect.y:
            self.rect.y -= self.speedy
        
class Shooter(pygame.sprite.Sprite):
    
    #Construtor
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image=mob_img
        
        
        #Definindo posição do mob
        self.rect=self.image.get_rect()
        


        
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
    def __init__(self, x, y, bullet_img,speedy,speedx):
        
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
        self.speedy = SpeedyBull
        self.speedx = SpeedxBull

    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
#Iniciação do Pygame
pygame.init()
#Carrega a tela com esse tamanho
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Assets:
mob_img=pygame.image.load(path.join(img_dir, "sold_up.png")).convert()
mob_img = pygame.transform.scale(mob_img, (30, 30))        
mob_Img=mob_img.set_colorkey(WHITE)
bullet_image=pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()
bullet_position=bullet_image
keys = pygame.key.get_pressed()
SpeedyBull=-15
SpeedxBull=0

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
zombies = pygame.sprite.Group()
# Cria um grupo só dos meteoros
for i in range (10):
    zumbies = Zumbie()
    zombies.add(zumbies)
    all_sprites.add(zumbies)
    
shooter=Shooter()

all_sprites.add(shooter)

#Direções do Shooter:
d=1

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
                if keys [pygame.K_LEFT] and keys [pygame.K_UP]:
                    shooter.image=pygame.transform.rotate(mob_img,45)
                    SpeedyBull=-15
                    SpeedxBull=-15
                if keys [pygame.K_LEFT] and keys [pygame.K_DOWN]:
                    shooter.image=pygame.transform.rotate(mob_img,135)
                    SpeedyBull=15
                    SpeedxBull=-15
                if keys [pygame.K_RIGHT] and keys [pygame.K_UP]:
                    shooter.image=pygame.transform.rotate(mob_img,315)
                    SpeedyBull=-15
                    SpeedxBull=15
                if keys [pygame.K_RIGHT] and keys [pygame.K_UP]:
                    shooter.image=pygame.transform.rotate(mob_img,225)
                    SpeedyBull=15
                    SpeedxBull=15
                if event.key == pygame.K_LEFT and event.key != pygame.K_DOWN and event.key != pygame.K_UP:
                    shooter.image=pygame.transform.rotate(mob_img,90)
                    bullet_position=pygame.transform.rotate(bullet_image,90)
                    SpeedyBull=0
                    SpeedxBull=-15
                    shooter.speedx -= 3
                if event.key == pygame.K_RIGHT and event.key != pygame.K_DOWN and event.key != pygame.K_UP:
                    shooter.image=pygame.transform.rotate(mob_img,270)
                    bullet_position=pygame.transform.rotate(bullet_image,270)
                    SpeedyBull=0
                    SpeedxBull=15
                    shooter.speedx += 3
                if event.key == pygame.K_UP and not event.key == pygame.K_LEFT and not event.key == pygame.K_RIGHT:
                    shooter.image=pygame.transform.rotate(mob_img,0)
                    bullet_position=pygame.transform.rotate(bullet_image,0)
                    SpeedyBull=-15
                    SpeedxBull=0
                    shooter.speedy -= 3
                if event.key == pygame.K_DOWN and not event.key == pygame.K_LEFT and not event.key == pygame.K_RIGHT:
                     shooter.image=pygame.transform.rotate(mob_img,180)
                     bullet_position=pygame.transform.rotate(bullet_image,180)
                     SpeedyBull=15
                     SpeedxBull=0
                     shooter.speedy += 3
                
                # Se for um espaço atira!
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(shooter.rect.centerx, shooter.rect.centery, bullet_position,SpeedyBull,SpeedxBull)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    shooter.speedx += 3
                if event.key == pygame.K_RIGHT:
                    shooter.speedx -= 3
                if event.key == pygame.K_UP:
                    shooter.speedy += 3
                if event.key == pygame.K_DOWN:
                    shooter.speedy -= 3
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




