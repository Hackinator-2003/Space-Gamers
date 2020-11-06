from core.classes.enemy import Enemy
from random import randint

class Boss(Enemy):



    def __init__(self,game,type_="boss",position=[250,0],pv=10,fire_speed=1):
        self.pos=position
        self.game = game
        self.type_=type_
        self.pv = pv
        self.fire_timer = 0
        self.fire_speed = fire_speed
