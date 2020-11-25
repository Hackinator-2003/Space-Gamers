from core.game import Game
from core.screen.mainmenu import MainMenuPygameGui as pg



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
    Gui = pg()
    Gui.start()


