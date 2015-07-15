# -*- coding: utf-8 -*-                                                                                                 
"""
Created on Thu Mar 26 14:27:34 2015                                                                                     
@author: Daniele                                                                                                        
"""                                                                                                                     

#Working from left-to-right if no digit is exceeded by the digit to its left it                                         
#is called an increasing number; for example, 134468.                                                                   
#Similarly if no digit is exceeded by the digit to its right it is called a                                             
#decreasing number; for example, 66420.                                                                                 
#We shall call a positive integer that is neither increasing nor decreasing a                                           
#"bouncy" number; for example, 155349.                                                                                  
#Clearly there cannot be any bouncy numbers below one-hundred, but just over                                            
#half of the numbers below one-thousand (525) are bouncy. In fact, the least                                            
#number for which the proportion of bouncy numbers first reaches 50% is 538.                                            
#Surprisingly, bouncy numbers become more and more common and by the time we                                            
#reach 21780 the proportion of bouncy numbers is equal to 90%.                                                          
#Find the least number for which the proportion of bouncy numbers is                                                    
#exactly 99%.                                                                                                           

import time                                                                                                             

def is_incr(n):                                                                                                         
    s = str(n)                                                                                                          
    for i in range(len(s) - 1):                                                                                         
        if s[i] > s[i + 1]:                                                                                             
            return False                                                                                                
            break                                                                                                       

    return True                                                                                                         

def is_decr(n):                                                                                                         
    s = str(n)                                                                                                          
    for i in range(len(s) - 1):                                                                                         
        if s[i] < s[i + 1]:                                                                                             
            return False                                                                                                
            break                                                                                                       

    return True                                                                                                         

def is_bouncy(n):                                                                                                       
    if not is_incr(n) and not is_decr(n):                                                                               
        return True                                                                                                     
    else:                                                                                                               
        return False                                                                                                    

ini = 1                                                                                                                 
bouncy = 0                                                                                                              
ratio = float(bouncy) / ini                                                                                             

start = time.time()                                                                                                     

while ratio < 0.99:                                                                                                     
    ini += 1                                                                                                            
    if is_bouncy(ini):                                                                                                  
        bouncy += 1                                                                                                     

    ratio = float(bouncy) / ini                                                                                         

elapsed = (time.time() - start)                                                                                         
print ini, 'in %5.3f seconds' % elapsed 
