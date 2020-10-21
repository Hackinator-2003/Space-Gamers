import pygame
from core.GUI import*

class Player():

    max_pv = 3
    nom="player"
    vaisceau = pygame.image.load("core/rsc/img/best-ship.png")

    def __init__(self,position,pv=3):
        self.pos=position
        self.pv=pv






