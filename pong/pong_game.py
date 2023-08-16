import pygame
import sys

from ball import Ball
from player import Player

pygame.init()#activando pygame

black = (0,0,0)#color de la pantalla
white = (255,255,255)#color de las lineas centrales

x = 800#ancho de la ventana
y = 600#largo de la ventana

size = (x,y)#dimensiones de la ventana

screen = pygame.display.set_mode(size)#habilitación de la ventana
clock = pygame.time.Clock()#control de FPS (Frames Per Second)
pygame.mouse.set_visible(0)#hacer invisible el raton

player1 = Player(15,280,12,21)
player2 = Player(785,280,12,779)
ball = Ball(395,295)

players = player1,player2

while True:
    
    for event in pygame.event.get():
        
        player1.movePlayer_conf1(event,pygame)
        player2.movePlayer_conf2(event,pygame)
    
        if event.type == pygame.QUIT:
            sys.exit()
    
    player1.movingPlayer(pygame)
    player2.movingPlayer(pygame)
    
    ball.moveBall(player1,player2)
    
    screen.fill(black)
    
    ball.drawBall(screen,pygame.draw.rect)
    
    player1.drawPlayer(screen,pygame.draw.line)
    player2.drawPlayer(screen,pygame.draw.line)
    
    for i in range(5,600,30):
        pygame.draw.line(screen,white,[398,i],[398,i+20],4)

    pygame.display.flip()
    
    clock.tick(60)