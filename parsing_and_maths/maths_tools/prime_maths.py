# created on Tue Jul 22 17:47:59 2025
# python 3
# utf-8
# @author: CombatWorthyWombat

# prime_maths.py for PQ_hunt tool

import secrets
from maths import sqrt_baby
from cliFX import c

# function list
    # is_prime
    # prime_sieve
    # miller_rabin_round
    # miller_rabin
    # gen_prime

# Digital Signature Standard number of miller rabin rounds for RSA of different bitsize
# https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf#page=81

required_rounds = {1024 : 28,
                   1536 : 33,
                   2048 : 38,
                   3072 : 41,
                   4096 : 44,
                   6144 : 47,
                   8192 : 50}

# primes below 100:
    
low_primes = [2, 3, 5, 7, 11, 13, 17,
              19, 23, 29, 31, 37, 41,
              43, 47, 53, 59, 61, 67,
              71, 73, 79, 83, 89, 97]

# function to return boolean for prime number identity
# use for small numbers < 100,000

def is_prime(n):
    
    if n <= 1:
        return False
    
    if n == 2 or n == 3:
        return True

    for i in range(2, sqrt_baby(n) + 1):
        if n % i == 0:
            return False

    return True

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
    primes[0] = False # remove 0
    primes[1] = False # remove 1
    
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, (n + 1), p):
                primes[i] = False
        p += 1
    sieved = [i for i, x in enumerate(primes) if x]
    return sieved

# function to perform one miller test
# check that fermat exponents are == 1 mod (n - 1) and therefore likley prime

def miller_rabin_round(n, a):
    
    exp = n - 1
    
    while exp % 2 == 1:
        exp >>= 1 # floor division by bitshift
        
    if pow(a, exp, n) == 1:
        return True
    
    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True
        
        exp <<= 1 # multiply by bitshift
        
    return False

# function to perform k miller rabin primality rounds

def miller_rabin(n, k):
    
    for i in range (0, k):
        
        a = secrets.randbelow(n - 3) + 2 # conversion for random.
        if not miller_rabin_round(n, a):
            
            return False
        
    return True

# function to generate primes of a certain bitlength

def gen_prime(bits):
    
    found = False
    
    k = required_rounds.get(bits, 40)
        
    while not found:
        candidate = secrets.randbelow(1 << bits - 1) | (1 << (bits - 1)) | 1 # ensures candidate is odd
        if miller_rabin(candidate, k):
            return candidate
