﻿
class Bullet():

    degat=(1,3) #on pourrait augmenter les degats avec le temps ?

    def __init__(self,position,type_,speed=300,direction=None):
        self.pos=position
        self.type_ = type_ # type of the projectile (mouvement différents etc)
        self.speed = speed
        self.direction = direction

    def move(self,dt): 
        if self.type_ == "up":self.pos[1] -= self.speed*dt
        if self.type_ == "down":self.pos[1] += self.speed*dt
        if self.type_ == "downleft":
            self.pos[1] += self.speed*dt*0.8
            self.pos[0] += self.speed*dt*0.2 
        if self.type_ == "downright":
            self.pos[1] += self.speed*dt*0.8
            self.pos[0] -= self.speed*dt*0.2 
        if self.type_ == "direction":
            self.pos[1] += self.speed*dt*self.direction[0]
            self.pos[0] += self.speed*dt*self.direction[1]

    def update(self,dt):
        pass