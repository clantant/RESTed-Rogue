import unittest
from restgame import *

global inst_test
inst_test = start("foo")

class DungeonValid(unittest.TestCase):

	def setUp(self):
		inst_test = start("foo")

	def tearDown(self):
		end(inst_test)

	def testStartUpSuccess(self):
		self.failUnless(start("bar"))

	@unittest.skip("No colliding startup concerns at this time")
	def testStartUpFailOnSame(self):
		self.assertFalse(start("foo"))

	def testCorrectRoom(self):
		self.failUnless(inst_test.roomcheck(1))

	def testMoveSuccess(self):
		self.assertEqual(inst_test.move(2), 2)

	def testMoveFail(self):
		self.assertFalse(inst_test.move(3))
		
def main():
	unittest.main()

if __name__ == '__main__':
	main()
