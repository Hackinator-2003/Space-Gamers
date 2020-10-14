import logging

class Game():
    def __init__(self):
        self.set_up_logging()
        logging.debug("Instance done !")
    
    def start(self):
        logging.info("game starting")
        
    
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