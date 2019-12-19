import random
from math import sqrt
import sys # for command line arguments

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


def generator_primes(desired_length, how_many_nums_to_test):
	"""
	parameter length is how many digits should the prime be approx
	This technique uses miller - rabin + Ulams spiral
	"""
	num = desired_length//2 # num is the length we are using during the algorithm
	ctr=0
	for i in range(how_many_nums_to_test):
		X = random.randint(10**num,10**(num+1))
		Y = X**2 + X + 3399714628553118047 # gives odd numbers only
		if Y%5==0:
			Y+=2
		result = rabin_miller(Y)
		if result:
			print("[Prime Found] ", Y)


print("Input format: python3 generateLargePrimes.py  <desired_length>  <how_many_nums_to_test>")
desired_length = int(sys.argv[1])
how_many_nums_to_test = int(sys.argv[2])
generator_primes(desired_length, how_many_nums_to_test)

