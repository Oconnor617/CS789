from crypto.Euclidean import GCD, power
from crypto.Exponentiation import FastModExo
import random
from math import pow
from crypto.PrimRoots import *


"""This  is an implementation of the ElGamal Cipher Algorithm.
    For the Encryption side of the Algorithm, the user will provide a message to encrypt. This script will then generate a large 
    random number N (to be used as the modulus). It will then make a list of the elements of the multiplicative group of N. 
    From that list it will find all of the primitive roots of N. From there it will choose one primitive root, b, which will 
    serve as the basis of the keys and be used to encrypt the message"""

class PublicKey:
    """Keys will be represented as Objects. Here:
        p: A group chosen by both parties and agreed upon
        b: a primitive root of p
        h: h=b^r(modp) -> r is a secret random number that is chosen during the key generation phase"""
    def __init__(self,p,b,h):
        self.p = p
        self.b = b
        self.h = h

    def get_p(self):
        print("Public P: {}".format(self.p))
        return self.p

    def get_b(self):
        return self.b

    def get_h(self):
        print("Public H: {}".format(self.h))
        return self.h

class PrivateKey:
    """Keys will be represented as Objects. Here:
        p: A group chosen by both parties and agreed upon
        b: a primitive root of p
        r: a secret random number that is chosen during the key generation phase"""
    def __init__(self,p,b,r):
        self.p = p
        self.b = b
        self.r = r
            
    def get_p(self):
        print("Private P")
        return self.p

    def get_b(self):
        return self.b

    def get_r(self):
        return self.r

def key_gen(p):
    """This function will take a group P and genereate a Public/Private Key pair based upon that
    it will retuen a dictionary containing those two. What we will produce is:
    p: A group chosen by both parties and agreed upon
    b: a primitive root of p
    r: a secret random number
    h: h=b^r(modp) used for the public key"""
    b = findPrimitive(p) #Should be the smallest Primitive Root of P. This will be -1 if root DNE
    # Need to fix the Primitive Root Search Algorithm. It currently doesn't work for non prime
    r = random.randint(1,(p-1))  # random secret between 1 and p-1
    print("b = {}, r = {}".format(b,r))
    h = FastModExo(b,r,p) #Fast Exponentiation for h=g^r(mod p) used as part of the public key

    public = PublicKey(p,b,h)
    private = PrivateKey(p,b,r)
    return {'PublicKey': public, 'PrivateKey': private}

def gen_key(p):
    """This function will be used to generate private and public keys for Alice and Bob
        It will take a large number which has a cyclic group as input and use that as the basis
        to generate key based on n and random integers
    """
    key = random.randint(pow(10,20),p) #Generate a random key between 10^20 and n
    #for now we use Pythons built in Random until we make out own Random Int Algorithm
    while GCD(p,key) != 1:
        # if we are here then the GCD of n and the random key is not 1. So no Inverse in n. So choose a new one
        key = random.randint(pow(10,20),p)

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

