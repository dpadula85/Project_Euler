# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:16:49 2015

@author: Daniele
"""

# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?

# Prime Factorize any number
def factor(x):
    factors = []
    i = 2
    while x > 1:
        if x % i == 0:
            x = x / i
            factors.append(i)
        else:
            i += 1
    return factors

# Write list of prime factors as factor**exp
def condense(L):
  prime,count,list=0,0,[]
  for x in L:
    if x == prime:
      count = count + 1
    else:
      if prime != 0:
        list = list + [str(prime) + '**' + str(count)]
      prime,count=x,1
  facs = list + [str(prime) + '**' + str(count)]
  return facs
    
# get prime factors of the numbers from 2 to 20 in a dictionary
prime_factors = {}    
for i in range(2, 21):
    a = factor(i)
    prime_factors[i] = condense(a)

# get common prime factors with highest exponent and uncommon prime factors
mcm_dict = {}
for list_factors in prime_factors.itervalues():
    for factor in list_factors:
        fact = int(factor.split('**')[0])
        exp = int(factor.split('**')[1])
        if not mcm_dict.has_key(fact):
            mcm_dict[fact] = exp
        elif mcm_dict.has_key(fact) and exp > mcm_dict[fact]:
            mcm_dict[fact] = exp

# calculate mcm multiplying the elements of the mcm_dict
mcm = 1
for f in mcm_dict.keys():
    mcm = mcm * f**mcm_dict[f]
    
print mcm
    