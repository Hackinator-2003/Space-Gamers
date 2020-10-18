import logging
from core.classes.player import*

class Game():

    def __init__(self,dimentions=(20,20)):
        self.set_up_logging()
        logging.debug("Instance done !")
        self.dimentions = dimentions
        self.joueur = self.generate(Player)
        self.enemy = self.generate(Enemy)
        self.start()


    def start(self):
        logging.info("game starting")
        PygameGui.screen.blit(vaisceau,(Player.pos_init[0],Player.pos_init[1]))
        pygame.display.flip()




    def set_up_logging(self):
        logging.basicConfig(level=logging.DEBUG)
        outFormatter = logging.Formatter("[%(levelname)-5.5s] %(message)s")
        fileFormatter = logging.Formatter("%(asctime)s <%(filename)s:%(lineno)s - %(funcName)10s()> [%(levelname)-5.5s] %(message)s")
        rootLogger = logging.getLogger()
        rootLogger.handlers = []

        fileHandler = logging.FileHandler("core/log")
        fileHandler.setFormatter(fileFormatter)
        rootLogger.addHandler(fileHandler)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(outFormatter)
        rootLogger.addHandler(consoleHandler)


    def generate(self,entite):

        if entite==Player:
            player=entite([Player.pos_init[0],Player.pos_init[1]],3)
            return player
        else:
            return None


