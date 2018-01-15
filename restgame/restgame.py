"""Dungeon Crawler for working with a REST api"""
# Author: Eric Timmerman
# This is the main functionality for the rest game
# This will include the dungeon object definition and some core utilities
# Later there may be a point to refactor the utilities into their own files
from random import sample
from random import randint
from pprint import pformat
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
global CURR
global EVENTS
EVENTS = ['Nothing', 'Monster', 'Treasure', 'Maw of madness', 'Spiraling shape']

class Dungeon:
    """this is our main object and represents all of the rooms on 1 floor and the player"""

    def __init__(self, name):
        """Set maxes and limits"""
        self.cap = 10
        self.width = 4
        self.unused = [x for x in range(1, self.cap)]
        self.in_progress = []
        self.used = []
        self.rooms = [[[1], "Entrance"]]
        self.room_build()
        self.floor = 1
        self.event_assign()
        logging.debug("Rooms: " + pformat(self.rooms) + "unused: " + pformat(self.unused))
        self.player = {"name" : name, "pos" : 1}

    def print_dungeon(self):
        """show every room -> adjacent options"""
        for idx, room in enumerate(self.rooms):
            logging.debug(pformat(idx) + " " + pformat(room[1]) + " -> " + pformat(room[0]))

    def roomcheck(self, room_id):
        """Room validation utility, can be used for ensuring a room is defined"""
        try:
            self.rooms[int(room_id - 1)]
        except NameError:
            logging.error("That Room ID: " + pformat(room_id) + " does not exist")
            return False
        except IndexError:
            logging.error("That Room ID: " + pformat(room_id) + " is unitialized")
            return False
        else:
            return 1

    def move(self, room_id):
        """this takes a room_id and returns the room_id if the player succeeds
        in the move, False if cannot move"""
        current_room = self._players_room()
        if self.roomcheck(room_id):
            if room_id in current_room[0]:
                self.player["pos"] = room_id
                return room_id
        return False

    def room_build(self):
        """First populates the floor then builds the connections between rooms"""
        logging.debug("Building rooms")
        # Taking two passes, the first generates the individual rooms
        for room_id in list(self.unused):
            self.rooms.append([set([]), ""])

        # The second puts the adjacent rooms into the lists of both rooms
        for room_id in list(self.unused):
            self._add_adj(room_id)
            self._clean_lists

    def event_assign(self):
        """Choose end stairs and assign 1 or 2 random events to the rest of the rooms"""
        stairs = randint(1, self.cap - 1)
        logging.debug("Room chosen for stairs: " + pformat(stairs))
        self.rooms[stairs][1] = "The Stairs down!"
        self.rooms[stairs][0].add('>')
        for room in self.rooms:
            if room[1] == "":
                new_event = sample(EVENTS, randint(1, 2))
                if len(new_event) > 1:
                    room[1] = ' and '.join(new_event)
                else:
                    room[1] = str(new_event[0])

    # Internal Helper Functions
    def _players_room(self):
        """Return player's current room, check the room list at the player's position"""
        return self.rooms[self.player["pos"] - 1]

    def _add_adj(self, room_id):
        """Using the unused and in_progress lists choose the next adjacent rooms
         Once a room is chosen it is added to the in_progress list"""
        if not self.roomcheck(room_id):
            return False
        logging.debug("Rooms: " + pformat(self.rooms))
        candidates = self.unused + self.in_progress
        if room_id in candidates:
            candidates.remove(room_id)
        chosen = sample(candidates, randint(1, 3))
        logging.debug("Room ID: " + pformat(room_id) + " Chosen: " + pformat(chosen))
        for x in chosen:
            self.rooms[x][0].add(room_id)
            if x not in self.in_progress:
                self.in_progress.append(x)
                self.unused.remove(x)
        self.rooms[room_id][0] |= set(chosen)
        return True

    def _clean_lists(self):
        """Moves the in_progress list into used"""
        for x in self.in_progress:
            self.used.append(x)
            self.in_progress.remove(x)


def start(name):
    """starts the game and initializes the dungeon object"""
    instance = Dungeon(name)
    return instance

def end(instance):
    """Destroys the instance"""
    del instance
    return True

if __name__ == '__main__':
    CURR = start("Harold")
    CURR.print_dungeon()
    logging.debug(CURR.player)
    logging.debug(CURR.rooms[0])
