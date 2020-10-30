################################################ IMPORTATIONS DES MODULES NECESSAIRES ################################################
import logging
import pygame
from core.game import Game as jeu
from core.GUI import PygameGui as PyGameGUI
import sys
from core.configparser import get_config
#######################################################################################################################################

# pygame.init() pas besoin car initialisé dans menu.start()

class Section(): # Type de sauvegarde de donné pour structuré le menu

    def __init__(self,text,action,description="",color=(100,100,100),hold_color=(200,200,200)):
        self.text = text
        self.action = action
        self.color = color
        self.description = description
        self.hold_color = hold_color
        self.parent = None
        


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
    def __init__(self,size=(550,700)):
        logging.debug("initialisation of Pygame...")
        pygame.init()
        self.screen = None
        self.running = False
        self.size = size
        self.config = get_config()
        self.fond = pygame.image.load("core/rsc/img/background.jpg")
        self.logo=pygame.image.load("core/rsc/img/logo.png")
        self.input_config = self.config["INPUT"]
        self.valid_menu_sound = pygame.mixer.Sound('core/rsc/sounds/menu_valid_sound.wav')
        pygame.mixer.music.load("core/rsc/sounds/music.mp3")
        pygame.mixer.music.play(loops=-1)
        self.touches = {key:value for key,value in pygame.__dict__.items() if key[:2] == "K_" or key[:2] == "KM"}
        logging.debug("Creating sections")

        info_credits = Section("Crédits","texte","""Ce jeu à été réaliser par Cyprien
Bourotte, Aurélien XXXX et Marc XXXXX.


C'est un jeu simpa, avec des rockets
ou l'on tire sur des enemies.

Il a été réalisé dans le cadre d'un
Projet au lycée en classe de NSI""")
        info_pts = Section("Points","texte","""Comment sont comptabiliser les points ?

Tirer             : -1 pt
Tuer un rouge     : +100pt
Tier sur un rouge : +10pt
""")
        info_opt_inp = Section("Inputs","texte","""Modifier vos touches dans conf.ini

Dans la section "INPUT", en utili-
sant les noms de touche pygame.

Liste des clées:
 - left  : bouger à gauche
 - right : bouger à droite
 - down  : bouger en bas
 - up    : bouger en haut
 - fire  : tirer
""")

        info_opt_gui = Section("Graphique","texte","""Modifier vos options dans conf.ini

Dans la section "GUI" vous avez:
ShowHitbox: si "T", affiche les hitboxes
""")
        info_opt = Section("Options", [info_opt_inp,info_opt_gui])
        info_opt.parent = "Information"
        info = Section("Information", [info_pts,info_opt,info_credits])
        info.parent = "Space Gamers"
        info_opt.action.append(info)
        menu = Section("Space Gamers", [Section("Jouer",self.play),info,Section("Quit",self.quit,"",(255,50,50),(255,100,100))],"logo")
        info.action.append(menu)
        self.active_section = menu
        self.__mainLoop()

    def play(self):
        logging.info("Setup main menu")
        self.valid_menu_sound.play()
        pygame.time.wait(20)
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        game = jeu()
        Gui = PyGameGUI(game)
        Gui.start(self.screen)


#######################################################################################################################################################

################################################## DEFINITION DES METHODES DE LA CLASSE PYGAMEGUI #####################################################

    # Méthode de la boucle principale
    def __mainLoop(self):
        self.screen = pygame.display.set_mode(self.size)
        logging.debug("GUI mainloop called !")
        self.running = True
        clock = pygame.time.Clock()
        exec_= 0
        time = 0
        title_font = pygame.font.Font('core/rsc/fonts/korona.ttf', 60)
        text_font = pygame.font.Font('core/rsc/fonts/syne.ttf', 45)
        desc_font = pygame.font.Font('core/rsc/fonts/syne.ttf', 22)
        selected = 0
        ret = 0

        #Tant que la boucle principale est en cours d'excution
        while self.running:

            # affichage du fond
            self.screen.blit(self.fond,(0,0))

            # now print the main text / logo
            if self.active_section.description != "logo":
                main = title_font.render(self.active_section.text,True, self.active_section.color)
                self.screen.blit(main,(25,20))
            else:
                main = self.logo
                self.screen.blit(main,(50,50))

            pressed = pygame.key.get_pressed()
            press = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:self.quit();break
                if event.type == pygame.KEYUP:
                    if pressed[self.touches[self.input_config["left"]]]: selected -= 1
                    elif pressed[self.touches[self.input_config["right"]]]: selected += 1
                    elif pressed[self.touches[self.input_config["up"]]]: selected -= 1
                    elif pressed[self.touches[self.input_config["down"]]]: selected += 1
                    selected %= len(self.active_section.action)
                    if pressed[self.touches[self.input_config["fire"]]]: press = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    press = True
                    pass # pressed[self.touches[self.input_config["fire"]]] = 1 # simule le clique de souris
            
            
            if isinstance(self.active_section.action,list):
                
                for x,value in enumerate(self.active_section.action):
                    if selected == x: pygame.draw.rect(self.screen,(255,255,100),(38,x*60+300-2,self.size[0]-76,60-1))
                    pygame.draw.rect(self.screen,(20,20,20,200),(40,x*60+300,self.size[0]-80,60-5))
                    ok = text_font.render(value.text,True, value.color)
                    if value.text == self.active_section.parent:
                        ok = text_font.render("Retour",True, (255,50,50))
                    self.screen.blit(ok,(60,x*60+300))


                if press:
                    if callable(self.active_section.action[selected].action):self.active_section.action[selected].action() # si l'action est une fontion, set
                    elif isinstance(self.active_section.action[selected].action,list): # si l'action est list de section
                        ret = self.active_section
                        self.active_section = self.active_section.action[selected]
                    elif isinstance(self.active_section.action[selected].action,str):
                        ret = self.active_section
                        self.active_section = self.active_section.action[selected]
                    selected = 0

            elif isinstance(self.active_section.action,str):
                pygame.draw.rect(self.screen,(20,20,20,200),(40,200,self.size[0]-80,400))

                for x,value in enumerate(self.active_section.description.split("\n")):
                    ok = desc_font.render(value, True, (255,255,255))
                    self.screen.blit(ok,(40,x*30+205))
                
                pygame.draw.rect(self.screen,(255,255,100),(38,598,self.size[0]-76,64))
                pygame.draw.rect(self.screen,(20,20,20,200),(40,600,self.size[0]-80,60))
                ok = text_font.render("return", True, (255,0,0))
                self.screen.blit(ok,(60,605))
                if press:
                    self.active_section = ret

            # flip
            pygame.display.flip()

    # Fermeture de la fenêtre
    def quit(self):
        logging.warn("Menu.quit() called !")
        pygame.quit()
        self.running = False
        sys.exit(0)

#######################################################################################################################################################

#######################################################################################################################################################
