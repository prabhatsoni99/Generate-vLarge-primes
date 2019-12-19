# Generate-vLarge-primes

Our goal is to build a fast method to generate large prime numbers that can be used for cryptographic applications. Size of primes should be >= 1024 bits.

Techniques used:
- Miller-Rabin primality test
- Ulam's Spiral

 # Why do we need large primes?
They are required in cryptographic protocols like:
- RSA
- Diffie-Hellman
- Elliptic curve cryptography

These techniques rely on the secrecy and large size of prime numbers.
And, you cannot take your prime numbers from somewhere else - then it would not be secret. Thus, you need to generate these primes using code running on your PC.

# Usage
Format:
```
$ python3 generateLargePrimes.py  <desired_length>  <how_many_nums_to_test>
```
Example:
```
$ python3 generateLargePrimes.py 650 100
```
will test 100 numbers of length 650 each.
Industry standards say we should use 1024+ bit primes.
Setting the first parameter, i.e. ```desired_length``` to ```650``` achieves that.

# Ulam's Spiral
Would recommend you to watch [Video on Ulam's Spiral](https://www.youtube.com/watch?v=iFuR97YcSLM)
This is basically a distribution of numbers that have high chance of being prime.
Golden Line is a curve. The y-coordinates of this curve have 20X more chance of being prime than other random numbers.
Golden Line Equation: ```y = x^2 + x + 3399714628553118047```

# Miller-Rabin Primality Test

[Learn about Miller-Rabin](https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/)

This comes from Fermat's Little Theorem.
This technique is non-deterministic, or a pseudo-primality test. This technique is not mathematically perfect; it works in about 99% times.
Since, it may not necessarily give the correct answer the first time, we can run 5 or 10 tests to test if a given number is prime or not - if the test says it is not prime in any of the tests run, we can reject it,
Time complexity for a single test: ```O(log^3 n)```
Time complexity for k tests run: ```O(k  *  log^3 n)```

This technique is very efficient as the time taken to test primality of a number doesn't increase much with the size of the number

This was presented as a Student Talk by me.
Where: Evariste(math club), IIIT Delhi
When: January, 2019
