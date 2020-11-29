import logging
from sys import platform
from core.classes.player import Player
from core.classes.enemy import Enemy
from core.classes.bullet import Bullet
from core.configparser import get_config

from random import randint

class Game():

    def __init__(self,conf):
        logging.debug("init game...")
        logging.debug("loading config...")
        self.config = conf
        self.player = Player(self,[252,500])
        self.enemys = []
        self.pl_bullets = []
        self.en_bullets = []
        self.general_timer = 0
        self.timers = {
            # format : timer, temps_appartition, temps_appartition_min, temps_dimunution
            "en_basic":[2,15,10,0.8], # new enemy
            "en_move":[7,15,6,0.8], # new enemy
            "boss":[0,30,20,0.8]
        }



    def start(self):
        logging.info("game starting")


    def check_coll(self):
        def is_in(pos,pos2,rad):
            return pos2[0]-rad <= pos[0] <= pos2[0]+rad and pos2[1]-rad <= pos[1] <= pos2[1]+rad

        for i,bullet in enumerate(self.en_bullets):
            if is_in(bullet.pos,self.player.pos,self.player.hitbox_rad):
                logging.info("Player take en bullet: pv="+str(self.player.pv))
                del self.en_bullets[i]
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

        if self.player.pv <= 0: return

        self.general_timer += dt
        for x in self.timers.keys():
            self.timers[x][0] += dt
        
        def res(name):
            self.timers[name][0] = 0
            self.timers[name][1] = (self.timers[name][1]-self.timers[name][2])*self.timers[name][3]+self.timers[name][2]


        if self.timers["en_basic"][0] >= self.timers["en_basic"][1]:
            res("en_basic")
            self.enemys.append(Enemy(self,"basic",[randint(20,530),0]))
        
        if self.timers["en_move"][0] >= self.timers["en_move"][1]:
            res("en_move")
            self.enemys.append(Enemy(self,"move",[randint(20,530),0]))


        if self.timers["boss"][0] >= self.timers["boss"][1]:
            res("boss")
            self.enemys.append(Enemy(self,"boss",[250,0],15,1,40))



        # call update on entitys
        self.player.update(dt)
        for enemy in self.enemys: enemy.update(dt)
        for bullet in self.pl_bullets:bullet.update(dt);bullet.move(dt)
        for bullet in self.en_bullets:bullet.update(dt);bullet.move(dt)

        self.check_coll()

        for i, bullet in enumerate(self.pl_bullets):
            if bullet.pos[1]<0 or bullet.pos[1]>700:
                del self.pl_bullets[i]

        for i, bullet in enumerate(self.en_bullets):
            if bullet.pos[1]<0 or bullet.pos[1]>700:
                del self.en_bullets[i]





