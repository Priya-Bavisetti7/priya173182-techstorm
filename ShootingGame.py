import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((800,600))
running=True
font = pygame.font.SysFont('Arial',32, 'bold')
pygame.display.set_caption("Space Shooter Game")
icon=pygame.image.load('shuttle.png')
pygame.display.set_icon(icon)
background=pygame.image.load('backgroundspace.jpg')
playerImage=pygame.image.load('space.png')
alienImage = []
alienx = []
alieny=[]
alienspeedx=[]
alienspeedy=[]
no_of_aliens = 6 
for i in range(no_of_aliens):
    alienImage.append(pygame.image.load('ufo.png'))
    alienx.append(random.randint(0,736))
    alieny.append(random.randint(30,150))
    alienspeedx.append(-0.5)
    alienspeedy.append(40)
bulletImage= pygame.image.load('bullet.png')
spaceshipx=370
spaceshipy=480
changeX=0
bulletx = 386
bullety=450
score = 0
check = False
def score_text():
    img = font.render(f"score: {score}",True,'white')
    screen.blit(img,(10,10))
def game_over():
    img_gameover = font_gameover.render("GAME OVER",True,'white')
    screen.blit(img_gameover,(200,250))
font_gameover = pygame.font.SysFont('Arial',64, 'bold')
while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                changeX=-1
            if event.key==pygame.K_RIGHT:
                changeX=1
            if event.key == pygame.K_SPACE:
                if check is False:
                    check = True
                    bulletx=spaceshipx+16
        if event.type==pygame.KEYUP:
            changeX=0
    spaceshipx+=changeX
    # This allow my spaceship to not to go outside of my window
    if(spaceshipx<=0):
        spaceshipx=0
    elif(spaceshipx>736):
        spaceshipx=736
    for i in range(no_of_aliens):
        if alieny[i]>420:
            for j in range(no_of_aliens):
                alieny[j] = 2000
            game_over()
            break
        alienx[i]+=alienspeedx[i]
        if(alienx[i]<=0):
            alienspeedx[i]=0.4
            alieny[i]+=alienspeedy[i]
        if(alienx[i]>=736):
            alienspeedx[i]=-0.4
            alieny[i]+=alienspeedy[i]
        distance = math.sqrt(math.pow(bulletx-alienx[i],2)+math.pow(bullety-alieny[i],2))
        if distance<27:
            bullety=480
            check = False
            alienx[i]=random.randint(0,736)
            alieny[i]=random.randint(30,150)
            score += 1
        screen.blit(alienImage[i],(alienx[i],alieny[i]))
    if bullety<=0:
        bullety=490
        check = False
    if check is True:
        screen.blit(bulletImage,(bulletx,bullety))
        bullety-=1
    
    screen.blit(playerImage,(spaceshipx,spaceshipy))
    
    score_text()
    pygame.display.update()
