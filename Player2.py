# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:07:58 2021

Player2

@author: Silvia
"""

import pygame


class Player2:
    
    
    
     def __init__(self, wWidth, wHeight):
    
        self.sizeLong = 100
        self.sizeWide = 20
        
        self.posX = wWidth - self.sizeWide
        self.posY = wHeight/2 - self.sizeLong/2
        self.moveSpeed = 1.0
        self.maxSpeed = 10.0
        

        self.VY = 1.0
        


    
       
                        
                        
                    
     def move(self, wDown, sDown, VY, posY, moveSpeed, wHeight):
       if wDown:
           #'re already moving upwards, reset the moving speed and invert the direction
           if VY > 0.0:
               VY = moveSpeed
               VY = -VY
         #Make sure our square doesn't leave our window from the upper part
           if posY > 0:
               posY += VY
                 
       if sDown:
            #If we are already moving downwards, reestart speed and change direction
            if VY < 0.0:
                VY = moveSpeed
                VY = -VY
            if posY < wHeight:
                posY += VY            
                    
            