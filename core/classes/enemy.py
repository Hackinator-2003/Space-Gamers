from random import randint
import logging
from core.classes.bullet import Bullet
import math
class Enemy():

    nom = "Enemy"

    def __init__(self,game,type_="normal",position=[250,0],pv=3,fire_speed=1,hitbox_rad=20):
        self.pos=position
        self.game = game
        self.type_=type_
        self.pv = pv
        self.hitbox_rad = hitbox_rad
        self.fire_timer = 0
        self.fire_speed = fire_speed
        logging.debug("init enemys at "+str(position)+", pv="+str(self.pv))

    def update(self,dt):
        
        self.fire_timer += dt
        if self.type_ == "basic":
            self.pos[1]+=100*dt
            if self.fire_timer >= self.fire_speed and self.game.player.pos[1] > self.pos[1]:
                self.fire_timer = 0
                distance = math.sqrt((self.game.player.pos[0]-self.pos[0])**2+(self.game.player.pos[1]-self.pos[1])**2)
                self.game.en_bullets.append(Bullet([self.pos[0],self.pos[1]+self.hitbox_rad+1],"direction",300,[
                    -(self.pos[1]-self.game.player.pos[1])/distance,
                    -(self.pos[0]-self.game.player.pos[0])/distance]))
        if self.type_ == "move":
            self.pos[1]+=100*dt
            if self.game.player.pos[0]-5 < self.pos[0]: self.pos[0] -= dt*100
            elif self.game.player.pos[0]+5 > self.pos[0]: self.pos[0] += dt*100
            if self.fire_timer >= self.fire_speed:
                self.fire_timer = 0
                self.game.en_bullets.append(Bullet([self.pos[0],self.pos[1]+self.hitbox_rad+1],"down",300))
        elif self.type_ == "boss":
            if self.pos[1] <= 100:self.pos[1]+=100*dt
            else:self.pos[1] = 100
            if self.fire_timer >= self.fire_speed:
                self.fire_timer = 0
                self.game.en_bullets.append(Bullet([self.pos[0],self.pos[1]+self.hitbox_rad+1],"down",300))
                self.game.en_bullets.append(Bullet([self.pos[0],self.pos[1]+self.hitbox_rad+1],"downleft",300))
                self.game.en_bullets.append(Bullet([self.pos[0],self.pos[1]+self.hitbox_rad+1],"downright",300))

    def __del__(self):
        if self.type_ == "normal":self.game.player.score+=100

    def damage(self):
        self.pv -= 1
        if self.type_ == "normal":self.game.player.score+=10