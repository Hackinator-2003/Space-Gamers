
################################################ IMPORTATIONS DES MODULES NECESSAIRES ################################################

import pygame
from core.classes.enemy import Enemy
from core.classes.player import*
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
    def __init__(self,monde,size=(550,700)):
        self.screen = None
        self.monde = monde
        self.running = False
        self.size = size
        self.fond = pygame.image.load("core/rsc/img/space.jpg")
        pygame.init()
        self.dt = 0




#######################################################################################################################################################

################################################## DEFINITION DES METHODES DE LA CLASSE PYGAMEGUI #####################################################




    # Méthode du lancement de la boucle principale
    def start(self):
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(self.fond,(0,0))
        pygame.display.flip()
        pygame.display.set_caption("Space Invader")
        self.__mainLoop()

    # Méthode de la boucle principale
    def __mainLoop(self):
        self.running = True
        clock = pygame.time.Clock()
        exec_= 0

        #Tant que la boucle principale est en cours d'excution
        while self.running:

            # Calculation du delaTime utile pour les transitions
            self.dt = clock.tick()/1000
            exec_ += self.dt


            if player.Pv==3:
                point_de_vie =  pygame.image.load("core/rsc/img/3_coeurs.png")
                self.screen.blit(point_de_vie,(0,0))
                pygame.display.flip()

            elif player.Pv==2:
                point_de_vie =  pygame.image.load("core/rsc/img/2_coeurs.png")
                self.screen.blit(point_de_vie,(0,0))
                pygame.display.flip()

            elif player.Pv==1:
                point_de_vie =  pygame.image.load("core/rsc/img/1_coeur.png")
                self.screen.blit(point_de_vie,(0,0))
                pygame.display.flip()
            elif player.Pv==0:
                point_de_vie =  pygame.image.load("core/rsc/img/game-over.png")
                self.screen.blit(point_de_vie,(0,0))
                pygame.display.flip()




            pos = pygame.mouse.get_pos()

            for event in pygame.event.get():

                # Création de l'évènement quitter
                if event.type == pygame.QUIT:self.quit();break
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    # Si clic gauche, on execute la raction liée à clic gauche
                    if event.button == 1:self.left_click(pos)

                    # Si clic droit, on execute la raction liée à clic droit
                    if event.button == 3:self.right_click(pos) #


    # Réaction après l'event de clic droit
    def left_click(self,pos):
        pass

    # Réaction après l'event de clic droit
    def right_click(self,pos):
        pass

    # Fermeture de la fenêtre
    def quit(self):
        pygame.quit()
        self.running = False
        exit()

#######################################################################################################################################################

#######################################################################################################################################################
