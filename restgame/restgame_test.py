import unittest
from restgame import *

class DungeonValid(unittest.TestCase):

	def testStartUp(self):
		self.failUnless(start("foo"))

	def testCorrectRoom(self):
		inst_test = start("foo")
		self.failUnless(inst_test.roomcheck(1))

def main():
	unittest.main()

if __name__ == '__main__':
	main()
