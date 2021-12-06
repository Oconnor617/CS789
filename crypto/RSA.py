"""This module wll contain code for performin RSA Encryption and Decryption based on user input. It will be passed two large Prime numbers and from there it will
crate Encryption and Dercryption Keys. """
from crypto.Exponentiation import isPrime
from crypto.Euclidean import GCD, power
import random

def rsa_keys(p,q):
    """This function will take tow large primes (p & q such that p!=q) as inputs and generate RSA Encryption/Decryption Keys based upon that."""
    #make sure the inputs are Prime - if not that would reall mess this all up
    """if isPrime(p) or isPrime(q):
       raise ValueError("The two numbers must be Prime!")
    elif p == q:
        raise ValueError("p and q cannot be the same number")
    """
    #n = pq
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi) # will have to change this to my own Psewudo Random Number Generator eventually

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = GCD(e,phi)
    while g != 1: # I guess g was not reletively prime
        e = random.randrange(1, phi) # try again
        g = GCD(e,phi)

    #when we are here we can assume GCD(e,phi)=1
    