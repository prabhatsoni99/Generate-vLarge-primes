import random
from math import sqrt

def rabin_miller(num):
	"""https://inventwithpython.com/rabinMiller.py
	if it returns True -> probably prime(99% +)
	if it returns False -> definitely composite"""
	s = num - 1
	t = 0
	while s % 2 == 0:
		# keep halving s while it is even (and use t
		# to count how many times we halve s)
		s = s // 2
		t += 1

	for trials in range(2): # try to falsify num's primality 5 times
		a = random.randrange(2, num - 1)
		v = pow(a, s, num)
		if v != 1: # this test does not apply if v is 1.
			i = 0
			while v != (num - 1):
				if i == t - 1:
					return False
				else:
					i = i + 1
					v = (v ** 2) % num
	return True


def generator_primes(twice_the_length):
	"""
	parameter length is how many digits should the prime be approx
	This technique uses miller - rabin + Ulams spiral
	"""
	num = twice_the_length//2
	ctr=0
	for i in range(100):
		lol = random.randint(10**num,10**(num+1))
		val = lol**2 + lol + 3399714628553118047
		if val%2==0:
			val+=1
		if val%5==0:
			val+=2
		res = rabin_miller(val)
		if res:
			print(val,":",res)


generator_primes(300)