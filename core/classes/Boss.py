﻿from core.classes.enemy import Enemy
from random import randint
from core.GUI import*

class Boss(Enemy):


    fire_recovery = 2.0

    def __init__(self,game,position):
        self.pos=position
        self.game=game
        self.speed=100
        self.lasershot_sound = pygame.mixer.Sound('core/rsc/sounds/laser_shot.wav')
        self.fire_timer = 0

    def shoot(self,dt):
        if self.fire_timer >= self.fire_recovery:
            self.lasershot_sound.play()
            self.game.bullets.append(Bullet(self,[self.pos[0]+85,self.pos[1]+100],"down",100))
            self.fire_timer = 0.0


    def move(self,dt,speed):
        rand=randint(0,1)
        if rand==0:
            self.pos[0]-=speed*dt
        else:
            self.pos[0]+=speed*dt

        if self.pos[0]>550-212: self.pos[0]=550-212
        if self.pos[0]<0: self.pos[0]=0

    def update(self,dt):
        self.fire_timer += dt


