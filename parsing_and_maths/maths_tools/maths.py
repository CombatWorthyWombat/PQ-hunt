# Created on Tue Mar 27 
# Python 3
# UTF-8
# @author: CWW

# base_maths.py for PQ_hunt tool - contains common maths functions

from cliFX import c, verbose_print

# function list:
    # sqrt_baby
    # sqrt_exp
    # gcd
    # egcd
    # modinv
    
# function for finding the approximate root of n

def sqrt_baby(n):
    
    if type(n) != type(1):
        return c.ansi171("<TypeError>: cannot root a non int")
    if n <= 0:
        return c.ansi171("<TypeError>: cannot root a negative")
    
    # n = number to square root
    # starting guess set to half the digit length of n
    
    trim = len(str(n))/2
    guess = n/(10 ** trim)
    e = 0
    steps = 0
    mean = (guess + n/guess)/2
    verbose_print(f"√{n}:")
    try:
        if n > 0:
            while abs(mean ** 2 - n) > e:
                estimate = n/mean
                mean = (mean + estimate)/2
                verbose_print(f"step{steps + 1}: {int(estimate)}")
                steps += 1
                if steps > 4:
                    verbose_print(f"√{n} ≈ {int(estimate)}")
                    return int(estimate)
                    break
            else:
                return int(estimate)
    except:
            return c.ansi171("<ValueError>: check value type")
        
# function to return square root through ^ 1/2, results in innacuracy using floats

def sqrt_exp(n):
    
    try:
        if n > 0:
            x = n ** (1/2)
            return x
    except:
        return c.ansi171("<ValueError>: cannot root a negative")

# function to return the greatest common divisor of a and b

def gcd(a, b):
    
    while b != 0:
        a, b = b, a % b
    return a

# function to compute the coefficients of Bézout’s identity
# returns returns integers g, x and y such that ax + by = gcd(a, b) = g

def egcd(a, b):

    x, y, x1, y1 = 1, 0, 0, 1
    a1, b1 = a, b
    
    while b1 != 0:
        q = a1 // b1
        x, x1 = x1, x - q * x1
        y, y1 = y1, y - q * y1
        a1, b1 = b1, a1 - q * b1
        
    return a1, x, y

# function to return the modular inverse
# find an x, such that ax ≅ 1 mod(b)
    
def modinv(a, b):
    
    g, x, y = egcd(a, b)
    
    if g == 1:
        return x % b
    else:
        print(c.ansi171("<ValueError>: gcd(a,b) != 1, ∴ no multiplicitive inverse exists"))

if __name__ == "__main__":

    print(sqrt_baby(103574365843567867867867867867867867867813451345172435423000004))
    #print(sqrt_exp(1029))
    #print(prime_sieve(100))
    #print(is_prime(967848345623444444444444444443222222423425))
    #print(sqrt_exp(11111111111111111111111111111111117))
    #print(gcd(1221,1234567891011121314151617181920212223242526272829))
    #print(egcd(1221,1234567891011121314151617181920212223242526272829))
    #print(modinv(3,11))
