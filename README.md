
# Generate-vLarge-primes

This project explores the idea of using Ulam's Spiral to generate primes faster.


# [1/7] Why do we need large primes?
They are required in cryptographic protocols like:
- RSA
- Diffie-Hellman
- Elliptic curve cryptography

1. These protocols rely on the secrecy of prime numbers.
2. If you get from a third party, then they would *not be secret anymore* - thereby defeating the purpose of the protocol.
3. Thus, you need to generate these primes *using code, on the fly, and on your PC*.


# [2/7] How Are Primes Generated in Standard Libraries?
Broadly,
1. Generate a random number that ends with `1,3,7 or 9`.
Depending on protocol this number is to be used in, it would be of `1024` or `2048` bits.
If this number is to be used in RSA, the number must be coprime to your selected `e`.
3. Check if it is divisible by primes `< 10,000`.
4. Apply Miller-Rabin primality test.

# [3/7] Ulam's Spiral

- Ulam's Spiral is basically a distribution of numbers that have high chance of being prime.
- Golden Line is one particular curve/parabola on Ulam's spiral. The `y`-coordinates of this curve have 10-20X more chance of being prime than random numbers.
- Golden Line Equation: ```y = x^2 + x + 3399714628553118047```
- I learnt about Ulam's Spiral from [This Awesome Video](https://www.youtube.com/watch?v=iFuR97YcSLM). I recommend you watch it too.

Ulam's Spiral has been excluded from all major crypto libraries. Let us find out why.


# [4/7] Why Ulam's Spiral Should Not Be Used In Practice

The answer is *SECURITY*.
1. If we generated primes using Ulam's Spiral only, that would significantly reduce the keyspace (i.e. possible numbers we can select as key). This makes it much easier for the attacker to "guess" our secret prime.
2. The time savings will be 10-20X at max. (since Golden Line of Ulam's Spiral has 10-20X the density of prime numbers). After getting a candidate number to check, we are applying the same primality test only.
3.  There is **not a lot of time savings**. The reduction in keyspace is **huge**.
Current library software can generate `1024`-bit primes in `0.1-0.5 seconds`. Also, keys for RSA are exchanged infrequently.

I learnt about this from [this issue I had raised](https://github.com/Legrandin/pycryptodome/issues/374).

Apart from this, **another less important reason**:\
There are some constraints on `y`:
  1. `y` must be `mod e`. 
  2. `y` must be `1024` or `2048` bits long.

We can only control the selection of `x`. So, we must select such an `x` that we get a `y` obeying `1.` and `2.`\
And this must be done in `O(1)` since our time savings are 10-20X only.



# [5/7] Usage

The python script helps us experimentally compare the density of primes in Ulam's Spiral and randomly selected numbers.
1. Install the dependencies of `pip`.\
```pip install -r requirements.txt```
2. Run the script.\
```python3 run_me.py```


# [6/7] Slides
The slides contain various techniques that help us generate primes faster. The slides should be understandable by beginners.

|  | General Math | Use  Modular Arithmetic |
| --- | --- | --- |
| **Probabilistic** | Ulam's Spiral | - Fermat's Little Theorem (FLT)<br>- Rabin-Miller test |
| **Deterministic** | <br>- Comparing with list_primes<br>- Sieve of Eratosthenes<br>- Fibonacci primes<br>- AKS primality test | Lucas-Lehmer Test |


# [7/7] Credits

This was presented as a Student Talk by me.\
*Where*: [Evariste (math club)](https://www.reddit.com/r/mathiiitd/wiki/index), IIIT Delhi\
*When*: January, 2019
