
class Bullet():

    degat=(1,3) #on pourrait augmenter les degats avec le temps ?

    def __init__(self,handler,position,type_,speed=100):
        self.pos=position
        self.handler = handler # à qui appratiens le rpojectile (au joueur ou aux ennemys)
        self.type_ = type_ # type of the projectile (mouvement différents etc)
        self.speed = speed

    def move(self,dt):
        if self.type_ == "up":self.pos[1] -= self.speed*dt
        if self.type_ == "down":self.pos[1] += self.speed*dt

    def update(self,dt):
        pass