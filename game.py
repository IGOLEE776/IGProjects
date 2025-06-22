# 0_0 WHAT

from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Player
#from player import Player

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        x, y = self.land.loadLand('land2.txt')
        self.hero = Player((x//2, y//2, 2), self.land)
        base.camLens.setFov(90) # type: ignore

game = Game()
game.run()