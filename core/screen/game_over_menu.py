﻿################################################ IMPORTATIONS DES MODULES NECESSAIRES ################################################
import logging
import pygame
import sys
from core.screen.section import Section
from core.classes.exeptions import *
#######################################################################################################################################





############################################### CREATION DE LA CLASSE PYGAMEGUI #######################################################

#Création de la classe PygameGui
class Game_Over():
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
    def __init__(self,screen,config_input,config_gui,touches,size,game,score):
        logging.debug("initialisation of Pygame...")
        pygame.mixer.music.stop()
        pygame.mixer.music.load("core/rsc/sounds/menu_music.mp3")
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.3)
        self.screen = screen
        self.running = False
        self.fond = pygame.image.load("core/rsc/img/game-over.png")
        self.config_gui = config_gui
        self.input_config = config_input
        self.touches = touches
        self.game = game
        self.size = size
        police = pygame.font.Font('core/rsc/fonts/GameBattle.ttf', 30)
        self.texte = police.render("SCORE : "+score,True,pygame.Color("#faf489"))
        self.texte_rect = self.texte.get_rect(center=(self.size[0]/2, 400))
        self.valid_menu_sound = pygame.mixer.Sound('core/rsc/sounds/menu_valid_sound.wav')
        menu = Section("", [Section("Rejouer",self.play),Section("Menu",self.main_menu),Section("Quitter",self.quit,"",(255,50,50),(255,100,100))])
        self.active_section = menu
        self.__mainLoop()

    def play(self):
        raise ReplayEx()

    def main_menu(self):
        raise MenuEx()


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
            self.screen.blit(self.texte,(self.texte_rect[0],225))



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
                    if pressed[self.touches[self.input_config["left"]]] or pressed[self.touches["K_LEFT"]]: selected -= 1
                    elif pressed[self.touches[self.input_config["right"]]] or pressed[self.touches["K_RIGHT"]]: selected += 1
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
