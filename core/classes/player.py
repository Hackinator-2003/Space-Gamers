import pygame
from core.GUI import*
import logging

class Player():

    max_pv = 3
    vaisceau = pygame.image.load("core/rsc/img/spaceship.png")

    def __init__(self,position,pv=3):
        self.pos=position
        self.pv=pv
        logging.debug("init player at "+str(position)+", pv="+str(pv))



    # Réaction après l'event de clic droit
    def left(self,dt):
        logging.debug("Left click event called")
        self.pos[0]-=PygameGui.speed*dt
        if self.pos[0]<0: self.pos[0]=0

    # Réaction après l'event de clic droit
    def right(self,dt):
        logging.debug("Right click event called")
        self.pos[0]+=PygameGui.speed*dt
        if self.pos[0]>550-60: self.pos[0]=550-60

    # Réaction après l'event de clic droit
    def up(self,dt):
        logging.debug("Left click event called")
        self.pos[1]-=PygameGui.speed*dt
        if self.pos[1]<0: self.pos[1]=0


    # Réaction après l'event de clic droit
    def down(self,dt):
        logging.debug("Right click event called")
        self.pos[1]+=PygameGui.speed*dt
        if self.pos[1]>700-60: self.pos[1]=700-60

