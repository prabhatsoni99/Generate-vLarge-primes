import gmpy2
import random

"""
This program will compare
- the density of primes in Ulam's Spiral
and
- the density of primes among positive integers
"""

# NOTE
# len(x**2) = 2 * len(x)
#		or
# len(x**2) = 2 * len(x) - 1
# => NAIVE_START_RANGE = 2 * ULAMS_START_RANGE
# This is done so that both Ulam's Spiral and Naive method are checking for
# primes of similar length/size - so that there is no bias.

# Golden line equation: y = x^2 + x + 3399714628553118047


naive_prime_numbers = []
naive_prime_number_count = 0

ulams_prime_numbers = []
ulams_prime_number_count = 0

##### YOU CAN EDIT THESE:
NAIVE_START_RANGE = 10**240
ULAMS_START_RANGE = 10**120 # make sure this is NAIVE_START_RANGE / 2, else tests will be biased
NUM_TESTS = 3000


for i in range(NUM_TESTS):
	# Single primality test run (Number generated randomly/naively)
	naive_testcase = random.randint(NAIVE_START_RANGE, NAIVE_START_RANGE*10)
	naive_ans = gmpy2.is_prime(naive_testcase)
	if naive_ans == True:
		naive_prime_number_count += 1
		naive_prime_numbers.append(naive_testcase)

	# Single primality test run (number generated by Ulam's Spiral)
	x = random.randint(ULAMS_START_RANGE, ULAMS_START_RANGE*10)
	ulams_testcase = x**2 + x + 3399714628553118047 # ulams_testcase is y
	ulams_ans = gmpy2.is_prime(ulams_testcase)
	if ulams_ans == True:
		ulams_prime_number_count += 1
		ulams_prime_numbers.append(ulams_testcase)

	completed_percentage = ((i+1)/NUM_TESTS)*100
	print("Completed: " + str(int(completed_percentage)) + "%", end = '\r')


print()
print("---------- RESULTS ----------")
print("Naive method: " + str(naive_prime_number_count) + " primes")
print("Ulams Spiral: " + str(ulams_prime_number_count) + " primes")

##### UNCOMMENT THESE IF YOU WANT TO PRINT LISTS:
# print()
# print("Naive prime numbers:")
# print('\n'.join(str(x) for x in naive_prime_numbers))
# print("Ulams prime numbers:")
# print('\n'.join(str(x) for x in ulams_prime_numbers))