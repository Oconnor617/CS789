from math import *

"""
CS789 Cryptograpy
Thomas O'Connor
This Module will contian functions for the Euclidean Algorithm and the Extended Euclidean Algorithm. 
"""

def GCD(m,n):
    """Given two large numbers this algorithim will recursivly find the Greatest Common Divisor
    this is the Eclidean Algorithm. It is based on the fact that GDC(m,n) = GCD(n,m%n) essentially
    saying that the GDC of two numbers is NOT changes if the larger number is replaced by its differnce with the smaller number
    It will also print out the steps it took along the way in the form m=qn+r for visual purposes
    Issues: right now if n>=m we will do one extra step at the start"""
    if n == 0: #base case
        return m
    r = int (m%n) #going to replace m as the new number
    q = floor(m/n) #q is the number of time n divides m evenly and r above is the remainder
    print("{} = {} * {} + {}" .format(m,q,n,r))
    print()
    return GCD(n,r) # Recursive step with n as the new m and r as the new n

def ExtendedGDC(m,n):
    """This is the Extended Euclidean Algorithm. It will take two integers m,n and find two integers x,y such that
    the equation x*m + y*n yeilds the smallest possible positive integer that is equal to the gcd(m,n) i.e
    x*m + y*n = gdc(m,n)."""
    if m == 0: #basecase
        print("Base: n={} x={} y={}".format(n,0,1)) #You are going to get to the base case and use it on the way back up to build the final x,y
        return n, 0, 1 #return a touple
    else:
        gcd,x1,y1 = ExtendedGDC(n % m,m) #Recursive Step - Result should be a sum of all the previous x,y
        print("x1={} y1={}".format(x1,y1))
        #update the x,y with the results of the recursion abouve
        x = y1 - (n // m) * x1
        y = x1
        print("Final x={}, y={}".format(x,y))
        return gcd,x,y
        #return gcd, y1 -(n // m) *x1,x1

def power(x,y,m):
    """Essentially this is an iterative function to find the modular inverse of a number. This one will only be used if we have already
    verified that the two numbers a and m are coPrime i.e GCD(a,m) = 1. That means that a multiplicative inverse exists under m and this function
    will return it. THis will compute x^y under modulo m """
    if (y==0):
        return 1
    p = power(x,y//2,m) % m
    p = (p * p) % m
    if (y % 2 == 0):
        return p
    else:
        return ((x*p)%m)

"""
print("starting a few trials now")
GCD(1000,10)
print("The GDC is: {}".format(GCD(1000,10)))
GCD(150,9)
print()
GCD(31,2)
print("Another. GDC is: {}" .format(GCD(150,304)))
print("Let's see what's happening with extended")
#print("The values are {} = {} * m35 * + {} * n15".format(ExtendedGDC(35,15)))
print(ExtendedGDC(30,50))
gcd, x, y = ExtendedGDC(30, 50)
print("The GCD is", gcd)
print(f"x = {x}, y = {y}")
"""