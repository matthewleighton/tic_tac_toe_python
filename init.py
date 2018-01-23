from grid import Grid
from game import Game
from player import Player

players = [
	Player(0),
	Player(1)
]

#exit()

grid = Grid(3)

game = Game(grid, players)