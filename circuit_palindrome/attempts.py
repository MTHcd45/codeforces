# circuit

import math
 
def min_max(n, s):
   if sum(s) <= n:
       M = sum(s)
       m = math.ceil(sum(s)/2)
   else:
       M = 2*n - sum(s)
       if sum(s) % 2 != 0:
           m = sum(s) % 2
       else:
           m = 0
   return m, M


# simple palindrome

def solution(*arg):
   def opti(n):
   vowels = ['a','e','i','o','u']
   level = "".join(vowels)
   vowelsR = vowels
   string = ""
   for j in range(0, divmod(n,5)[0]):
       string += level
   for k in range(0, divmod(n,5)[1]):
       rmc = vowelsR[k]
       string += rmc
       vowelsR.remove(rmc)
   return string
   N = arg[0]
   sizes = [arg[j] for j in range(0,arg[0])]
   return [opti(arg[j+1]) for j in range(0,N)]


def challenge1(*arg):
   def opti(n):
       vowels = ['a','e','i','o','u']
       level = "".join(vowels)
       vowelsR = vowels
       string = ""
       for j in range(0, divmod(n,5)[0]):
           string += level
       for k in range(0, divmod(n,5)[1]):
           rmc = vowelsR[k]
           string += rmc
           vowelsR.remove(rmc)
       return string
   N = arg[0]
   sizes = [arg[j] for j in range(0,arg[0])]
   return [opti(arg[j+1]) for j in range(0,N)]


