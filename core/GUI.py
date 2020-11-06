
################################################ IMPORTATIONS DES MODULES NECESSAIRES ################################################
import logging
import pygame
from core.classes.enemy import Enemy
from core.classes.bullet import Bullet
from core.classes.Boss import Boss
import sys
#######################################################################################################################################

############################################### CREATION DE LA CLASSE PYGAMEGUI #######################################################

#Création de la classe PygameGui
class PygameGui():
    """
    La classe PygameGui est la classe qui s'occupe de la gestion de l'interface graphique.

    Attributs communs à toutes les instances :
        screen: l'affichage de la fenêtre
        running: lancement actif de pygame
        size: taille de la fenêtre

    Methodes :

    """


################################# CREATION DE LA FONCTION D'INITIALISATION DE LA CLASSE PYGAMEGUI AVEC SES ATTRIBUTS ##################################
    speed = 200
    speed_bullet = 500

    #Initialisation de la classe PygameGui et de ses attributs
    def __init__(self,game,size=(550,700)):
        self.screen = None
        self.game = game
        self.gui_config = self.game.config["GUI"]
        self.input_config = self.game.config["INPUT"]
        self.running = False
        self.size = size
        self.fond = pygame.image.load("core/rsc/img/background.jpg")
        self.touches = {key:value for key,value in pygame.__dict__.items() if key[:2] == "K_" or key[:2] == "KM"}
        self.touches["K_MOUSE"] = len(self.touches.keys())
        logging.debug("init Pygame...")
        pygame.init()
        self.dt = 0




#######################################################################################################################################################

################################################## DEFINITION DES METHODES DE LA CLASSE PYGAMEGUI #####################################################




    # Méthode du lancement de la boucle principale
    def start(self,screen):
        logging.info("Starting GUI mainloop")
        self.screen = screen
        self.ismousedown = False
        pygame.display.flip()
        logging.debug("Calling game.start()")
        self.__mainLoop()

    # Méthode de la boucle principale
    def __mainLoop(self):
        logging.debug("GUI mainloop called !")
        self.running = True
        clock = pygame.time.Clock()

        #Tant que la boucle principale est en cours d'excution
        while self.running:

            # Calculation du delaTime utile pour les transitions
            self.dt = clock.tick()/1000

            # appel de self.manageEvents()
            self.manageEvents()

            # appel de game.update()
            self.game.update(self.dt)

            # appel de self.draw()
            self.draw()







    def draw(self):
        # affichage du fond
        self.screen.blit(self.fond,(0,0))

        # affichage du joueur
        self.screen.blit(self.game.player.vaisceau,(self.game.player.pos[0]-self.game.player.vaisceau.get_rect().width//2,self.game.player.pos[1]-self.game.player.vaisceau.get_rect().height//2))
        fire = pygame.image.load("core/rsc/img/tire.png")

        if self.gui_config["ShowHitbox"] == "T":
            rad = self.game.player.hitbox_rad
            pygame.draw.rect(self.screen, (0,255,0), (self.game.player.pos[0]-rad,self.game.player.pos[1]-rad,rad*2,rad*2),1)

        # affichange des missiles du joueur
        for bullet in self.game.pl_bullets:
            if bullet.type_ == "up":self.screen.blit(fire,(bullet.pos[0]-fire.get_rect().width//2,bullet.pos[1]-fire.get_rect().height//2))
            else: self.screen.blit(pygame.transform.flip(fire,False,True),(bullet.pos[0]-fire.get_rect().width//2,bullet.pos[1]-fire.get_rect().height//2))

            if self.gui_config["ShowHitbox"] == "T":
                pygame.draw.circle(self.screen, (0,255,0), (int(bullet.pos[0]),int(bullet.pos[1])),1)

        # affichange des missiles des ennemies
        for bullet in self.game.en_bullets:
            if bullet.type_ == "up":self.screen.blit(fire,(bullet.pos[0]-fire.get_rect().width//2,bullet.pos[1]-fire.get_rect().height//2))
            else: self.screen.blit(pygame.transform.flip(fire,False,True),(bullet.pos[0]-fire.get_rect().width//2,bullet.pos[1]-fire.get_rect().height//2))

            if self.gui_config["ShowHitbox"] == "T":
                pygame.draw.circle(self.screen, (0,255,0), (int(bullet.pos[0]),int(bullet.pos[1])),1)


        # affichange des enemies
        for enemy in self.game.enemys:
            if self.gui_config["ShowHitbox"] == "T":
                rad = enemy.hitbox_rad
                pygame.draw.rect(self.screen, (0,255,0), (enemy.pos[0]-rad,enemy.pos[1]-rad,rad*2,rad*2),1)
            if enemy.type_ == "normal": look = pygame.image.load("core/rsc/img/placeholder.png")
            elif enemy.type_ == "boss": look = pygame.image.load("core/rsc/img/red-enemy.png")
            else: look = pygame.image.load("core/rsc/img/placeholder.png")
            self.screen.blit(look,(enemy.pos[0]-look.get_rect().width//2,enemy.pos[1]-look.get_rect().height//2))


        # affichage du score
        police = pygame.font.Font(None,55)
        texte = police.render(str(round(self.game.player.score)),True,pygame.Color("#FFFFFF"))
        texte_rect = texte.get_rect(center=(self.size[0]/2, 0))
        self.screen.blit(texte,(texte_rect[0],10))

        # affichage de la vie / écran de game-over (on verra si on fais vraiment comme ça)
        if self.game.player.pv>=3: point_de_vie = pygame.image.load("core/rsc/img/3_coeurs.png")
        elif self.game.player.pv==2: point_de_vie = pygame.image.load("core/rsc/img/2_coeurs.png")
        elif self.game.player.pv==1: point_de_vie = pygame.image.load("core/rsc/img/1_coeur.png")
        elif self.game.player.pv<=0: point_de_vie = pygame.image.load("core/rsc/img/game-over.png")
        self.screen.blit(point_de_vie,(0,0))

        # flip
        pygame.display.flip()

    def manageEvents(self):
        # mpos = pygame.mouse.get_pos()
        self.ismousedown = pygame.mouse.get_pressed() == 1

        pressed = list(pygame.key.get_pressed())
        pressed.append(self.ismousedown)
        if pressed[self.touches[self.input_config["left"]]]: self.game.player.left(self.dt)
        if pressed[self.touches[self.input_config["right"]]]: self.game.player.right(self.dt)
        if pressed[self.touches[self.input_config["up"]]]: self.game.player.up(self.dt)
        if pressed[self.touches[self.input_config["down"]]]: self.game.player.down(self.dt)

        if pressed[self.touches[self.input_config["fire"]]]:
            self.game.player.shoot(self.dt)

    # Fermeture de la fenêtre
    def quit(self):
        logging.warn("Gui.quit() called !")
        pygame.quit()
        self.running = False
        sys.exit(0)

#######################################################################################################################################################

#######################################################################################################################################################
