

class Player():

    max_Pv = 3
    nom="player"

    def __init__(self,position,pv=3):
        self.pos=position
        self.Pv=pv


player=Player((100,300),3)