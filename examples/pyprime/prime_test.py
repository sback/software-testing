import unittest
from prime import *

class TestCase(unittest.TestCase):
    def testNotPrimes(self):
        self.assertFalse(isPrime(1))
        self.assertFalse(isPrime(4))
        self.assertFalse(isPrime(20))
        self.assertFalse(isPrime(21))
        self.assertFalse(isPrime(22))
        self.assertFalse(isPrime(24))
    
    def testPrimes(self):
        self.assertTrue(isPrime(2))
        self.assertTrue(isPrime(3))
        self.assertTrue(isPrime(5))
        self.assertTrue(isPrime(23))

if __name__ == "__main__":
    unittest.main()
