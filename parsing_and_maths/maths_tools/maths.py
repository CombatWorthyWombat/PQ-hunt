# Created on Tue Mar 27 
# Python 3
# UTF-8
# @author: CWW

from cliFX import c, verbose_print

# function list:
    # suppress_sci
    # sqrt_baby
    # sqrt_exponent
    # prime_sieve
    # is_prime
    # gcd
    # egcd
    # modinv
    # modexp

# function for removing decimals and scientific notation

def suppress_sci(n):
    
    return ('{:.0f}'.format(n))
    
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
    verbose_print(f"√{suppress_sci(n)}:")
    try:
        if n > 0:
            while abs(mean ** 2 - n) > e:
                estimate = n/mean
                mean = (mean + estimate)/2
                verbose_print(f"step{steps + 1}: {suppress_sci(estimate)}")
                steps += 1
                if steps > 4:
                    verbose_print(f"√{suppress_sci(n)} ≈ {suppress_sci(estimate)}")
                    return int(suppress_sci(estimate))
                    break
            else:
                return int(suppress_sci(estimate))
    except:
            return c.ansi98("<ValueError>: cannot root a negative")
        
# function to find the square root of n through exponent 1/2, results in innacuracy using floats

def sqrt_exponent(n):
    
    try:
        if n > 0:
            x = n ** (1/2)
            return suppress_sci(x)
    except:
        return c.ansi171("<ValueError>: cannot root a negative")
    
# function to return primes in range 2 -> n+1 (sieve of eratosthenes)

def prime_sieve(n):
    
    if n > 10000000:
        return c.ansi171("<ComputeError>: please use numbers less than 10,000,000")
    if type(n) == type(1):
        pass
    else:
        return c.ansi171("<TypeError>: cannot find primes below non int")
    if n > 0:
        pass
    else:   
        return c.ansi171("<TypeError>: cannot find primes below zero")
    primes = [True] * (n + 1)
    primes[0] = False # remove 0 from prime list
    primes[1] = False # remove 1 from prime list
    
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, (n + 1), p):
                primes[i] = False
        p += 1
    sieved = [i for i, x in enumerate(primes) if x]
    return sieved

# function to return boolean for prime number identity

def is_prime(n):
    
    if n <= 1:
        return False
    
    if n == 2 or n == 3:
        return True

    for i in range(2, sqrt_baby(n) + 1):
        if n % i == 0:
            verbose_print(f"Factors found: {i} and {n//i} \n∴ {n} is not prime")
            return False

    verbose_print(f"No factors found between 2 and √{n} \n∴ {n} is prime")
    return True

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
    
# function to calculate a^x mod(c) in e steps

def modexp(b, e, m):
    
    if m == 1:
        return 0
    
    result = 1
    counter = 0
    while counter < e:
        result = (result * b) % m
        counter = counter + 1
        
    return result
    
    
    
    
if __name__ == "__main__":
    a = 1
    #print(sqrt_baby(100))
    #print(sqrt_exponent(1029))
    #print(prime_sieve(100))
    #print(is_prime(967848345623444444444444444443222222423425))
    #print(sqrt_exponent(11111111111111111111111111111111117))
    #print(gcd(1221,1234567891011121314151617181920212223242526272829))
    #print(egcd(1221,1234567891011121314151617181920212223242526272829))
    #print(modinv(3,11))
    #print(modexp(4,3,128))
