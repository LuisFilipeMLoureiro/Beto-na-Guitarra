#Beto na Guitarra
    
# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path
import time
import random
# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'imagens')
fnt_dir = path.join(path.dirname(__file__), 'font')
snd_dir = path.join(path.dirname(__file__), 'snd')

pygame.font.init()
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
       
#Criador de Score (fonte)
score_font = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
game_over_font = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 20)

class Zumbie(pygame.sprite.Sprite):
    
    #Construtor
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        zumbie_img=pygame.image.load(path.join(img_dir, "zumbie.png")).convert()
        self.image=zumbie_img
        #Definindo tamanho do zumbie
        self.image=pygame.transform.scale(zumbie_img,(30,30))
        #Definindo posição do zumbie
        self.rect=self.image.get_rect()
        
        
        #Deixando Transparente
        self.image.set_colorkey(BLACK)
        
        #Definindo posição do zumbie como aleatório
        LADO=random.randint(1,4)
        
        if LADO == 1:
            self.rect.bottom=random.randrange(0,HEIGHT)
            self.rect.right=random.randrange(-40,0)
        elif LADO ==2:
            self.rect.right=random.randrange(0,WIDTH)
            self.rect.bottom=random.randrange(-40,0)
        elif LADO ==3:
            self.rect.left=random.randrange(WIDTH,WIDTH + 40)
            self.rect.bottom=random.randrange(0,HEIGHT)
        elif LADO ==4:
            self.rect.left=random.randrange(0,WIDTH + 40)
            self.rect.bottom=random.randrange(HEIGHT, HEIGHT + 40)
        
        
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
class Ammo(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = ammo_box
        self.image=pygame.transform.scale(self.image,(20,20))
        self.image.set_colorkey(WHITE)
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        
class Medkit(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = kit_img
        self.image=pygame.transform.scale(self.image,(15,18))
        self.image.set_colorkey(WHITE)
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x           
# Classe Bullet que representa os tiros
class Bullet(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y, bullet_img,speedy,speedx):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        self.image = bullet_img

        # Deixando transparente.
        self.image.set_colorkey(WHITE)
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = speedy
        self.speedx = speedx

    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.top>HEIGHT:
            self.kill( )
        if self.rect.right < 0:
            self.kill()
        if self.rect.left>WIDTH:
            self.kill()


#Iniciação do Pygame
pygame.init()
pygame.mixer.init()
#Carrega a tela com esse tamanho
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Assets:
mob_img=pygame.image.load(path.join(img_dir, "sold_up.png")).convert()
mob_img = pygame.transform.scale(mob_img, (30, 30))        
mob_Img=mob_img.set_colorkey(WHITE)
bullet_image=pygame.image.load(path.join(img_dir, "balta_teste.png")).convert()
bullet_image = pygame.transform.scale(bullet_image, (10, 10))        
bullet_position=bullet_image
ammo_box=pygame.image.load(path.join(img_dir, "amo_box.png")).convert()
kit_img=pygame.image.load(path.join(img_dir, "med_kit.png")).convert()
SpeedyBull=-15
SpeedxBull=0

#sons do jogo:
pygame.mixer.music.load(path.join(snd_dir, 'Official Opening Credits Game of Thrones (HBO).wav'))
pygame.mixer.music.set_volume(0.8)
som_tiro1=pygame.mixer.Sound(path.join(snd_dir, 'bang2.ogg'))
som_tiro2=pygame.mixer.Sound(path.join(snd_dir, 'plaa.ogg'))
som_zumbi_morrendo1=pygame.mixer.Sound(path.join(snd_dir, 'zumbi_morrendo.ogg'))
som_zumbi_morrendo2=pygame.mixer.Sound(path.join(snd_dir, 'som_zm2.ogg'))
som_zumbi_morrendo3=pygame.mixer.Sound(path.join(snd_dir, 'som_zm3.ogg'))
morte=pygame.mixer.Sound(path.join(snd_dir, 'morte_conv.ogg'))
vida=pygame.mixer.Sound(path.join(snd_dir, 'vida.ogg'))
tictic=pygame.mixer.Sound(path.join(snd_dir, 'tiqtiq.ogg'))
sad_song=pygame.mixer.Sound(path.join(snd_dir, 'NARUTO FUNK - Sadness and Sorrow (PMM Funk Remix).ogg'))


# Nome do jogo
pygame.display.set_caption("BetoField")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, "imagem_fundo.png")).convert()
# Comando para evitar travamentos.
background_rect=background.get_rect()


#Adicionando os grupos das sprites
all_sprites=pygame.sprite.Group()
Jogadores=pygame.sprite.Group()
bullets = pygame.sprite.Group()
zombies = pygame.sprite.Group()
ammos = pygame.sprite.Group()
medkits = pygame.sprite.Group()
# Cria os zumbis
for i in range (10):
    zumbies = Zumbie()
    zombies.add(zumbies)
    all_sprites.add(zumbies)
    
shooter=Shooter()
Jogadores.add(shooter)
all_sprites.add(shooter)

