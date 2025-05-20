# PQ hunt RSA tool
Roadmap for the PQ_hunt RSA cracking tool

**DISCLAIMER:**

if implemented properly, none of the cracking tools in this tool will break RSA encryption. RSA is used because it works

this tool is designed and intended for home lab and CTF purposes only. do not use this out in the wild

**ROADMAP:**

scope: beginner to intermediate RSA CTF challenges, targeting weak RSA implementations

language: python3

define a CLI interface/UI
	- colour and read-out functions
	- verbose mode
	- time estimation for tasks
	- loading bars/spinners

implement maths module

	- prime number handling
	- modular inverse functions
	- gcd(a, b) function

implement basic RSA parsing tools

	- basic RSA decryption using known public and private keys
	- RSA encryption setup using known public keys
	- n, e, p, q, d, phi, eulers totient conversions for the above

implement other parsing tools

	- text to dec/hex/b64/bin and others
	- dec/hex/b64/bin to text
	- parser for standard format RSA keys
	
implement non-factorization attacks

	- Wieners attack for small d, d*e = 1 (mod φ(n)) - infeasable with e > 65537
	- Hastad's broadcast attack for multiple cts with low public exponenet
	- partial q or p values
	- Coppersmith's attack using CRT - so that if e = 3, all you need is a cube root
	- same N, different e for two RSA cts attack
	- common factor for ct and n
	
implement factorization attacks

	- lookup attacks
 
		- factorDB lookup
		- Rapid7 gcd prime dataset
		- wolfram alpha
		- past CTF primes
  
	- mathmatical attacks
 
		- small n factorisation
		- searching p/q values smaller than 100,000
		- assume p and q are close, and factorise based on root need
		- Pollards p-1 - for non cryptographicall safe primes
		- Pollards rho - upper limit of O(n^1/4)
		- Mersenne prime search and gcd
		- fermat numbers search and gcd 2^(2^n) + 1
		- quadratic sieve
