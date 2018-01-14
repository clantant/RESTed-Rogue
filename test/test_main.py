import unittest
import restgame

class DungeonValid(unittest.TestCase):

	def testStartUp(self):
		self.failUnless(restgame.start("foo"))

	def testCorrectRoom(self):
		self.failUnless(restgame.roomcheck(1))

def main():
	unittest.main()

if __name__ == '__main__':
	main()
