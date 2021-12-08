# Python3 program to find primitive root
# of a given number n
from math import gcd as bltin_gcd
"""1- Euler Totient Function phi = n-1 [Assuming n is prime]
1- Find all prime factors of phi.
2- Calculate all powers to be calculated further 
   using (phi/prime-factors) one by one.
3- Check for all numbered for all powers from i=2 
   to n-1 i.e. (i^ powers) modulo n.
4- If it is 1 then 'i' is not a primitive root of n.
5- If it is never 1 then return i;.


There is no general formula to find a primitive root. Typically, what you do is you pick a number and test. 
Once you find one primitive root, you find all the others.How you test

To test that a is a primitive root of p you need to do the following. First, let s=ϕ(p) where ϕ() is the Euler's totient function. 
If p is prime, then s=p−1. Then you need to determine all the prime factors of s: p1,…,pk. Finally, calculate as/pimodp for all i=1…k, 
and if you find 1 among residuals then it is NOT a primitive root, otherwise it is.
So, basically you need to calculate and check k numbers where k is the number of different prime factors in ϕ(p).

Let us find the lowest primitive root of 761:

s=ϕ(761)=760=2^3×5×19
the powers to test are: 760/2=380, 760/5=152 and 760/19=40 (just 3 instead of testing all of them)
test 2:
2^380≡1mod761 oops
test 3:
3^380≡−1mod761 OK
3^152≡1mod761 oops
test 5 (skip 4 because it is 2^2):
5^380≡1mod761 oops
test 6:
6^380≡−1mod761 OK
6^152≡67mod761 OK
6^40≡−263mod761 hooray!
So, the least primitive root of 761 is 6.

How you pick

Typically, you either pick at random, or starting from 2 and going up (when looking for the least primitive root, for example), 
or in any other sequence depending on your needs. Note that when you choose at random, the more prime factors are there in ϕ(p), 
the less, in general, is the probability of finding one at random. Also, there will be more powers to test.
For example, if you pick a random number to test for being a primitive root of 761, then the probability of finding one is
roughly 12×45×1819 or 38%, and there are 3 powers to test. But if you are looking for primitive roots of, say, 
2311 then the probability of finding one at random is about 20% and there are 5 powers to test.

How you find all the other primitive roots

Once you have found one primitive root, you can easily find all the others. 
Indeed, if a is a primitive root mod p, and p is prime (for simplicity), then a can generate all other remainders 1…(p−1) as 
powers: a1≡a,a2,…,ap−1≡1. And ammodp is another primitive root if and only if m and p−1 are coprime (if gcd(m,p−1)=d 
then (am)(p−1)/d≡(ap−1)m/d≡1modp, so we need d=1). By the way, this is exactly why you have ϕ(p−1) primitive roots when p is prime.

For example, 6^2=36 or 6^15≡686 are not primitive roots of 761 because gcd(2,760)=2>1 and gcd(15,760)=5>1, 
but, for example, 6^3=216 is another primitive root of 761."""
from math import sqrt
 
# Returns True if n is prime
def isPrime( n):
 
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True
 
    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
 
    return True
 
""" Iterative Function to calculate (x^n)%p
    in O(logy) */"""
def power( x, y, p):
 
    res = 1 # Initialize result
 
    x = x % p # Update x if it is more
              # than or equal to p
 
    while (y > 0):
 
        # If y is odd, multiply x with result
        if (y & 1):
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1 # y = y/2
        x = (x * x) % p
 
    return res
 
# Utility function to store prime
# factors of a number
def findPrimefactors(s, n) :
 
    # Print the number of 2s that divide n
    while (n % 2 == 0) :
        s.add(2)
        n = n // 2
 
    # n must be odd at this po. So we can 
    # skip one element (Note i = i +2)
    for i in range(3, int(sqrt(n)), 2):
         
        # While i divides n, print i and divide n
        while (n % i == 0) :
 
            s.add(i)
            n = n // i
         
    # This condition is to handle the case
    # when n is a prime number greater than 2
    if (n > 2) :
        s.add(n)
 
# Function to find smallest primitive
# root of n
def findPrimitive(n) :
    s = set()
 
    # Check if n is prime or not
    if (isPrime(n) == False):
        return -1
 
    # Find value of Euler Totient function
    # of n. Since n is a prime number, the
    # value of Euler Totient function is n-1
    # as there are n-1 relatively prime numbers.
    phi = n - 1
 
    # Find prime factors of phi and store in a set
    findPrimefactors(s, phi)
 
    # Check for every number from 2 to phi
    for r in range(2, phi + 1):
 
        # Iterate through all prime factors of phi.
        # and check if we found a power with value 1
        flag = False
        for it in s:
 
            # Check if r^((phi)/primefactors)
            # mod n is 1 or not
            if (power(r, phi // it, n) == 1):
 
                flag = True
                break
             
        # If there was no power with value 1.
        if (flag == False):
            return r
 
    # If no primitive root found
    return -1

def primRootsNP(modulo):
    """Only 1,2,4 and numbers of the form p^k and 2p^k (where p is an odd prime) have Primitive Roots"""
    required_set = {num for num in range(1, modulo) if bltin_gcd(num, modulo) }
    return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]

def primRoots(theNum):
    """make sure only to use this if the number is Prime. This algorithm also gets pretty slow for large Primes so it is probably best just to use 
    findPrimitive() above which will return the first i.e smallest Primitive root for the Encryption/Decryption. Since any Primitive Root will do just fine for Encrypting/Decryptin
    it makes the most sense from a time perspective just to go with the smallest root"""

    if(isPrime(theNum) == False):
        #This means it is not Prime "We shoud use PRIME"
        return primRootsNP(theNum)
    o = 1
    roots = []
    r = 2
    while r < theNum:
        k = pow(r, o, theNum)
        while (k > 1):
            o = o + 1
            k = (k * r) % theNum
        if o == (theNum - 1):
            roots.append(r)
        o = 1
        r = r + 1
    return roots