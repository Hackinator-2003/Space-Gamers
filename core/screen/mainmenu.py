################################################ IMPORTATIONS DES MODULES NECESSAIRES ################################################
import logging
import pygame
from core import GUI as PyGameGUI
#######################################################################################################################################

############################################### CREATION DE LA CLASSE PYGAMEGUI #######################################################
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
    def __init__(self,size=(550,700)):
        self.screen = None
        self.running = False
        self.size = size
        self.fond = pygame.image.load("core/rsc/img/background.jpg")
        self.logo=pygame.image.load("core/rsc/img/logo.png")
        self.play_button=pygame.image.load("core/rsc/img/play-button.png")
        self.touches = {key:value for key,value in pygame.__dict__.items() if key[:2] == "K_" or key[:2] == "KM"}
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
        logging.debug("Calling ggamemenu.start()")
        self.__mainLoop()

    # Méthode de la boucle principale
    def __mainLoop(self):
        logging.debug("GUI mainloop called !")
        self.running = True
        clock = pygame.time.Clock()
        exec_= 0
        time = 0

        #Tant que la boucle principale est en cours d'excution
        while self.running:

            # Calculation du delaTime utile pour les transitions
            self.dt = clock.tick()/1000
            exec_ += self.dt

            # affichage du fond
            self.screen.blit(self.fond,(0,0))
            logo_rect = self.logo.get_rect(center=(self.size[0]/2,0))
            self.screen.blit(self.logo,(logo_rect[0],0))
            # flip
            pygame.display.flip()

            # affichage du fond


            pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:self.quit();break


    # Fermeture de la fenêtre
    def quit(self):
        pygame.quit()
        self.running = False
        exit()

#######################################################################################################################################################

#######################################################################################################################################################
