import pygame
from core.GUI import*
import logging

class Player():

    max_pv = 3
    speed = 300
    fire_recovery = 0.1
    nom="player"
    vaisceau = pygame.image.load("core/rsc/img/spaceship.png")

    def __init__(self,game,position,pv=3):
        self.pos=position
        self.pv=pv
        self.game = game
        self.lasershot_sound = pygame.mixer.Sound('core/rsc/sounds/laser_shot.wav')
        logging.debug("init player at "+str(position)+", pv="+str(pv))
        self.fire_timer = 0 

    def update(self,dt):
        self.fire_timer += dt

    def shoot(self,dt):
        if self.fire_timer >= self.fire_recovery:
            self.lasershot_sound.play()
            self.game.bullets.append(Bullet([self.game.player.pos[0]+12,self.game.player.pos[1]-30],"up",100))
            self.fire_timer = 0.0

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

