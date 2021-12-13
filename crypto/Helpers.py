#from math import *
import math
#from crypto.Exponentiation import isPrime
from crypto.Euclidean import GCD
from crypto.PseudoRandoms import isPrimeMR

"""This module will provide helper functions to the rest of  b"""

def Order(n):
    """Given  a number P. This algorithm will find the order of p. That is the multiplicative order of the group based on Euler's 
    function i.e the order (size of Zp) is ther the number of integers from 1->p that are reletivly prime to P. 
    If P is prime then psi(p) = p-1. """
    z = []

    if (isPrimeMR(n)):
        "Well we know this is Prime. So via FLT we know phi(p) = p-1 so return that as the order of the group"
        size = n-1
        return size

    """Now we need to check if a given number x is a divisor of n. I.E we need to check if they are reletivly prime
    if the GCD(n,x)= 1 then they are relatively prime and they belong in Zp """
    for i in range(n):
        "if the GCD(n,i) = 1 then then it belong to the group." 
        if (GCD(n,i) == 1):
            z.append(i)
    print(z) #This should be a list of all the elements in Z
    return len(z)

def primeRoots(modulo):
    """This function will return a list of the Prime Roots of N if they exist"""
    roots = []
    print("Mod in function:")
    print(modulo)
    required_set = set(num for num in range (1, modulo) if GCD(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)           
    return roots

def bsgs(g, h, p):
    '''
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    N = math.ceil(math.sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(g, i, p): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return -1

