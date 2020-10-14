from core.game import Game
from core.GUI import PygameGui

if __name__ == "__main__":
    Gui = PygameGui((700,700))
    game = Game()
    Gui.start()
    game.start()
