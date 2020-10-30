
class Bullet():

    degat=(1,3) #on pourrait augmenter les degats avec le temps ?

    def __init__(self,position,type_,speed=100):
        self.pos=position
        self.type_ = type_ # type of the projectile (mouvement différents etc)

    def move(self,dt): 
        if type_ == "up":self.pos[1] += speed*dt
        if type_ == "down":self.pos[1] -= speed*dt

    def update(self,dt):
        pass