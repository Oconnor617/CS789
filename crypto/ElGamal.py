from crypto.Euclidean import GCD
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

def key_gen_root(p,b):
    """This function will take a group P and genereate a Public/Private Key pair based upon that
    it will retuen a dictionary containing those two. What we will produce is:
    p: A group chosen by both parties and agreed upon
    b: a primitive root of p
    r: a secret random number
    h: h=b^r(modp) used for the public key"""

    r = random.randint(1,(p-1))  # random secret between 1 and p-1
    print("b = {}, r = {}".format(b,r))
    h = FastModExo(b,r,p) #Fast Exponentiation for h=g^r(mod p) used as part of the public key

    public = PublicKey(p,b,h)
    private = PrivateKey(p,b,r)
    return {'PublicKey': public, 'PrivateKey': private}

def encrypt(msg,pkb,r,p):
    """ This will function will have a few parameters
        msg: A plain text message that Alice wants to encrypt & send to Bob
        pkb: Bob's public key which will be used for the encryption. pkb will consist of:
            p: A group chosen by both parties and agreed upon
            b: a primitive root of p
            h: h=b^l(modp) only bob knows l but Alice will use h to encrypt the message with
        r: Alice's private key
    """
    en_msg = [] # we are going to encrypt the plaintext letter by letter so have an empty array
    print(len(msg))
    print(type(msg))
    for i in range(0,(len(msg))):
        print(i)
        en_msg.append(msg[i]) # A loop to add the message letter by letter to the array
    print("test")
    print(en_msg)
    #pkb gives us h=b^l which and we want to compute s=b^lr - use Fast Exponentiation
    s = FastModExo(pkb,r,p) # s should be b^lr
    print("b^l used: {}".format(pkb))
    print("b^rl used: {}".format(s))
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i]) # ord will return the int ASCII representation of each char
    return en_msg

def encrypt_num(x,pkb,r,p):
    """ This function will be used to encrypt a number with someone's Public Key. My team members are passing numbers so I will need a function
    seperate from the one I use to encrypt strings.
    This will function will have a few parameters
        x: a number that will get 
        pkb: Bob's public key which will be used for the encryption. pkb will consist of:
            p: A group chosen by both parties and agreed upon
            b: a primitive root of p
            h: h=b^l(modp) only bob knows l but Alice will use h to encrypt the message with
        r: Alice's private key
    """
    #pkb gives us h=b^l which and we want to compute s=b^lr - use Fast Exponentiation
    s = FastModExo(pkb,r,p) # s should be b^lr
    print("b^l used: {}".format(pkb))
    print("b^rl used: {}".format(s))
    en_num = s * x # This should equal n
    print("The encrypted number is: {}".format(en_num)) 
    return en_num

def decrypt(enc_msg, pka, l, p):
    """This function will be used for decryption. It will have a few input parameters
    enc_msg: An encrypted message that was made using the public key associated with the private key l
    l: the private key associated with the public key used to encrypt the message
    pka: The public key of the person who encryped and sent the message
    p: the group used as the basis for the generator and the modulus"""
    dr_msg = [] #We will use this array to decrypt the message letter by letter
    #pka gives us b^r and we want b^rl for decryption - Fast Exponentiation
    s = FastModExo(pka,l,p) # s should be b^rl
    print("b^r used: {}".format(pka))
    print("b^lr used: {}".format(s))
    #dec = int(enc_msg/s) #In reality change this to a loop to handle this letter by letter
    #print("Decrypted message is: {}".format(dec))
    #return dec
    for i in range (0, len(enc_msg)):
        dr_msg.append(chr(int(enc_msg[i]/s))) #decrypt each char one at a time and add it
    print("From here the message should be {}".format(dr_msg))
    return dr_msg

def decrypt_num(enc_num, pka, l, p):
    """This function will be used for decryption. My team members are passing numbers so I will need a function
    seperate from the one I use to decrypt strings. It will have a few input parameters
    enc_num: An encrypted message that was made using the public key associated with the private key l
    l: the private key associated with the public key used to encrypt the message
    pka: The public key of the person who encryped and sent the message
    p: the group used as the basis for the generator and the modulus"""
    #pka gives us b^r and we want b^rl for decryption - Fast Exponentiation
    s = FastModExo(pka,l,p) # s should be b^rl
    print("b^r used: {}".format(pka))
    print("b^lr used: {}".format(s))
    dec = int(enc_num/s) #In reality change this to a loop to handle this letter by letter
    print("Decrypted message is: {}".format(dec))
    return dec