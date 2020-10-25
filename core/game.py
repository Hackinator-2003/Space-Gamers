import logging
from core.classes.player import Player
from core.classes.enemy import Enemy
from core.classes.bullet import Bullet
from core.configparser import get_config

class Game():

    def __init__(self):
        logging.debug("init game...")
        logging.debug("loading config...")
        self.config = get_config()
        self.player = Player(self,[252,500])
        self.enemys = [Enemy(self,[30,30]),Enemy(self,[60,30]),Enemy(self,[90,30])]
        self.bullets = []



    def start(self):
        logging.info("game starting")







