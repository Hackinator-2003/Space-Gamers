import pygame
from core.GUI import*
import logging

class Player():

    max_pv = 3
    nom="player"
    vaisceau = pygame.image.load("core/rsc/img/spaceship.png")

    def __init__(self,position,pv=3):
        self.pos=position
        self.pv=pv
        logging.debug("init player at "+str(position)+", pv="+str(pv))



    # Réaction après l'event de clic droit
    def left(self,pos,dt):
        logging.debug("Left click event called")
        self.pos[0]-=100*dt

    # Réaction après l'event de clic droit
    def right(self,pos,dt):
        logging.debug("Right click event called")
        self.pos[0]+=100*dt


