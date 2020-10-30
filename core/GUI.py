
################################################ IMPORTATIONS DES MODULES NECESSAIRES ################################################
import logging
import pygame
from core.classes.enemy import Enemy
from core.classes.bullet import Bullet
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
    speed = 200


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
        time = 0

        #Tant que la boucle principale est en cours d'excution
        while self.running:

            # Calculation du delaTime utile pour les transitions
            self.dt = clock.tick()/1000
            exec_ += self.dt

            # affichage du fond
            self.screen.blit(self.fond,(0,0))


            police = pygame.font.Font(None,55)
            texte = police.render(str(round(exec_)),True,pygame.Color("#FFFFFF"))
            texte_rect = texte.get_rect(center=(self.size[0]/2, 0))
            self.screen.blit(texte,(texte_rect[0],10))


            # affichage du joueur
            self.screen.blit(self.game.player.vaisceau,(self.game.player.pos[0],self.game.player.pos[1]))
            fire = pygame.image.load("core/rsc/img/tire.png")


            # affichage de la vie / écran de game-over
            if self.game.player.pv==3: point_de_vie =  pygame.image.load("core/rsc/img/3_coeurs.png")
            elif self.game.player.pv==2: point_de_vie =  pygame.image.load("core/rsc/img/2_coeurs.png")
            elif self.game.player.pv==1: point_de_vie =  pygame.image.load("core/rsc/img/1_coeur.png")
            elif self.game.player.pv==0: point_de_vie =  pygame.image.load("core/rsc/img/game-over.png")

            self.screen.blit(point_de_vie,(0,0))


            pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:self.quit();break

            pressed = pygame.key.get_pressed()
            if pressed[self.touches[self.input_config["left"]]]: self.game.player.left(self.dt)
            if pressed[self.touches[self.input_config["right"]]]: self.game.player.right(self.dt)
            if pressed[self.touches[self.input_config["up"]]]: self.game.player.up(self.dt)
            if pressed[self.touches[self.input_config["down"]]]: self.game.player.down(self.dt)

            if pressed[self.touches[self.input_config["fire"]]]:
                self.game.player.shoot(self.dt)


            if self.game.bullets != None:
                for bullet in self.game.bullets:
                    bullet.move(self.dt)


                    if bullet.pos[1]<0 or bullet.pos[1]>700-79:

                        for i,x in enumerate(self.game.bullets):
                            if x == bullet:
                                del self.game.bullets[i]

                    elif bullet.type_ == "down" and (((bullet.pos[0]>=self.game.player.pos[0] and bullet.pos[0]<=self.game.player.pos[0]+60)or(bullet.pos[0]+35>=self.game.player.pos[0] and bullet.pos[0]+35<=self.game.player.pos[0]+60)) and ((bullet.pos[1]>=self.game.player.pos[1] and bullet.pos[1]<=self.game.player.pos[1]+60)or(bullet.pos[1]+79>=self.game.player.pos[1] and bullet.pos[1]+79<=self.game.player.pos[1]+60))):

                        self.game.player.degat()
                        for i,x in enumerate(self.game.bullets):
                            if x == bullet:
                                del self.game.bullets[i]

                    else:

                        for enemy in self.game.enemys:

                            if  bullet.type_ == "up" and (((bullet.pos[0]>=enemy.pos[0] and bullet.pos[0]<=enemy.pos[0]+60)or(bullet.pos[0]+35>=enemy.pos[0] and bullet.pos[0]+35<=enemy.pos[0]+60)) and ((bullet.pos[1]>=enemy.pos[1] and bullet.pos[1]<=enemy.pos[1]+60)or(bullet.pos[1]+79>=enemy.pos[1] and bullet.pos[1]+79<=enemy.pos[1]+60))):

                                enemy.degat()
                                for i,x in enumerate(self.game.bullets):
                                    if x == bullet:
                                        del self.game.bullets[i]

                        for boss in self.game.boss:
                            if bullet.type_ == "up" and (((bullet.pos[0]>=boss.pos[0] and bullet.pos[0]<=boss.pos[0]+212)or(bullet.pos[0]+35>=boss.pos[0] and bullet.pos[0]+35<=boss.pos[0]+212)) and ((bullet.pos[1]>=boss.pos[1] and bullet.pos[1]<=boss.pos[1]+189)or(bullet.pos[1]+79>=boss.pos[1] and bullet.pos[1]+79<=boss.pos[1]+189))):
                                boss.degat()
                                for i,x in enumerate(self.game.bullets):
                                    if x == bullet:
                                        del self.game.bullets[i]




            for bullet in self.game.bullets:
                bullet.update(self.dt)
                self.screen.blit(fire,(bullet.pos[0],bullet.pos[1]))


            if round(exec_)!=0 and round(exec_)%60.0 == 0:
                if len(self.game.boss)<1:
                    self.game.boss.append(Boss(self.game,[200,100],100))




            for boss in self.game.boss:
                bosse = pygame.image.load("core/rsc/img/blue-enemy.png")
                self.screen.blit(bosse,(boss.pos[0],boss.pos[1]))
                boss.move(self.dt,self.speed)
                boss.shoot(self.dt)



            # flip
            pygame.display.flip()

            # call update on entitys
            self.game.player.update(self.dt)

            for boss in self.game.boss:
                boss.update(self.dt)

            for enemy in self.game.enemys:
                enemy.update(self.dt)


    # Fermeture de la fenêtre
    def quit(self):
        logging.warn("Gui.quit() called !")
        pygame.quit()
        self.running = False
        exit()

#######################################################################################################################################################

#######################################################################################################################################################
