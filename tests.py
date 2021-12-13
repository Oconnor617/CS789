"""This Module will hold my test cases for the functions and classes that I write. It should be run periodically througout development
    The automatic tests should be run as I make changes to the functions to ensure that they are still working properally.
    Since this cryptography simulation is made using a Flask app the tests.py will need to have context of the Flask app in order to properally run
    run the tests. It will make use of Python's unittest framework.
"""
from crypto import app
from crypto.Euclidean import *
from crypto.Exponentiation import *
from crypto.Helpers import *
from crypto.PrimRoots import findPrimitive
from crypto.PseudoRandoms import *
from crypto.RSA import *
import unittest

class FunctionTests(unittest.TestCase):
    """A Class for my function unittests"""

    def test_modular_exponentiation(self):
        """Test cases for Fast Modular Exponentiation"""
        b,e,p = 11,3357,10
        r = FastModExo(b,e,p) #11^(3357)mod10 = 1 from the midterm
        self.assertEqual(r,1)
        self.assertEqual(FastModExo(56,12321,5645),4096)

    def test_gcd(self):
        """Test Cases for Euclid's GCD Algorithm"""
        self.assertEqual(GCD(55,123),1)
        self.assertEqual(GCD(131,87),1)

    def test_modInverse(self):
        """Test function for calculating the Modular Inverse of a number"""
        self.assertEqual(modinv(3,26),9)
        self.assertEqual(modinv(9,26),3)
        self.assertEqual(modinv(44,3369),536)
        self.assertEqual(modinv(536,3369),44)
        self.assertEqual(modinv(13,3369),1555)

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
    
    def test_smallest_root(self):
        """Test cases for finding the smallest Primitive Root. Used in El Gamal"""
        self.assertEqual(findPrimitive(23),5)
        self.assertEqual(findPrimitive(40),-1) #should be no Primitive Root and my Algorithm returns 1 if DNE
        self.assertEqual(findPrimitive(74561),3)

    def test_baby_giant(self):
        """Test cases for the Baby-Step Giant-Step solution for the Discrete Log which solves for x in h=g^x(modp)"""
        self.assertEqual(bsgs(5,8,23),6)
        self.assertEqual(bsgs(5,21,23),13)
        self.assertEqual(bsgs(7894352216,355407489,604604729),102900819)
        self.assertEqual(bsgs(135,56465,654),32)

    def test_pollards(self):
        """Test cases for Pollards p-1 Algorithm"""
        p=26713
        q=17981
        n = p*q
        res1,res2 = pollard_result(n)
        self.assertTrue(((res1 == p) or (res1 == q)))
        self.assertTrue(((res2 == p) or (res2 == q)))

    def test_rsa_simulation(self):
        """Test function that will essentially simulate a Alice/Bob/Eve RSA exchange"""
        alice_e = 178512487
        alice_d = 658290871
        n = 749458163 #n is the product of two primes
        bob_msg = 44 #the message Bob will encrypt to Alice using E(x)
        msg_enc = rsa_enc(bob_msg,alice_e,n) #should be (bob-msg)^alice_e (modn)
        self.assertEqual(msg_enc,374155687) #(44^178512487)mod(749458163)=374155687 - Assert that the Encryption Works
        msg_dec = rsa_dec(msg_enc,alice_d,n) #(374155687^658290871)mod(749458163) = 44
        self.assertEqual(msg_dec,bob_msg) # Assert that the Decryption works
        #time for Eve's attack
        eve = rsa_eve(msg_enc,alice_e,n)
        self.assertEqual(bob_msg,eve) #Assert that Eve can break the message by Factoring Primes

if __name__ == '__main__':
    unittest.main(verbosity=2)