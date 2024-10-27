#!/bin/python3

# Python program to find and print all of the positive primes smaller 
# than or equal to n using the Sieve of Eratosthenes.


import sys
import math

SEARCH_SPACE = 10000


# Brute-force check if a number if prime
def is_prime(number: int) -> bool:
    prime = True
    for x in range(2, number):
        if number % x == 0: 
            prime = False
            break
    return prime

def main():
    
    # Generate a list of prime candidates
    primes = list(range(0, SEARCH_SPACE + 1))
    
    # Edge cases: 0 and 1 are not primes
    primes[0] = 'x'
    primes[1] = 'x'

    for i in range(SEARCH_SPACE):
        if primes[i] == 'x':
            continue
    
        # Cross off any multiples of the current prime
        for k in range(2, math.floor(SEARCH_SPACE / i) + 1):
            primes[i * k] = 'x'

    # Output
    final_prime_list = list(filter(lambda z: z != 'x', primes))
    print(final_prime_list)
    print(f"Primes found between 2 and {SEARCH_SPACE}: {len(final_prime_list)}")

if __name__ == "__main__":
    sys.exit(main())


