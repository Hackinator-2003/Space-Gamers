from random import randint
import logging
class Enemy():

    nom = "Enemy"
    start_pv=(1,10)


    def __init__(self,position,pv=None):
        self.pos=position
        if pv==None: self.pv=randint(self.start_pv[0],self.start_pv[1])
        else: self.pv = pv
        logging.debug("init enemys at"+str(position)+", pv="+str(self.pv))