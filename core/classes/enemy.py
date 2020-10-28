﻿from random import randint
import logging
import pygame

class Enemy():

    nom = "Enemy"
    start_pv=(1,10)
    fire_recovery = 2.0


    def __init__(self,game,position,pv=None):
        self.pos=position
        self.game = game
        if pv==None: self.pv=randint(self.start_pv[0],self.start_pv[1])
        else: self.pv = pv
        logging.debug("init enemys at "+str(position)+", pv="+str(self.pv))
        self.lasershot_sound = pygame.mixer.Sound('core/rsc/sounds/laser_shot.wav')
        self.fire_timer = 0

    def update(self,dt):
        self.fire_timer += dt




    def shoot(self,dt):
        if self.fire_timer >= self.fire_recovery:
            self.lasershot_sound.play()
            self.game.bullets.append(Bullet(self,[self.pos[0]+12,self.pos[1]-30],"down",100))
            self.fire_timer = 0.0


    def move(self,dt,speed):
        rand=randint(0,1)
        if rand==0:
            self.pos[0]-=speed*dt
        else:
            self.pos[0]+=speed*dt

        if self.pos[0]>550-212: self.pos[0]=550-212
        if self.pos[0]<0: self.pos[0]=0


    def degat(self,liste):
        self.pv -= 1

        if self.pv <= 0:
            for i,x in enumerate(liste):
                if x == self:
                    del liste[i]
        else: pass

