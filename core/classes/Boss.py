from core.classes.enemy import Enemy
from random import randint
from core.GUI import*

class Boss(Enemy):



    nom = "boss"

    def __init__(self,game,position,pv=None):
        self.pos=position
        self.game=game
        if pv==None: self.pv=randint(self.start_pv[0],self.start_pv[1])
        else: self.pv = pv
        self.speed=100
        self.lasershot_sound = pygame.mixer.Sound('core/rsc/sounds/laser_shot.wav')
        self.fire_timer = 0


    def shoot(self,dt):
        if self.fire_timer >= self.fire_recovery:
            self.lasershot_sound.play()
            self.game.bullets.append(Bullet(self,[self.pos[0]+85,self.pos[1]+100],"down",100))
            self.fire_timer = 0.0



    def dead(self):
        if self.pv <= 0:
            for i,x in enumerate(self.game.boss):
                if x == self:
                    del self.game.boss[i]
        else: pass


    def update(self,dt):
        self.fire_timer += dt
        self.dead()




