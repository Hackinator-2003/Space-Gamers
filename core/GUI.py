
################################################ IMPORTATIONS DES MODULES NECESSAIRES ################################################
import logging
import pygame
from core.classes.enemy import Enemy
from core.classes.Boss import Boss

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

    #Initialisation de la classe PygameGui et de ses attributs
    def __init__(self,game,size=(550,700)):
        self.screen = None
        self.game = game
        self.conf = self.game.config
        self.running = False
        self.size = size
        self.fond = pygame.image.load("core/rsc/img/background.jpg")
        logging.debug("init Pygame...")
        pygame.init()
        self.dt = 0




#######################################################################################################################################################

################################################## DEFINITION DES METHODES DE LA CLASSE PYGAMEGUI #####################################################




    # Méthode du lancement de la boucle principale
    def start(self):
        logging.info("Starting GUI mainloop")
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Space Invader")
        pygame.display.flip()
        logging.debug("Calling game.start()")
        self.game.start()
        self.__mainLoop()

    # Méthode de la boucle principale
    def __mainLoop(self):
        logging.debug("GUI mainloop called !")
        self.running = True
        clock = pygame.time.Clock()
        exec_= 0

        #Tant que la boucle principale est en cours d'excution
        while self.running:

            # affichage du fond
            self.screen.blit(self.fond,(0,0))

            # affichage du joueur
            self.screen.blit(self.game.player.vaisceau,(self.game.player.pos[0],self.game.player.pos[1]))

            # affichage de la vie / écran de game-over
            if self.game.player.pv==3: point_de_vie =  pygame.image.load("core/rsc/img/3_coeurs.png")
            elif self.game.player.pv==2: point_de_vie =  pygame.image.load("core/rsc/img/2_coeurs.png")
            elif self.game.player.pv==1: point_de_vie =  pygame.image.load("core/rsc/img/1_coeur.png")
            elif self.game.player.pv==0: point_de_vie =  pygame.image.load("core/rsc/img/game-over.png")

            self.screen.blit(point_de_vie,(0,0))
            # flip
            pygame.display.flip()

            # Calculation du delaTime utile pour les transitions
            self.dt = clock.tick()/1000
            exec_ += self.dt

            pos = pygame.mouse.get_pos()

            for event in pygame.event.get():

                # Création de l'évènement quitter
                if event.type == pygame.QUIT:self.quit();break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Si clic gauche, on execute la raction liée à clic gauche
                    if event.button == 1:self.left(pos)
                    # Si clic droit, on execute la raction liée à clic droit
                    if event.button == 3:self.right(pos) #


    # Réaction après l'event de clic droit
    def left(self,pos):
        logging.debug("Left click event called")
        self.game.player.pos[0]-=100*self.dt

    # Réaction après l'event de clic droit
    def right(self,pos):
        logging.debug("Right click event called")
        self.game.player.pos[0]+=100*self.dt

    # Fermeture de la fenêtre
    def quit(self):
        logging.warn("Gui.quit() called !")
        pygame.quit()
        self.running = False
        exit()

#######################################################################################################################################################

#######################################################################################################################################################
