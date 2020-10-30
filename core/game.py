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
        self.enemys = [Enemy(self,[30,30]),Enemy(self,[60,30]),Enemy(self,[90,30])]
        self.bullets = []
        self.timer_new_enemys = 0



    def start(self):
        logging.info("game starting")
    

    def check_coll(self):
        def is_in(pos,pos2,rad):
            return pos2[0]-rad <= pos[0] <= pos2[0]+rad and pos2[1]-rad <= pos[1] <= pos2[1]+rad
        
        for i,bullet in enumerate(self.bullets):
            if is_in(bullet.pos,self.player.pos,self.player.hitbox_rad):
                print("PLAYER IN BULLET")
                if len(self.bullets) >= i: del self.bullets[i]
                self.player.damage()
        
        for i,enemy in enumerate(self.enemys):
            if is_in(enemy.pos,self.player.pos,self.player.hitbox_rad+enemy.hitbox_rad):
                print("PLAYER IN ENEMY")
                self.player.damage()
                if len(self.enemys) >= i: del self.enemys[i]
        
        for i,bullet in enumerate(self.bullets):
            for enemy in self.enemys:
                if is_in(enemy.pos,bullet.pos,enemy.hitbox_rad):
                    print("BULLET IN ENEMY")
                    enemy.damage()
                    if len(self.bullets) >= i: del self.bullets[i]
        
        
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
        for bullet in self.bullets:bullet.update(dt)

        self.check_coll()

        if self.bullets != None:
            for bullet in self.bullets:
                bullet.move(dt)

                if bullet.pos[1]<0:
                    for i,x in enumerate(self.bullets):
                        if x == bullet:
                            del self.bullets[i]





