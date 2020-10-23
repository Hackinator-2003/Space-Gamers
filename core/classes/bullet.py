from core.GUI import*
import pygame

class Bullet():

    degat=(1,3) #on pourrait augmenter les degats avec le temps ?


    def __init__(self,position):
        self.pos=position


    def tire(self,dt):
        self.pos[1]-=200*dt
        if self.pos[1]<0:
            print(self,"hors")