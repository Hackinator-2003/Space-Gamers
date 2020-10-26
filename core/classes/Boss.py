from core.classes.enemy import Enemy
from random import randint
from core.GUI import*

class Boss(Enemy):



    def __init__(self,position):
        self.pos=position
        self.speed=100

    def shoot(self,dt):
        if self.fire_timer >= self.fire_recovery:
            self.lasershot_sound.play()
            self.game.bullets.append(Bullet(self,[self.game.player.pos[0]+12,self.game.player.pos[1]-30],"down",100))
            self.fire_timer = 0.0


    def mov(self,dt):
        pass


