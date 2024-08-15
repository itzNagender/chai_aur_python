x = 2
y = 3
z = 4

print(x+y)

print(40 + 2.23) #output: 40.23
#print('Nagender' + 3)  #give error can only concatenate str to str not int

print('chai' + 'code') # output: chaicode
print(x, y, z) #gives output in tuple(in shell)

print(repr('chai')) # The output of repr() is intended for developers and is more useful for debugging purposes.
print(str('chai')) # The output of str() is intend for end-user and in human-readable string representation of an object.  
print('chai')

import math
math.floor(3.6) #output: 3
math.floor(-3.6) #output: -4

math.trunc(3.6) #output: 3  Truncates the Real x to the nearest Integral toward 0.
math.trunc(-3.6) #output: -3

print((2 + 3j) * 3) #output:(6+9j)  It also handle imaginary number and iota is represented by 'j'

import random
random.randint(1, 10) #gives random value btw 1 , 10

l1 = ['lemon', 'ginger', 'masala', 'mint']
random.choice(l1) #gives random value from above list
random.shuffle(l1) #shuffle the element of l1 list

setOne = {1, 2, 3, 4} #this is a mathematical set not dictionary(it has key value pair)
setOne | {5, 6, 7} #'|' is use for union the set and '&' for intersection

type() #this method is use for finding the type of datatype




