import unittest
from stats import *

class TestCase(unittest.TestCase):
    def testExample(self):
        l = [31]
        stats(l)
    
    def testFullCoverage(self):
        ###Your code here.
        # Change l to something that manages full coverage. You may 
        # need to call stats twice with different input in order 
        # to achieve full coverage.
        l = [31]
        stats(l)

if __name__ == "__main__":
    unittest.main()
