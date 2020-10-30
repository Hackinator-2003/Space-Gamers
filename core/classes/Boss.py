from core.classes.enemy import Enemy
from random import randint

class Boss(Enemy):

    position=(10,15)

    def __init__(self,position=None):
        if self.position==None:position=randint(self.position[0],self.position[1])