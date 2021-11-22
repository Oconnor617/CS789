from crypto.Euclidean import GCD, power
"""This  is an implementation of the ElGamal Cipher Algorithm.
    For the Encryption side of the Algorithm, the user will provide a message to encrypt. This script will then generate a large 
    random number N (to be used as the modulus). It will then make a list of the elements of the multiplicative group of N. 
    From that list it will find all of the primitive roots of N. From there it will choose one primitive root, b, which will 
    serve as the basis of the keys and be used to encrypt the message"""
