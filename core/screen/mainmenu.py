﻿################################################ IMPORTATIONS DES MODULES NECESSAIRES ################################################
import logging
import pygame
from core.game import Game as jeu
from core.GUI import PygameGui as PyGameGUI
import sys
from core.configparser import get_config, save_config
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
        pygame.mixer.music.set_volume(0.3)
        self.touches = {key:value for key,value in pygame.__dict__.items() if key[:2] == "K_" or key[:2] == "KM"}
        self.touches["K_MOUSE"] = len(self.touches.keys())
        logging.debug("pygame.__dict__:"+"".join([str(x)+":"+str(y)+", " for x,y in self.touches.items()]))
        logging.debug("touches={"+"".join([str(x)+":"+str(y)+", " for x,y in self.touches.items()])+"}")
        logging.debug("Creating sections")

        info_credits = Section("Credits","texte","""Ce jeu à été réaliser par Cyprien
Bourotte, Aurélien Kittel et Marc Guillemot.


C'est un jeu simpa, avec des rockets
ou l'on tire sur des enemies.

Il a été réalisé dans le cadre d'un
Projet au lycée en classe de NSI""")
        info_pts = Section("Points","texte","""Comment sont comptabiliser les points ?

Tirer             : -1   pt
Perdre une vie    : -200 pts
Tuer un rouge     : +100 pts
Tirer sur un rouge: +10  pts
""")
        info_opt_inp = Section("Inputs","texte","""Modifier vos touches dans conf.ini

Dans la section "INPUT", en utili-
sant les noms de touche pygame +
K_MOUSE pour click souris.

Liste des clées:
 - left  : bouger à gauche
 - right : bouger à droite
 - down  : bouger en bas
 - up    : bouger en haut
 - fire  : tirer
""")

        info_opt_gui = Section("Graphique","texte","""Modifier vos options dans conf.ini

Dans la section "GUI" vous avez:
ShowHitbox: si "T", affiche
            les hitboxes
""")
        touches = Section("Touches",
            [Section("<touches1.png", self.setconfig_zqsd),
             Section("<touches2.png", self.setconfig_fleches)]
        )
        touches.parent = "Space Gamers"
        info_opt = Section("Options", [info_opt_inp,info_opt_gui])
        info_opt.parent = "Information"
        info = Section("Information", [info_pts,info_opt,info_credits])
        info.parent = "Space Gamers"
        info_opt.action.append(info)
        menu = Section("Space Gamers", [Section("Jouer",self.play),touches,info,Section("Quit",self.quit,"",(255,50,50),(255,100,100))],"logo")
        info.action.append(menu)
        touches.action.append(menu)
        self.active_section = menu
        self.__mainLoop()

    def setconfig_zqsd(self):
        self.config["INPUT"]["left"] = "K_a"
        self.config["INPUT"]["right"] = "K_d"
        self.config["INPUT"]["up"] = "K_w"
        self.config["INPUT"]["down"] = "K_s"
        self.config["INPUT"]["fire"] = "K_MOUSE"
        save_config(self.config)

    def setconfig_fleches(self):
        self.config["INPUT"]["left"] = "K_LEFT"
        self.config["INPUT"]["right"] = "K_RIGHT"
        self.config["INPUT"]["up"] = "K_UP"
        self.config["INPUT"]["down"] = "K_DOWN"
        self.config["INPUT"]["fire"] = "K_SPACE"
        save_config(self.config)



    def play(self):
        logging.info("Setup main menu")
        self.valid_menu_sound.play()
        pygame.time.wait(20)
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        game = jeu(self.config)
        Gui = PyGameGUI(game)
        Gui.start(self.screen)


#######################################################################################################################################################

################################################## DEFINITION DES METHODES DE LA CLASSE PYGAMEGUI #####################################################

    # Méthode de la boucle principale
    def __mainLoop(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Space Invader")
        logging.debug("GUI mainloop called !")
        self.running = True
        clock = pygame.time.Clock()
        exec_= 0
        time = 0
        title_font = pygame.font.Font('core/rsc/fonts/GameBattle.ttf', 40)
        text_font = pygame.font.Font('core/rsc/fonts/Game.ttf', 50)
        desc_font = pygame.font.Font('core/rsc/fonts/syne.ttf', 22)
        selected = 0
        ret = 0
        self.ismousedown = False

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


  
            press = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:self.quit();break
                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()

                    if isinstance(self.active_section.action,list):
                        if 40 <= pos[0] <= self.size[0]-40:
                            for x,value in enumerate(self.active_section.action):
                                if x*60+300 <= pos[1] <= x*60+355: selected = x

                if event.type == pygame.MOUSEBUTTONDOWN:
                    press = True
                    pass # pressed[self.touches[self.input_config["fire"]]] = 1 # simule le clique de souris
                
                if event.type == pygame.KEYDOWN:
                    self.ismousedown = pygame.mouse.get_pressed() == 1
                    pressed = list(pygame.key.get_pressed())
                    pressed.append(self.ismousedown)
                    #logging.debug("pressed len="+str(len(pressed))+" pressed="+str(pressed))
                    logging.debug("Button down event!")
                    if pressed[self.touches[self.input_config["left"]]] or pressed[self.touches["K_LEFT"]]: selected += 1
                    elif pressed[self.touches[self.input_config["right"]]] or pressed[self.touches["K_RIGHT"]]: selected -= 1
                    elif pressed[self.touches[self.input_config["up"]]] or pressed[self.touches["K_UP"]]: selected -= 1
                    elif pressed[self.touches[self.input_config["down"]] or pressed[self.touches["K_DOWN"]]]: selected += 1
                    selected %= len(self.active_section.action)
                    if pressed[self.touches[self.input_config["fire"]]] or pressed[self.touches["K_SPACE"]] or pressed[self.touches["K_RETURN"]]: press = True
            


            if isinstance(self.active_section.action,list):

                for x,value in enumerate(self.active_section.action):
                    if selected == x: pygame.draw.rect(self.screen,(255,255,100),(38,x*60+300-2,self.size[0]-76,60-1))
                    pygame.draw.rect(self.screen,(20,20,20,200),(40,x*60+300,self.size[0]-80,60-5))
                    if value.text.startswith("<"):
                        img = pygame.image.load("core/rsc/img/"+"<".join(value.text.split("<")[1:]))
                        self.screen.blit(img, (40,x*60+300))
                    else:
                        if value.text == self.active_section.parent:
                            ok = text_font.render("Retour",True, (255,50,50))
                        else:ok = text_font.render(value.text,True, value.color)
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
                pygame.draw.rect(self.screen,(20,20,20,200),(40,150,self.size[0]-80,400))

                for x,value in enumerate(self.active_section.description.split("\n")):
                    ok = desc_font.render(value, True, (255,255,255))
                    self.screen.blit(ok,(40,x*30+155))

                pygame.draw.rect(self.screen,(255,255,100),(38,598,self.size[0]-76,64))
                pygame.draw.rect(self.screen,(20,20,20,200),(40,600,self.size[0]-80,60))
                ok = text_font.render("Retour", True, (255,50,50))
                self.screen.blit(ok,(60,605))
                if press:
                    self.active_section = ret

            # flip
            pygame.display.flip()
            pygame.event.pump()

    # Fermeture de la fenêtre
    def quit(self):
        logging.warn("Menu.quit() called !")
        pygame.quit()
        self.running = False
        sys.exit(0)

#######################################################################################################################################################

#######################################################################################################################################################
