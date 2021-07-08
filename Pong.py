# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:45:28 2021

el juego tendrá variables como que si te da una bola maligna t 
encoja la plataforma o te quedes bloqueado

2 jugadores w,s y uparrow, downarrow


@author: Silvia
"""

import pygame, sys 
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import Player1, Player2

pygame.init()
clock = pygame.time.Clock()

wHeight = 400
wWidth = 600

#Variables de teclado
arrowUpDown = False
arrowDownDown = False
wDown = False
sDown = False




window  = pygame.display.set_mode((wWidth ,wHeight))
pygame.display.set_caption(":Pong")





J1 = Player1.Player1(wWidth, wHeight)
J2 = Player2.Player2(wWidth, wHeight)

# Variables de jugadores
X1= J1.posX 
Y1 = J1.posY
sizeWide1 = J1.sizeWide
sizeLong1 = J1.sizeLong
    
    
X2 = J2.posX 
Y2 = J2.posY
sizeWide2 = J2.sizeWide
sizeLong2 = J2.sizeLong

moveSpeed = J1.moveSpeed




def QuitGame():
    pygame.quit()
    sys.exit()
    




while True:
    
    window.fill((0,0,0))
    
    
   
    
    pygame.draw.rect(window, (255, 255, 255), (X1, Y1, sizeWide1, sizeLong1))
    pygame.draw.rect(window,(0, 255, 255), (X2, Y2, sizeWide2, sizeLong2))
    
    
    
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                arrowUpDown = True
            if event.key == pygame.K_DOWN:
                arrowDownDown = True
            if event.key == pygame.K_w:
                wDown = True
            if event.key == pygame.K_s:
                sDown = True
           
                
        if event.type == pygame.KEYUP:
               if event.key == pygame.K_UP:
                   arrowUpDown = False
                   J1.VY = moveSpeed
               if event.key == pygame.K_DOWN:
                   arrowDownDown = False
                   J1.VY = moveSpeed
               if event.key == pygame.K_w:
                   wDown = False
                   J2.VY = moveSpeed
               if event.key == pygame.K_s:
                   sDown = False
                   J2.VY = moveSpeed
        if event.type == GAME_GLOBALS.QUIT:
            QuitGame()
                   
                   
             
                    
            
   
   
    
    
                
        
            
    
    # move(arrowUpDown, arrowDownDown, VY, posY, moveSpeed, wHeight)     
    J1.move(arrowUpDown, arrowDownDown, J1.VY, J1.posY, J1.moveSpeed, wHeight)  
    J2.move(wDown, sDown, J2.VY, J2.posY, J2.moveSpeed, wHeight)
    
    clock.tick(60)
    pygame.display.update()
    