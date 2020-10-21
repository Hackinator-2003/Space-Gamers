import pygame
from core.GUI import*
import logging

class Player():

    max_pv = 3
    nom="player"
    vaisceau = pygame.image.load("core/rsc/img/best-ship.png")

    def __init__(self,position,pv=3):
        self.pos=position
        self.pv=pv
        logging.debug("init player at"+str(position)+", pv="+str(pv))






