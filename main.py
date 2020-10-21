from core.game import Game
from core.GUI import PygameGui

if __name__ == "__main__":
    game = Game()
    Gui = PygameGui(game)
    Gui.start()


