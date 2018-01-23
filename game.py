class Game(object):
	def __init__(self, grid, players):
		self.grid = grid
		self.players = players

		self.loopCount = 0

		self.startMainLoop()

	def startMainLoop(self):
		##self.drawGrid()

		while not self.checkVictory():
			self.loopCount += 1

			gridImage = grid.generateImage()
			print(gridImage)
			#print("Loop " + str(self.loopCount))

	def checkVictory(self)	:
		if self.loopCount < 100:
			return False
		else:
			return True

	def drawGrid(self):
		gridSize = self.grid.size
		gridString = ""

		rowBorder = ""
		for i in range(0, gridSize):
			rowBorder += "+-"
		rowBorder = rowBorder[:-1] + "\n"

		for y in range(0, gridSize):
			for x in range(0, gridSize):
				gridString += "| "
			
			if (y != gridSize -1):
				gridString += "\n" + rowBorder

		print(gridString)