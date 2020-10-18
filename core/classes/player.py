import pygame
from core.GUI import*

class Player():

    max_Pv = 3
    nom="player"
    vaisceau = pygame.image.load("core/rsc/img/best-ship.png")
    pos_init = (225,500)

    def __init__(self,position,pv=3):

        self.pos=position
        self.Pv=pv






