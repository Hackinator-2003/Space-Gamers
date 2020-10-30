import logging
from core.classes.player import Player
from core.classes.enemy import Enemy
from core.classes.bullet import Bullet
from core.configparser import get_config

class Game():

    def __init__(self):
        logging.debug("init game...")
        logging.debug("loading config...")
        self.config = get_config()
        self.player = Player(self,[252,500])
        self.enemys = []
        self.pl_bullets = []
        self.en_bullets = []
        self.timer_new_enemys = 0



    def start(self):
        logging.info("game starting")
    

    def check_coll(self):
        def is_in(pos,pos2,rad):
            return pos2[0]-rad <= pos[0] <= pos2[0]+rad and pos2[1]-rad <= pos[1] <= pos2[1]+rad
        
        for i,bullet in enumerate(self.en_bullets):
            if is_in(bullet.pos,self.player.pos,self.player.hitbox_rad):
                logging.info("Player take en bullet: pv="+str(self.player.pv))
                del self.en_bullets[i]
                print(self.en_bullets)
                self.player.damage()
                break
        
        for i,enemy in enumerate(self.enemys):
            if is_in(enemy.pos,self.player.pos,self.player.hitbox_rad+enemy.hitbox_rad):
                logging.info("Player collide: pv="+str(self.player.pv))
                self.player.damage()
                del self.enemys[i]
                break
        
        for i,bullet in enumerate(self.pl_bullets):
            for enemy in self.enemys:
                if is_in(enemy.pos,bullet.pos,enemy.hitbox_rad):
                    logging.info("enemy take pl bullet: pv="+str(enemy.pv))
                    enemy.damage()
                    del self.pl_bullets[i]
                    break
        
        
        for i,enemy in enumerate(self.enemys):
            if enemy.pv <= 0: del self.enemys[i]

    def update(self,dt):
        
        self.timer_new_enemys += dt
        if self.timer_new_enemys >= 3.0:
            self.timer_new_enemys = 0
            self.enemys.append(Enemy(self,"normal",[250,0]))
        
        # call update on entitys
        self.player.update(dt)
        for enemy in self.enemys:enemy.update(dt)
        for bullet in self.pl_bullets:bullet.update(dt);bullet.move(dt)
        for bullet in self.en_bullets:bullet.update(dt);bullet.move(dt)

        self.check_coll()

        for i, bullet in enumerate(self.pl_bullets):
            if bullet.pos[1]<0 or bullet.pos[1]>700:
                del self.pl_bullets[i]
        
        for i, bullet in enumerate(self.en_bullets):
            if bullet.pos[1]<0 or bullet.pos[1]>700:
                del self.en_bullets[i]





