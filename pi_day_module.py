import math


class PiDay:

	def __init__(self, limit):
		self.limit = limit

	@staticmethod
	def calcPi(limit):

	  q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

	  decimal = limit
	  counter = 0

	  while counter != decimal + 1:
	    if 4 * q + r - t < n * t:

	      yield n
	      
	      if counter == 0:
	        yield '.'
	      
	      if decimal == counter:
	        print('')
	        break
	        
	      counter += 1
	      nr = 10 * (r - n * t)
	      n = ((10 * (3 * q + r)) // t) - 10 * n
	      q *= 10
	      r = nr

	    else:
	      nr = (2 * q + r) * l
	      nn = (q * (7 * k) + 2 + (r * l)) // (t * l)

	      q *= k
	      t *= l
	      l += 2
	      k += 1
	      n = nn
	      r = nr

	def get_pi(self):
	  pi_digits = self.calcPi(self.limit)

	  i = 0
	  
	  for d in pi_digits:
	  	print(d, end="")

	  	i += 1
	  	if i == 60:
	  		print("")
	  		i = 0