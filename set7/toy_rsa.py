# toy_rsa
# Aritra Biswas
#
# A demo implementation of RSA.

import random
from math import sqrt

def gen_primes(bound):
    '''Generates a list of prime numbers below bound using a sieve.'''

    # status list: composite[i] = 0 means i is composite
    composite = [0] * (bound + 1)

    for i in xrange(2, int(sqrt(bound)) + 1):
        if composite[i] == 0:
            for n in xrange(2, int(bound/i) + 1):
                composite[n * i] = 1

    # primes list
    primes = []
    for i in xrange(2, bound):
        if composite[i] == 0:
            primes.append(i)

    return primes

def gen_keys():
    '''Generates an RSA public and private key pair, returned as
    (public, private) = ((modulus, public_exp), (modulus, private_exp)).'''

    # pick two primes
    four_bit_primes = gen_primes(2**4) # chosen such that n is 8 bits
    while True:
        p = random.choice(four_bit_primes)
        print p
        q = random.choice(four_bit_primes)
        print q
        if (p != q):
            print 'Ready!'
            break

    # calculate the product n, and its totient
    n = p * q
    totn = (p - 1) * (q - 1) # since phi(n) = phi(p) * phi(q), both prime

    # public key exponent must be smaller than and coprime with totn, so
    # pick a prime number so that we only have to check if it divides totn
    possible_e = gen_primes(totn)
    for elem in possible_e:
        if totn % elem == 0:
            possible_e.remove(elem)
    e = random.choice(possible_e)

    # private key exponent is the multiplicative inverse mod totn, i.e.:
    # d*e = 1 (mod totn)
    # d*e = k*totn + 1
    #   d = (k*totn + 1) / e,   for any k that makes d an integer
    k = 0
    # increment k until the quotient (k*totn + 1) / e is an integer
    while (k*totn + 1) % e != 0:
        k += 1
    d = (k*totn + 1) / e

    public_key = (n, e)
    private_key = (n, d)

    return (public_key, private_key)

def encrypt(m, public_key):
    '''Encrypts an integer message m.'''

    (n, e) = public_key
    c = (m**e) % n

    return c

def decrypt(c, private_key):
    '''Decrypts an integer message c.'''

    (n, d) = private_key
    m = (c**d) % n

    return m

def brute_collision_attack(public_key):
    '''Attempts to find two messages that result in the same encrypted
    message given a public key. '''

    hashes = []
    m = 0

    while True:
        new_hash = encrypt(m, public_key)
        if new_hash in hashes:
            return (hashes.index(new_hash), m)
        hashes.append(new_hash)
        m += 1
