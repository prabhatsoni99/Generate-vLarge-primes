/*
We will add basic testing later:
	- %5 == 0
	- prime sieve - testing divisibility with prime numbers < 1000

	first do everything in int and then shift later

	https://www.boost.org/doc/libs/1_64_0/libs/math/doc/html/math_toolkit/number_series/primes.html
*/

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <time.h>
#include <math.h>
//using namespace std;


int generate_NUMBITS_bits_prime(int NUMBITS)
{
	int myPrime;

	srand(time(0)); // initialising the seed

	int x = random()%100; //generate random number - around 10^600
	int y = pow(x,2) + x + 33;
	// int y = x**2 + x + 3399714628553118047; // gives odd numbers only
	// myPrime = primality_test(y);
	myPrime = y;

	return myPrime;
}


int main(int argc, char *argv[])
{
	int NUMBITS = atoi(argv[1]);
	int myPrime = generate_NUMBITS_bits_prime(NUMBITS);
	std::cout << myPrime;
}

