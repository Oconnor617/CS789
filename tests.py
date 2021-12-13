"""This Module will hold my test cases for the functions and classes that I write. It should be run periodically througout development
    The automatic tests should be run as I make changes to the functions to ensure that they are still working properally.
    Since this cryptography simulation is made using a Flask app the tests.py will need to have context of the Flask app in order to properally run
    run the tests. It will make use of Python's unittest framework.
"""
from crypto import app
from crypto.Euclidean import *
from crypto.Exponentiation import *
from crypto.Helpers import *
from crypto.PseudoRandoms import *
import unittest

class FunctionTests(unittest.TestCase):
    """A Class for my function unittests"""

    def test_modular_exponentiation(self):
        b,e,p = 11,3357,10
        r = FastModExo(b,e,p) #11^(3357)mod10 = 1 from the midterm
        self.assertEqual(r,1)

    def test_gcd(self):
        self.assertEqual(GCD(55,123),1)
        self.assertEqual(GCD(131,87),1)

    def test_order(self):
        """Test function to deteriming the size of a numbers multiplicative group"""
        self.assertEqual(Order(100),40) #should be 40 from the Midterm
        self.assertEqual(Order(23),22)
        self.assertEqual(Order(77813),77812)
    
    def test_miller_rabin(self):
        """Primality tests using Miller-Rabin"""
        self.assertTrue(isPrimeMR(77813))
        self.assertTrue(isPrimeMR(23))
        self.assertFalse(isPrimeMR(40))

if __name__ == '__main__':
    unittest.main(verbosity=2)