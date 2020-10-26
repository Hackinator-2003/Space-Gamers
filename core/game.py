import logging
from core.classes.player import Player
from core.classes.enemy import Enemy
from core.classes.bullet import Bullet
from core.classes.Boss import Boss
from core.configparser import get_config

class Game():

    def __init__(self):
        self.set_up_logging()
        logging.debug("init game...")
        logging.debug("loading config...")
        self.config = get_config()
        self.player = Player(self,[252,500])
        self.enemys = [Enemy(self,[30,30]),Enemy(self,[60,30]),Enemy(self,[90,30])]
        self.bullets = []
        self.boss = []



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







