import solution_one
import unittest

class testSolutionOne(unittest.TestCase):
   
    def testChop(self):
        self.assertEqual(-1, solution_one.main(3, []))
        pass

if __name__ == '__main__':
    unittest.main()
