from crypto.Euclidean import GCD, power
from crypto.Exponentiation import FastModExo
import random
from math import pow
"""This  is an implementation of the ElGamal Cipher Algorithm.
    For the Encryption side of the Algorithm, the user will provide a message to encrypt. This script will then generate a large 
    random number N (to be used as the modulus). It will then make a list of the elements of the multiplicative group of N. 
    From that list it will find all of the primitive roots of N. From there it will choose one primitive root, b, which will 
    serve as the basis of the keys and be used to encrypt the message"""

def gen_key(n):
    """This function will be used to generate private and public keys for Alice and Bob
        It will take a large number which has a cyclic group as input and use that as the basis
        to generate key based on n and random integers
    """
    key = random.randint(pow(10,20),n) #Generate a random key between 10^20 and n
    #for now we use Pythons built in Random until we make out own Random Int Algorithm
    while GCD(n,key) != 1:
        # if we are here then the GCD of n and the random key is not 1. So no Inverse in n. So choose a new one
        key = random.randint(pow(10,20),n)

    return key # Return this key becasue it must have an inverse in Zn

def encrypt(msg,n):
    """A function to encrypt a message. It will take a message to encrypt, 
        n: the random number to be used to genreate the keys
        g: a random int between 2 and n which is an element of Zn
        h: g^a(modn) where a is a samll random int probably use 3 - use Fast Modular Exponentiation
        This will return an encrypted message as well as a value p where
        p: g^k(modn) where k is the private key of the sender.
    """
    a = 3 #might change this later
    k = gen_key(n) # a new private key for the person encrypting this meassage
    g = random.randint(2,n)
    h = FastModExo(g,k,n)

