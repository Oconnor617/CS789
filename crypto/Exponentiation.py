"""
CS789 Cryptograpy
Thomas O'Connor
This Module will contian functions for the Fast Exponentiation Algorithm. 
"""
import math

def FastModExo(x,e,m):
    """This Algorithm will take three numbers: x,e,m and return x^e(mod m). It will do this via
    the Fast Exponentiation Algorithm and print out the intermidiate steps along the way. The key steps along the way are
    X - Base
    E - Shifted Exponent
    Y - Accumulated Intermediate Result
    At each step: 
        e is Even -  x <--(x^2)%m ; e <--(e/2) [note maybe try a bitwise shift for speed] ; y <--y
        e is Odd - x <--x ; y <-- (x*y)%m ; e <-- (e-1)
        """
    X = x  #For the first step the working Base is the orginal
    E = e  #Start with the orginal Exponent
    Y = 1  #From definition of the Algorithm
    print(m)
    print("x   e     y")
    print("{}  {}  {}".format(X,E,Y))
    while E>0: #The Algorithm stops when the exponent is 0
        #Now check for E's parity
        if E % 2 == 0: #Even E
            X = (X*X)%m
            E = E/2
            print("{}  {}  {}".format(X,E,Y))
        else: #Odd E
            Y = (X*Y)%m
            E = E-1
            print("{}  {}  {}".format(X,E,Y))
    return Y # At the End when E=0 the resultant Y is our anwser

def primeFactor(n):
    """A function that will take an integer number as input and print out the Prime Factorization of that
        number. The basic steps of the Algorithm are: 
            1) If n is divisible by 2, print 2 and set n = n/2
            2) Eventually n will be odd. Now loop from i=3 to sqrt(n)
                if i is a divisor of n: print i and set n = n/i
                if i is not a divisor of n: set i = i + 2 and repeat 2)
            3) if n is prime && n>2 it will not become 1 via 1) & 2) so print n. 
    """
    # Start with the lowest Prime. Print the number of time 2 divides n
    while (n%2 == 0):
        print (2)
        n = n/2
    # once the while loop is over n must now be odd
    # we also know 2 is no longer a divisor so we want to do a loop that skips 2
    # easiest way is to start with 3 i.e (i=i+2=3)
    for i in range(3,int(math.sqrt(n))+1,2): #make the sqrt an integer
        #now start step 2)
        while (n%i == 0): #is i a divisor of n?
            print(i)
            n = n/i
        # if the while loop condition is not met then i = i+2 via the step in the for loop
    # step 3)
    if n>2:
        print(n) # this must be a prime larger than 2

def isPrime(n):
    """Given a number n this function will determin if that number is prime or not
    We do this by starting at i=2 and increasing until sqrt(n) and each time check if
    i is a divisor of n. If it is then we know that n is not prime and we can exit early. 
    We go until sqrt(n) because any larger factor than that must be a multiple of a smaller
    factor that we already checked on our way up to sqrt(n) """
    prime_flag = 0 # use this flag to see if it is prime as we check. If we flip this we can stop beacuse we know its not prime    

    if(n>1):
        for i in range(2,int(math.sqrt(n))+1):
            if (n%i == 0): # i is a divisor of n -> not prime
                prime_flag = 1
                break # we can breakout early
        if (prime_flag == 0):
            print("{} is a prime number".format(n))
        else:
            print("{} is not a prime number".format(n))
            print("{} times {} = {}".format(i,(n//i),n))
    else: # maybe it is a negative number
        print("{} is not a prime number".format(n))
    return prime_flag

"""
print("Let's try it")
print(FastModExo(2,100,71))
print("And again")
print(FastModExo(12039,7915,12091))

print(primeFactor(12248856))
isPrime(11)
isPrime(25)
isPrime(44)
isPrime(-11)
isPrime(12397864568)
"""

