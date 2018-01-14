# This is the main functionality for the rest game
# This will include the dungeon object definition and some core utilities
# Later there may be a point to refactor the utilities into their own files

# Dungeon class, this is our main object and represents all of the rooms and the player
class Dungeon:
	def __init__(self, name):
		self.rooms=[]
		self.player={"name" : name, "pos" : 1}

# Start - starts the game and initializes the dungeon object
def start(name):
	instance = Dungeon(name)
	return 1
