from core.game import Game
from core.screen.mainmenu import MainMenuPygameGui as pg

def check_pygame_version():
    import logging
    import pygame.version as p
    
    if p.ver.startswith("1.9"): logging.info("BOnne version de pygame !"); return True

    logging.warning("Votre version de pygame n'est pas bonne: vous avez "+str(p.ver)+" et il vous faut la version 1.9.x")
    logging.info("Installation de la bonne version...")
    import os
    os.system("py -m pip install pygame==1.9.6")
    logging.info("\n\nInstallation réussi, veuillez redémarrer votre programme")

def set_up_logging():
    import logging
    logging.basicConfig(level=logging.DEBUG)
    outFormatter = logging.Formatter("[%(levelname)-5.5s] %(message)s")
    fileFormatter = logging.Formatter("%(asctime)s <%(filename)s:%(lineno)s - %(funcName)10s()> [%(levelname)-5.5s] %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.handlers = []

    fileHandler = logging.FileHandler("core/log.log")
    fileHandler.setFormatter(fileFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(outFormatter)
    rootLogger.addHandler(consoleHandler)
    logging.debug("Logging setup !")


if __name__ == "__main__":
    set_up_logging()
    check_pygame_version()
    Gui = pg()
    Gui.start()


