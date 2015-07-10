# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 13:58:14 2015

@author: Daniele Padula
"""
#set of common functions to deal with Project Euler problems.

from itertools import permutations
from math import sqrt

def trial_division(n, bound=None):
    if n == 1: return 1
    for p in [2, 3, 5]:
        if n%p == 0: return p
    if bound == None: bound = n
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7; i = 1
    while m <= bound and m*m <= n:
        if n%m == 0:
            return m
        m += dif[i%8]
        i += 1
    
    return n
    
def fact(n):
    '''Return the factorial of n.'''
    if n < 1:
        return 1
    else:
        return n * fact(n - 1)
    
def is_prime(n):
    '''Returns True if n is prime.'''
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    
    return True
    
def sieve_erat(n):
    '''Returns a list containing the primes lower than n.'''
    primes = [2]
    sieve = [True] * (n + 1)
    for p in range(3, n + 1)[::2]:
        if sieve[p]:
           primes.append(p)
           for i in range(p * p, n + 1, p):
               sieve[i] = False
    
    return primes

def nth_prime(n):
    '''Returns the nth prime.'''    
    return sieve_erat[n - 1]
      
def sum_primes(n):
    '''Returns the sum of the primes up to n included.'''
    return sum(sieve_erat(n))
    
def p_sum(n):
    '''Returns a list of the sums of the primes up to n included.'''
    prime_list = sieve_erat(n)    
    p_s = [0]
    s = 0
    for p in prime_list:
        s += p
        p_s.append(s)

    return p_s

def factorize(n):
    '''Returns a list of tuples containing the prime factors of n and their
    exponents.
    
    Example:
    >>> factor(786456)
    [(2,3), (3,3), (11,1), (331,1)]'''
    
    if n in [-1, 0, 1]: return []
    if n < 0: n = -n
    F = []
    while n > 1:
        p = trial_division(n)
        e = 1
        n /= p
        while n % p == 0:
            e += 1; n /= p
        F.append((p, e))
    
    return sorted(F)
    
def truncatable_r(n):
    '''Returns True is a prime is right-truncatable.'''
    truncated = [n]
    for i in range(len(str(n))):
        truncated_r = str(n)[:-i]
        if truncated_r not in truncated:
            truncated.append(truncated_r)
    trunc = sorted(map(int, filter(None, truncated)))
    
    return all(map(is_prime, trunc))
    
def truncatable_l(n):
    '''Returns True is a prime is left-truncatable.'''    
    truncated = [n]
    for i in range(len(str(n))):
        truncated_l = str(n)[i:]
        if truncated_l not in truncated:
            truncated.append(truncated_l)
    trunc = sorted(map(int, filter(None, truncated)))
    
    return all(map(is_prime, trunc))
    
def truncatable(n):
    '''Returns True is a prime is both right- and left- truncatable.'''
    return all((truncatable_r(n), truncatable_l(n)))

def n_divs(n):
    '''Returns the number of divisors of n.'''
    prime_factors = factorize(n)
    num_divs = 1    
    for factor in prime_factors:
        num_divs *= (factor[1] + 1)
    
    return num_divs

def divs(n):
    '''Returns a list containing the divisors of n.'''
#prime_factors = [(prime1, i), (prime2, j), ..., (primeN, k)]
#
#divisors = [prime1 ^ 0 * prime2 ^ 0 * ... primeN ^ 0,
#           prime1 ^ 0 * prime2 ^ 0 * ... primeN ^ 1,
#            ...          ...        ...   ...     
#           prime2 ^ i * prime2 ^ j * ... primeN ^ k]
    n_prime_facts = factorize(n)
    divs = [1]
    for p, exp in n_prime_facts:
        divs = [d * p**e for d in divs for e in range(exp + 1)]
        
    return sorted(divs)

def is_palindromic(n):
    '''Returns True if n is palindromic.'''    
    return str(n) == str(n)[::-1]

def is_pandigital(n, s=9, zero=False):
    '''Returns True if n is pandigital in s digits.'''
    n = str(n)
    if zero == False:
        return len(n) == s and not '123456789'[:s].strip(n)
    if zero == True:
        return len(n) == s and not '0123456789'[:s].strip(n)
    
def pandigitals(n, zero=False):
    '''Returns a list containing all the n-digit pandigital numbers.'''      
    pans = []    
    
    if zero == False:
        digits = range(1, n + 1)
        l = n
    if zero == True:
        digits = range(n + 1)
        l = n + 1

    str_digits = ''.join([str(d) for d in digits])
    for pan in permutations(str_digits):      
        if pan[0] != '0' and len(pan) == l:
            pan_int = int(''.join(pan))
            if is_pandigital(pan_int, l) and pan_int not in pans:
                pans.append(pan_int)
    
    return sorted(pans)
    
def is_perm(a, b):
    '''Returns True if a, b are permutations of each other.'''
    return sorted(str(a)) == sorted(str(b))
    
def lycherel(n):
    '''Returns True is n is a Lycherel number.'''
    l = 50  #iteration limit
    i = 0   #iteration count
    while i < l:
        rev_n = int(str(n)[::-1])
        sum_l = n + rev_n
        if is_palindromic(sum_l):
            return False
            break
        else:
            n = sum_l
            i += 1
    
    return True
    
def digit_sum(n):
    '''Returns the sum of the digits of n.'''
    return sum(map(int, list(str(n)))) 

def triplet(lim_n=0, lim_p=1):
    '''Returns a list of Pythagorean triplets as a list of tuples.'''
    triplets = []    
    for n in range(lim_n + 1):
        for p in range(1, lim_p + 1):
            a = 3*p**2 + 2*n*p
            b = 2*(n + p)*(n + 2*p)
            c = 2*(n + p)*(n + 2*p) + p**2
            assert (a**2 + b**2 == c**2)
            triplets.append((a, b, c))
    
    return triplets
    
def period(n):
    '''Returns the continued fraction expansion of sqrt(n).'''
    if sqrt(n).is_integer():
        return sqrt(n)
    period = []
    a0 = int(sqrt(n))
    period.append(a0)
    a = a0
    p = 0
    d = 1
    m = 0
    while a != 2*a0:
        m = d*a - m
        d = (n - m*m)//d
        a = (a0 + m)//d
        p += 1
        period.append(a)
        
    return period

def triangle(n):
    '''Returns the nth Triangle number.'''
    return n * (n + 1) / 2

def triangle_list(n):
    '''Returns a list containing the Triangle numbers up to the nth.'''
    t = []
    for i in range(1, n + 1):
        t_i = i*(i + 1)/2
        t.append(t_i)
        
    return t

def is_triangle(n):
    '''Returns True if n is a Triangle number.'''
    return (-1 + sqrt(1 + 8*n)) % 2 == 0
    
def penta(n):
    '''Returns the nth Pentagonal number.'''
    return n * (3*n - 1) / 2
    
def penta_list(n):
    '''Returns a list of Pentagonal numbers up to the nth.'''
    p = []
    for i in range(1, n + 1):    
        p_i = i * (3*i - 1) / 2
        p.append(p_i)
    
    return p
    
def is_penta(n):
    '''Returns True if n is a Pentagonal number.'''
    return (1 + sqrt(1 + 24*n)) % 6 == 0
    
def hexa(n):
    '''Returns the nth Hexagonal number.'''
    return n * (2*n - 1)
    
def hexa_list(n):
    '''Returns a list of Hexagonal numbers up to the nth.'''
    h = []
    for i in range(1, n + 1):    
        h_i = i * (2*i - 1)
        h.append(h_i)
    
    return h
    
def is_hexa(n):
    '''Returns True if n is a Hexagonal number.'''
    return (1 + sqrt(1 + 8*n)) % 4 == 0
    
def hepta(n):
    '''Returns the nth Heptagonal number.'''
    return n * (5*n - 3) / 2
    
def hepta_list(n):
    '''Returns a list of Heptagonal numbers up to the nth.'''
    h = []
    for i in range(1, n + 1):    
        h_i = i * (5*i - 3) / 2
        h.append(h_i)
    
    return h
    
def is_hepta(n):
    '''Returns True if n is a Heptagonal number.'''
    return (3 + sqrt(9 + 40*n)) % 10 == 0
    
def octa(n):
    '''Returns the nth Octagonal number.'''
    return n * (3*n - 2)
    
def octa_list(n):
    '''Returns a list of Octagonal numbers up to the nth.'''
    h = []
    for i in range(1, n + 1):    
        h_i = i * (3*i - 2)
        h.append(h_i)
    
    return h
    
def is_octa(n):
    '''Returns True if n is an Octagonal number.'''
    return (4 + sqrt(4 + 12*n)) % 6 == 0