try:
    #carregando sprites e cenário para o loop principal
    game_over=False
    running = True
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    #Invertendo o display
    pygame.display.flip()
    pygame.mixer.music.play(loops=-1)
    #Definindo variáveis
    score = 0
    lives = 3
    ammunition = 50
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
                    shooter.speedx -= 3
                if event.key == pygame.K_RIGHT:
                    shooter.speedx += 3
                if event.key == pygame.K_UP:
                    shooter.speedy -= 3
                if event.key == pygame.K_DOWN: 
                     shooter.speedy += 3
                # Se for um espaço atira!
                if event.key == pygame.K_SPACE and ammunition > 0:
                    bullet = Bullet(shooter.rect.centerx, shooter.rect.centery, bullet_position,SpeedyBull,SpeedxBull)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    ammunition -=1
                    #sorteia o som do tiro
                    sm=random.randrange(0,40)
                    if sm >= 20:
                        som_tiro1.play()
                    else:
                        som_tiro2.play()


                    
                    
                if event.key == pygame.K_p and lives>1:
                    lives-=1
                    ammunition += 15
                    

                    
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
        if shooter.speedx==0 and shooter.speedy<0:
            shooter.image=pygame.transform.rotate(mob_img,0)
            bullet_position=pygame.transform.rotate(bullet_image,0)
            SpeedyBull=-15
            SpeedxBull=0
        if shooter.speedx>0 and shooter.speedy<0:
            shooter.image=pygame.transform.rotate(mob_img,315)
            bullet_position=pygame.transform.rotate(bullet_image,315)
            SpeedyBull=-15
            SpeedxBull=15
        if shooter.speedx>0 and shooter.speedy==0:
            shooter.image=pygame.transform.rotate(mob_img,270)
            bullet_position=pygame.transform.rotate(bullet_image,270)
            SpeedyBull=0
            SpeedxBull=15
        if shooter.speedx>0 and shooter.speedy>0:
            shooter.image=pygame.transform.rotate(mob_img,225)
            bullet_position=pygame.transform.rotate(bullet_image,225)
            SpeedyBull=15
            SpeedxBull=15
        if shooter.speedx==0 and shooter.speedy>0:
            shooter.image=pygame.transform.rotate(mob_img,180)
            bullet_position=pygame.transform.rotate(bullet_image,180)
            SpeedyBull=15
            SpeedxBull=0
        if shooter.speedx<0 and shooter.speedy>0:
            shooter.image=pygame.transform.rotate(mob_img,135)
            bullet_position=pygame.transform.rotate(bullet_image,135)
            SpeedyBull=15
            SpeedxBull=-15
        if shooter.speedx<0 and shooter.speedy==0:
            shooter.image=pygame.transform.rotate(mob_img,90)
            bullet_position=pygame.transform.rotate(bullet_image,90)
            SpeedyBull=0
            SpeedxBull=-15
        if shooter.speedx<0 and shooter.speedy<0:
            shooter.image=pygame.transform.rotate(mob_img,45)
            bullet_position=pygame.transform.rotate(bullet_image,45)
            SpeedyBull=-15
            SpeedxBull=-15
                 # Se o tiro chegar no zumbie, byebye zumbie
        hits = pygame.sprite.groupcollide(zombies, bullets, True, True)
        if game_over == False:
            for hit in hits: # Pode haver mais de um
                sz=random.randrange(0,40)
                if sz >= 19 and sz <= 38:
                    som_zumbi_morrendo1.play()
                if sz < 19:
                    som_zumbi_morrendo2.play()
                if sz > 38:
                    som_zumbi_morrendo3.play()

                z = Zumbie() 
                all_sprites.add(z)
                zombies.add(z)
                score +=100
                am=random.randrange(0,30)
                if am == 1 or am==10:
                    x= Ammo(hit.rect.centerx,hit.rect.centery)
                    ammos.add(x)
                    all_sprites.add(x)
                if am == 2:
                    m= Medkit(hit.rect.centerx,hit.rect.centery)
                    medkits.add(m)
                    all_sprites.add(m) 
        hitz=pygame.sprite.groupcollide(Jogadores, ammos, False, True)
        for hit in hitz:
            ammunition +=15
            tictic.play()
        gethit=pygame.sprite.groupcollide(Jogadores,zombies, False, True)
        hitm1=pygame.sprite.groupcollide(Jogadores, medkits, False, True)
        for hit in hitm1:
                lives +=1
                vida.play()

        for hit in gethit:
            morte.play()
            lives -= 1
            z = Zumbie() 
            all_sprites.add(z)
            zombies.add(z)

        # A cada loop, redesenha o fundo e os sprites
        all_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
         
        # Desenha o score
        text_surface = score_font.render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        screen.blit(text_surface, text_rect) 
        
        text_surface = score_font.render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        screen.blit(text_surface, text_rect)
        
        text_surface = score_font.render("Ammo:{0}".format(ammunition), True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10,  HEIGHT- 35)
        screen.blit(text_surface, text_rect) 

        
        if lives<=0:
            game_over=True
            text_surface = score_font.render("GAME OVER", True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.bottomleft = ((WIDTH/2) - 140,  HEIGHT/2-20)
            screen.blit(text_surface, text_rect)
            
            text_surface =game_over_font.render("PRESSIONE ENTER PARA VOLTAR AO MENU", True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.bottomleft = ((WIDTH/2) - 400,  HEIGHT/2 +120)
            screen.blit(text_surface, text_rect)
            sad_song.play()
            
            if event.key == pygame.K_SPACE:
                running=False
            
            #Comando para caso o jogador pressione enter vá para menu
            #menu ainda está inacabado
            

        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
finally:
    pygame.quit()