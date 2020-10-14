from random import randint

class Enemy():

    nom = "Enemy"
    start_pv=(1,10)


    def __init__(self,position,Pv=None):
        self.pos=position
        self.Pv==None: self.Pv=randint(self.start_pv[0],self.start_pv[1])