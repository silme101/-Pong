# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 09:59:18 2021

@author: Silvia
"""

import pygame


#.init lo que hace es poner en marcha los modulos, si no lo tuviera, las teclas no servirian de nada que se pulsaran
#y no iniciaria, daria error "video system not initialized





class Player1:
    
    def __init__(self, wWidth, wHeight):
    
        self.sizeLong = 100
        self.sizeWide = 20
        
        self.posX = 0
        self.posY = wHeight/2 - self.sizeLong/2
        self.moveSpeed = 1.0
        self.maxSpeed = 10.0
        


    


        self.VY = 1.0

    
    

    
# Importante pasar el self como argumento cuando son argumentos relacionados con un objeto, 
# ya que este tambien lo cuenta

    def move(self, arrowUpDown, arrowDownDown, VY, posY, moveSpeed, wHeight):
        if arrowUpDown:
		#If we're already moving upwards, reset the moving speed and invert the direction
            if VY > 0.0:
                VY = moveSpeed
                VY = -VY
         #Make sure our square doesn't leave our window from the upper part
            if posY > 0:
                 posY += VY
                 
        if arrowDownDown:
            #If we are already moving downwards, reestart speed and change direction
            if VY < 0.0:
                VY = moveSpeed
                VY = -VY
            if posY < wHeight:
                posY += VY
                
                
            
            
                 
                
                

                
       
            