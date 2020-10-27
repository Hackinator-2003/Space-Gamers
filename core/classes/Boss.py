from core.classes.enemy import Enemy
from random import randint
from core.GUI import*

class Boss(Enemy):


    fire_recovery = 5.5

    def __init__(self,game,position):
        self.pos=position
        self.game=game
        self.speed=100
        self.lasershot_sound = pygame.mixer.Sound('core/rsc/sounds/laser_shot.wav')
        self.fire_timer = 0

    def shoot(self,dt):
        if self.fire_timer >= self.fire_recovery:
            self.lasershot_sound.play()
            self.game.bullets.append(Bullet(self,[self.pos[0]+85,self.pos[1]+30],"down",100))
            self.fire_timer = 0.0


    def mov(self,dt):
        pass

    def update(self,dt):
        self.fire_timer += dt


