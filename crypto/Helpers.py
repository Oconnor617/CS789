#from math import *
import math
from crypto.Exponentiation import isPrime

"""This module will provide helper functions to the rest of  b"""
def GCDNP(m,n):
    """Given two large numbers this algorithim will recursivly find the Greatest Common Divisor
    this is the Eclidean Algorithm. It is based on the fact that GDC(m,n) = GCD(n,m%n) essentially
    saying that the GDC of two numbers is NOT changes if the larger number is replaced by its differnce with the smaller number
    It will also print out the steps it took along the way in the form m=qn+r for visual purposes
    Issues: right now if n>=m we will do one extra step at the start"""
    if n == 0: #base case
        return m
    r = int (m%n) #going to replace m as the new number
    q = floor(m/n) #q is the number of time n divides m evenly and r above is the remainder
    return GCDNP(n,r) # Recursive step with n as the new m and r as the new n

def Order(n):
    """Given  a number P. This algorithm will find the order of p. That is the multiplicative order of the group based on Euler's 
    function i.e the order (size of Zp) is ther the number of integers from 1->p that are reletivly prime to P. 
    If P is prime then psi(p) = p-1. """
    z = []

    if (isPrime(n) == 0):
        "Well we know this is Prime. So via FLT we know phi(p) = p-1 so return that as the order of the group"
        size = n-1
        return size

    """Now we need to check if a given number x is a divisor of n. I.E we need to check if they are reletivly prime
    if the GCD(n,x)= 1 then they are relatively prime and they belong in Zp """
    for i in range(n):
        "if the GCD(n,i) = 1 then then it belong to the group." 
        if (GCDNP(n,i) == 1):
            z.append(i)
    print(z) #This should be a list of all the elements in Z
    return len(z)

def gcdP(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primeRoots(modulo):
    """This function will return a list of the Prime Roots of N if they exist"""
    roots = []
    print("Mod in function:")
    print(modulo)
    required_set = set(num for num in range (1, modulo) if gcdP(num, modulo) == 1)

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
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

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
    return None

def babyStep(g,h,p):
    """Example: 22=5^x(mod53) so here
    g=5
    h=22
    p=53
    
    or log2(3) in Z101 -> g=2, h=3, p=101"""
    N = int(math.ceil(math.sqrt(p-1)))
    print("N=")
    print(N)
    t={}

    #babyStep
    for i in range(N):
        t[pow(g,i,p)]=i
    print("Baby Step: ")
    print(t)

    #Fermat's Little Theorem
    c = pow(g, N*(p-2),p)

    for j in range(N):
        y = (h * pow(c,j,p))%p
        if y in t:
            return j * N + t[y]
    
    return None # I found nothing

