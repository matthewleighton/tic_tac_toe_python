class Player(object):
	def __init__(self, number):
		self.number = number
		self.symbol = "O" if number == 0 else "X"

		#print("Player " + str(self.number) + ": " + self.symbol)