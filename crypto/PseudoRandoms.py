import random
"""THis module wll contain code for generating Pseudo Random Numbers and implement a Miller-Rabin Primality Test algorithm
to test the primality of those numbers. The random prime numbers generated can then be used for the El Gamal Encryption and
The RSA Encryption. This will also provide an update to my isPrime() function which will now use the Miller-Rabin algorthm to test
the pimiality of larger numbers efficiently."""

def isPrimeMR(n):
    """This is an inprovement on my old isPrime() funciton. That one took and iterative approch checking every number
    up to sqrt(n) checking for divisors. That was O[sqrt(n)] but this one should be faster. This function will first perform a quick
    straight forward check on a small subset of Primes to check if n is composit before moving onto the Miller-Rabin test. This returns True
    if n is has a Strong likelyhood of being Prime"""
    if (n < 2):
        return False # Obviously anything less than 2 is not prime
    # Now do a quick check to see if we can skip miller_rabin() all toghether. 
    # Sometimes you can quickly determine if num is not prime by dividing by the first few dozen prime numbers. 
    # This is quicker than miller_rabin() but cannot prove primality for sure
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 
    109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 
    251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 
    401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 
    569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 
    727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 
    887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997] #all Primes under 1000

    if n in lowPrimes: #looks like n is a prime under 1000
        return True
    #check if n is composite made up of some of the low primes
    for p in lowPrimes:
        if (n%p == 0): #p is a divisor of n
            return False
    #Now we gotta call miller_rabin() to be sure wether n is Prime or not
    return miller_rabin(n)

def miller_rabin(n):
    """This is my implementation of the Miller Rabin test for Pimality of N. Here is a breakdown of how the Algorithm works:
    Pre Conditions) Let n be odd before starting the proper algorithm. Write n-1 = 2^r * m where m is odd. n passes the test if 
            a) b^m(modn) = 1
            b) 0<=k<r where (b^m)^(2^k)(modn) = -1
    So the Algorithm is:
    1) if b^m(modn) = 1 -> halt. n is Prime
    2) if b^m(modn) = -1 -> halt. n is Prime
    3) if b^m(modn) != -1 -> check:
        3a) if (b^m)^2 = -1 -> halt. n is Prime
            else: if (b^m)^(2^2) = -1 -> halt. n is Prime
            ...
            else: if if (b^m)^(2^(r-1)) = -1 -> halt. n is Prime
        Here n must be a composite number return False. [i.e we check all the way up to [(b^m)^(2^(r-1)) = -1]
    Note for k runs of the MillerRabin test it has a Probability of 1-(1/4)^k of failing so if we run the trial k=8 times then then
    there is a 0.99998 chance that MillerRabin has correctly identified n as Prime. That is good enough for the purposes of this class 
    """
    if n % 2 == 0: # Obviously it can't be even
        return False

    if n == 2 or n == 3:
        return True # isPrimeMR() should have caught this but just incase
    
    r,s = 0, n-1 # s=2^r * m in the Pre-Conditions above. Easiest is m is 1
    while (s % 2 == 0): #divide s by 2 while it is even. r tracks howmany times we do it
        r +=1 #keep track of r so we know what form s=2^r * m is in
        s = s // 2 # maybe s is odd now
    
    #Now we can start the Algorithm
    for runs in range(8): #Going to run this upto 8 times giving us a 99.998% probabilyu of true Prime
        b = random.randrange(2, n-1)
        x = pow(b,s,n) #Fast Modular Exponetiation
        if x == 1 or x == n-1:
            return True #part 1) or 2) above
            #continue
        if x !=1: #this part of the test does now not apply if x congruent to 1
            i = 0
            while x != (n-1):
                if i == r-1:
                    return False # we have reached the end
                else:
                    i = i + 1
                    x = (x ** 2) % n # square x again and try (b^m)^2, then (b^m)^(2^2) ... (b^m)^(2^(r-1))
        """for more in range(r-1):# now do 3) and keep checking up to r-1
            x = pow(x,2,n) #(b^m)^2, then (b^m)^(2^2) ... (b^m)^(2^(r-1))
            if x == n-1:
                break
        else:
            return False"""
    return True #it "passed" all 8 runs so it must be Prime

def gen_random_prime(size=1000):
    """This should genreate and return a random Prime number. It basis for deteriming Primality is the MillerRabin test"""
    while True: # an Infinite Loop!
        rand = random.randrange(size)
        if isPrimeMR(rand):
            return rand
