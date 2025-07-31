# created on Thu Jul 17 03:23:09 2025
# python 3
# utf-8
# @author: CombatWorthyWombat

# RSA maths functions for use in PQ hunt

from maths import modinv
from prime_maths import gen_prime
   
# function list:
    # RSA_gen
    # encrypt
    # decrypt

# function to genenerate a set of public and private RSA keys of given bitsize
# private key pair = n, d
# public key pair = n, e

def RSA_gen(bits, e=65537):
    
    p = gen_prime(bits//2)
    q = gen_prime(bits//2)
    n = p * q
    tot = (p - 1)*(q - 1)
    d = modinv(e, tot)   
    return p, q, n, e, d, tot

# function to decrypt a ciphertext using private RSA key values
    
def encrypt(n, e, m):
    ct = pow(m, e, n)
    return ct

# function to encrypt a ciphertext using public RSA key values

def decrypt(n, d, ct):
    m = pow(ct, d, n)
    return m
