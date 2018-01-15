# Author: Eric Timmerman
# This is the main functionality for the rest game
# This will include the dungeon object definition and some core utilities
# Later there may be a point to refactor the utilities into their own files
from random import sample
from random import randint

global curr

# Dungeon class, this is our main object and represents all of the rooms and the player
class Dungeon:

	# Initialize our dungeon, currently static info
	def __init__(self, name):
		self.cap = 10
		self.width = 4
		self.unused = [x for x in range(1,self.cap)]
		print self.unused
		self.in_progress = []
		self.used = []
		self.rooms=[[[1],"Entrance"]]
		self.room_build()
		print self.rooms
#		self.rooms=[[[2],"Entrance"],[[1,3],"Nothing"],[[2],"Dead-end"]]
		self.player={"name" : name, "pos" : 1}

	# Print out dungeon, show every room -> adjacent options
	def print_dungeon(self):
		for idx, room in enumerate(self.rooms):
			print str(idx) + " " + str(room[1]) + " -> " + str(room[0])
			print

	# Room validation utility, can be used for ensuring a room is defined
	def roomcheck(self, room_id):
		try:
			self.rooms[int(room_id - 1)]
		except NameError:
			print "That Room ID: " + str(room_id) + " does not exist"
			return False
		except IndexError:
			print "That Room ID: " + str(room_id) + " is unitialized"
			return False
		else:
			return 1

	# Move, this takes a room_id and returns the room_id if the player succeeds
	# in the move, False if cannot move
	def move(self, room_id):
		current_room = self._players_room()
		if self.roomcheck(room_id):
			if room_id in current_room[0]:
				self.player["pos"] = room_id
				return room_id
		return False

	def room_build(self):
		print "Building rooms"
		for room_id in list(self.unused):
				self.rooms.append([set([]),""])
		for room_id in list(self.unused):
			print room_id
			self._add_adj(room_id)
			self._clean_lists

	# Internal Helper Functions
	# Return player's current room, check the room list at the player's position
	def _players_room(self):
		return self.rooms[self.player["pos"] - 1]

	# Using the unused and in_progress lists choose the next adjacent rooms
	# Once a room is chosen it is added to the in_progress list
	def _add_adj(self, room_id):
		if not self.roomcheck(room_id):
			return False
#		elif len(self.rooms[room_id][0]) >= self.width:
#			return False
		print self.rooms
		candidates = self.unused + self.in_progress
		if room_id in candidates:
			candidates.remove(room_id)
		chosen = sample(candidates, randint(0,4)) 
		print chosen
		print room_id
		self.rooms[room_id][0] |= set(chosen)
		for x in chosen:
			self.rooms[x][0].add(room_id)
			if x not in self.in_progress:
				self.in_progress.append(x)
				self.unused.remove(x)
		return True

	# Moves the in_progress list into used
	def _clean_lists(self):
		for x in self.in_progress:
			self.used.append(x)
			self.in_progress.remove(x)


# Start - starts the game and initializes the dungeon object
def start(name):
	instance = Dungeon(name)
	return instance

def end(instance):
	del(instance)
	return True

if __name__ == '__main__':
	curr = start("Harold")
	curr.print_dungeon()
	print curr.player
	print curr.rooms[0]
