class Grid(object):
	def __init__(self, size):
		self.size = size

		self.gridArray = self.generateGridArray()

		print(self.gridArray)

		self.rowBorder = self.generateRowBorder()

	def generateRowBorder(self):
		rowBorder = ""
		for i in range(0, self.gridSize):
			rowBorder += "+-"
		rowBorder = rowBorder[:-1] + "\n"

	def generateGridImage(self):
		

	def generateGridArray(self):
		gridSize = self.size
		gridString = ""

		gridArray = []


		for y in range(0, gridSize):
			gridArray.append([])

			for x in range(0, gridSize):
				gridArray[y].append("")

		return gridArray



		rowBorder = self.rowBorder

		for y in range(0, gridSize):
			for x in range(0, gridSize):
				gridString += "| "
			
			if (y != gridSize -1):
				gridString += "\n" + rowBorder

		print(gridString)