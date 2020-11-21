################################################ IMPORTATIONS DES MODULES NECESSAIRES ################################################
import logging
import pygame
from core.game import Game as jeu
from core.GUI import PygameGui as PyGameGUI
#######################################################################################################################################

pygame.init()

############################################### CREATION DE LA CLASSE PYGAMEGUI #######################################################
############################################### CREATION DE LA CLASSE PYGAMEGUI #######################################################

#Création de la classe PygameGui
class MainMenuPygameGui():
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
    def __init__(self,screen):
        self.screen = screen
        self.running = False
        self.fond = pygame.image.load("core/rsc/img/game-over.png")
        self.play_button=pygame.image.load("core/rsc/img/play-button.png")
        self.setting_button=pygame.image.load("core/rsc/img/setting-button.png")
        self.oldsi=pygame.image.load("core/rsc/img/old-si.png")
        self.play_button_over=pygame.image.load("core/rsc/img/play-button-over.png")
        self.setting_button_over=pygame.image.load("core/rsc/img/setting-button-over.png")
        self.valid_menu_sound = pygame.mixer.Sound('core/rsc/sounds/menu_valid_sound.wav')
        self.select=0
        pygame.mixer.stop()
        pygame.mixer.music.load("core/rsc/sounds/music.mp3")
        pygame.mixer.music.play(loops=-1)
        self.touches = {key:value for key,value in pygame.__dict__.items() if key[:2] == "K_" or key[:2] == "KM"}
        logging.debug("init Game Over")
        self.dt = 0




#######################################################################################################################################################

################################################## DEFINITION DES METHODES DE LA CLASSE PYGAMEGUI #####################################################




    # Méthode du lancement de la boucle principale
    def start(self):
        self.__mainLoop()

    # Méthode de la boucle principale
    def __mainLoop(self):
        logging.debug("GameOver Mainloop starting")
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

            play_rect = self.play_button.get_rect(center=(self.size[0]/2,0))
            play_coo=(play_rect[0],logo_rect[3])
            play_size=(self.play_button.get_width(),self.play_button.get_height())
            self.screen.blit(self.play_button,play_coo)

            setting_rect = self.setting_button.get_rect(center=(self.size[0]/2,0))
            setting_coo=(setting_rect[0],logo_rect[3]+20+play_rect[3])
            setting_size=(self.setting_button.get_width(),self.setting_button.get_height())
            self.screen.blit(self.setting_button,setting_coo)

            oldsi_rect = self.oldsi.get_rect(center=(self.size[0]/2,0))
            oldsi_coo=(oldsi_rect[0],logo_rect[3]+20+play_rect[3]+20+setting_rect[3])
            oldsi_size=((self.oldsi.get_width(),self.oldsi.get_height()))
            self.screen.blit(self.oldsi,oldsi_coo)
            # flip
            pygame.display.flip()

            # affichage du fond

            for event in pygame.event.get():
                if event.type == pygame.QUIT:self.quit();break
                if event.type == pygame.MOUSEMOTION:
                     mouse_x, mouse_y = pygame.mouse.get_pos()
                     if(play_coo[0] < mouse_x < play_coo[0] + play_size[0]) and (play_coo[1] < mouse_y < play_coo[1] + play_size[1]):
                        select=0
                     else:

                     if(setting_coo[0] < mouse_x < setting_coo[0] + setting_size[0]) and (setting_coo[1] < mouse_y < setting_coo[1] + setting_size[1]):
                        select=1

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if select==1:
                        # Set the x, y postions of the mouse click
                        if ((play_coo[0] < mouse_x < play_coo[0] + play_size[0]) and (play_coo[1] < mouse_y < play_coo[1] + play_size[1])):
                            self.screen.blit(self.play_button_over,play_coo)
                            pygame.display.flip()
                            self.valid_menu_sound.play()
                            pygame.time.wait(20)
                            pygame.mouse.set_cursor(*pygame.cursors.arrow)
                            game = jeu()
                            Gui = PyGameGUI(game)
                            Gui.start()




    # Fermeture de la fenêtre
    def quit(self):
        pygame.quit()
        self.running = False
        exit()

#######################################################################################################################################################

#######################################################################################################################################################
