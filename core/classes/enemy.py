from random import randint
import logging
class Enemy():

    nom = "Enemy"
    hitbox_rad = 20


    def __init__(self,game,type_="normal",position=[250,0],pv=3):
        self.pos=position
        self.game = game
        self.type_=type_
        self.pv = pv
        logging.debug("init enemys at "+str(position)+", pv="+str(self.pv))
    
    def update(self,dt):
        if self.type_ == "normal":
            self.pos[1]+=100 *dt
        if self.pos[1]>700-60: self.pos[1]=700-60
    
    def damage(self):
        self.pv -= 1