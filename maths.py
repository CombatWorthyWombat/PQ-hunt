# Created on Tue Mar 27 
# Python 3
# UTF-8
# @author: CWW

from cliFX import c, verbose_print

# turning a decimal/float to an int - rough rounding
'''
def dec_trim(num):
    list_num = str(num).split('.')
    return list_num[0]
'''
# handling for decimals and scientific notation for dec_trim (works only for positive e)
# replaced dec_trim function as has same functionality but more

def suppress_sci(num):
    return ('{:.0f}'.format(num))
    
# algorithm for finding the approximate root of n

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
                verbose_print(f"s{steps + 1}: {suppress_sci(estimate)}")
                steps += 1
                if steps > 4:
                    verbose_print(f"√{suppress_sci(n)} ≈ {suppress_sci(estimate)}")
                    return int(suppress_sci(estimate))
                    break
            else:
                return int(suppress_sci(estimate))
    except:
            return c.ansi98("<ValueError>: cannot root a negative")
        
# square root through exponent 1/2, results in innacuracy using floats

def sqrt_exponent(n):
    try:
        if n > 0:
            x = n ** (1/2)
            return suppress_sci(x)
    except:
        return c.ansi171("<ValueError>: cannot root a negative")
    
# function to return primes in range 2 -> n+1 (sieve of eratosthenes)

def prime_sieve(n):
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
    for i in range(2, int(n ** 2) + 1):
        if n % i == 0:
            verbose_print(f"factors found between √{n} and 0 \n∴ {n} is not prime")
            return False
        
        else:
            verbose_print(f"no factors found between √{n} and 0 \n∴ {n} is prime")
            return True

if __name__ == "__main__":
    # print(sqrt_baby(100))
    # print(sqrt_exponent(1029))
    print(prime_sieve(100000000))
    print(is_prime(967848345623444444444444444443222222423425))
    # print(sqrt_exponent(11111111111111111111111111111111117))


    
