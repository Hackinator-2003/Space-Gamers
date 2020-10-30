from random import randint
import logging
from core.classes.bullet import Bullet
class Enemy():

    nom = "Enemy"
    hitbox_rad = 20


    def __init__(self,game,type_="normal",position=[250,0],pv=3,fire_speed=1):
        self.pos=position
        self.game = game
        self.type_=type_
        self.pv = pv
        self.fire_timer = 0
        self.fire_speed = fire_speed
        logging.debug("init enemys at "+str(position)+", pv="+str(self.pv))
    
    def update(self,dt):
        self.fire_timer += dt
        if self.type_ == "normal":
            self.pos[1]+=100*dt
        if self.fire_timer >= self.fire_speed:
            self.fire_timer = 0
            self.game.en_bullets.append(Bullet([self.pos[0],self.pos[1]+self.hitbox_rad+1],"down",300))

    
    def damage(self):
        self.pv -= 1