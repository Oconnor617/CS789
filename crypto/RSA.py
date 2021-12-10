"""This module wll contain code for performin RSA Encryption and Decryption based on user input. It will be passed two large Prime numbers and from there it will
crate Encryption and Dercryption Keys. """
from crypto.Exponentiation import FastModExo
from crypto.Euclidean import GCD, egcd, modinv
from crypto.PseudoRandoms import isPrimeMR
import random

class RSAEncKey:
    """Keys will be represented as Objects. Here:
        e: encryption key. Must have an inverse in Psi(n)
        n: a product of two Primes p & q
    """

    def __init__(self,e,n):
        self.e = e
        self.n = n

    def get_e(self):
        return self.e

    def get_n(self):
        return self.n

class RSADecKey:
    """Keys will be represented as Objects. Here:
        d: decryption key. Mustbe the inverse of e in Psi(n)
        n: a product of two Primes p & q
    """

    def __init__(self,d,n):
        self.d = d
        self.n = n

    def get_d(self):
        return self.d

    def get_n(self):
        return self.n

def rsa_keys(p,q):
    """This function will take tow large primes (p & q such that p!=q) as inputs and generate RSA Encryption/Decryption Keys based upon that."""
    #make sure the inputs are Prime - if not that would reall mess this all up
    """if isPrimeMR(p) or isPrimeMR(q):
       raise ValueError("The two numbers must be Prime!")
    elif p == q:
        raise ValueError("p and q cannot be the same number")
    """
    #Since we are calling this from routes.py we can confirm there that p&q are Prime before calling
    #n = pq
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = GCD(e,phi)
    while g != 1: # I guess g was not reletively prime
        e = random.randrange(1, phi) # try again
        g = GCD(e,phi)

    #when we are here we can assume GCD(e,phi)=1 which means it has an inverse in Zn
    #So find it using the Multiplicative Inververe via Extended Euclidean
    d = modinv(e,phi) #hopefully d is the inverse of e under phi

    #Public key is (e, n) and private key is (d, n)
    print("Public Key: ({},{})".format(e,n))
    print("Private Key: ({},{})".format(d,n))
    encryption_key = RSAEncKey(e,n)
    decryption_key = RSADecKey(d,n)
    return {'EncKey': encryption_key, 'DecKey': decryption_key}

def rsa_enc(num,e,n):
    """This is the encryption function for RSA encryption. Since my group is passing encrypted numbers this function will currently only work for encrypting/decrypting numbers
    Not letters or characters. It will have three parameters
    e: The sender's Encryption Key
    n: The product of the two primes p & q
    num: The number to be encrypted""" 
    enc = FastModExo(num,e,n) #should be num^e(modn)
    return enc

def rsa_dec(num_enc,d,n):
    """This is the encryption function for RSA encryption. Since my group is passing encrypted numbers this function will currently only work for encrypting/decrypting numbers
    Not letters or characters. It will have three parameters
    d: The reciever's Decryption Key: This should be the inverse of e in modn
    n: The product of the two primes p & q
    num_enc: The encrypted number to be decrypted""" 
    dec = FastModExo(num_enc,d,n) # should be (num^e)^d=(num)^ed=num since e & d should be inverses modn
    print(dec)
    return dec