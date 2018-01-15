# This is the main functionality for the rest game
# This will include the dungeon object definition and some core utilities
# Later there may be a point to refactor the utilities into their own files

global curr


# Dungeon class, this is our main object and represents all of the rooms and the player
class Dungeon:

	# Initialize our dungeon, currently static info
	def __init__(self, name):
		self.rooms=[[[2],"Entrance"],[[1,3],"Nothing"],[[2],"Dead-end"]]
		self.player={"name" : name, "pos" : 1}

	# Print out dungeon, show every room -> adjacent options
	def print_dungeon(self):
		for room in self.rooms:
			print str(room[1]) + " -> " + str(room[0])
			print

	# Room validation utility, can be used for ensuring a room is defined
	def roomcheck(self, room_id):
		try:
			self.rooms[int(room_id - 1)]
		except NameError:
			print "That Room ID " + str(room_id) + " does not exist"
			return False
		else:
			return 1



# Start - starts the game and initializes the dungeon object
def start(name):
	instance = Dungeon(name)
	return instance

if __name__ == '__main__':
	curr = start("Harold")
	curr.print_dungeon()
	print curr.player
	print curr.rooms[0]
