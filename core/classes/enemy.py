from random import randint
import logging
class Enemy():

    nom = "Enemy"
    start_pv=(1,10)


    def __init__(self,game,position,pv=None):
        self.pos=position
        self.game = game
        if pv==None: self.pv=randint(self.start_pv[0],self.start_pv[1])
        else: self.pv = pv
        logging.debug("init enemys at "+str(position)+", pv="+str(self.pv))

    def update(self,dt):pass



    def shoot(self,dt):
        if self.fire_timer >= self.fire_recovery:
            self.lasershot_sound.play()
            self.game.bullets.append(Bullet(self,[self.game.player.pos[0]+12,self.game.player.pos[1]-30],"down",100))
            self.fire_timer = 0.0
