# -*- coding: utf-8 -*-                                                                                                 
"""
Created on Thu Jul 16 10:22:34 2015                                                                                     
@author: Daniele                                                                                                        
"""                                                                                                                     

#Using all of the digits 1 through 9 and concatenating them freely to form
#decimal integers, different sets can be formed. Interestingly with the set
#{2,5,47,89,631}, all of the elements belonging to it are prime.
#How many distinct sets containing each of the digits one through nine exactly
#once contain only prime elements?

# Two possible approaches:
# generate all primes up to 1000000000 and generate sets from them
# generate all permutations of the digits 1...9, partition each permutation in
# all possible ways, check that each number in the partition is prime

# The second approach needs 9! permutations to be partitioned in 256 ways each
# for a total of 9! * 256 = 92897280 combinations, many of which equivalent.
# I will run controls while the permutation is being partitioned, so that if
# a number is not prime, the partition will be discarded.
# I can add one more control to improve the speed, that is checking that one
# number in the partition is higher than the previous.

import time
import itertools
from Euler import *

def partition(s, result=None):
    if not result:
        result = []
    if is_prime(int(s)):
        result.append([s])
    for i in range(1, len(s)):
        first = [s[:i]]
        if is_prime(int(first[0])):
            rest = s[i:]
            for p in partition(rest):
                result.append(first + p)
    return result

start = time.time()

found = []

#runs in approximately 100 seconds...to be improved
for perm in itertools.permutations('123456789'):
    num_str = ''.join(perm)
    sets_perm = [sorted(map(int, p)) for p in partition(num_str)]
    for set_perm in sets_perm:
        if set_perm not in found:
            found.append(set_perm)

elapsed = (time.time() - start)                                                                                         
print len(found), 'in %5.3f seconds' % elapsed 
