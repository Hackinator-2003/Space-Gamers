import logging
from core.classes.player import*
from core.configparser import get_config

class Game():

    def __init__(self):
        self.set_up_logging()
        logging.debug("init game...")
        logging.debug("loading config...")
        self.config = get_config()
        self.player = Player((252,500))
        self.enemys = [Enemy((30,30)),Enemy((60,30)),Enemy((90,30))]

    def start(self):
        logging.info("game starting")


    def set_up_logging(self):
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



