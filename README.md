# Generate-vLarge-primes

Our aim is to take humanity ahead! To expand the boundaries of science.\
Our aim is to generate industry-ready primes faster than they are generated today.

# Notice
The product is not working currently. We plan to fix it soon.

# Why do we need large primes?
They are required in cryptographic protocols like:
- RSA
- Diffie-Hellman
- Elliptic curve cryptography

These techniques rely on the secrecy and large size of prime numbers. And, you cannot take your prime numbers from somewhere else - then it would not be secret.\
Thus, you need to generate these primes using code running on your PC.

# Usage

Building the binary:\
```$ make all```

Usage:\
```$ ./generate1Prime -<total number of bits>```

Example:\
```$ ./generate1Prime -1024```


- **Clarification**: The parameter is **total number of bits**, and not **number of bits as 1**.
- We are generating exactly 1024 bit primes. Nothing less. Nothing more. The reason for this is embedded devices have limited memory and are only able to use primes of exact length.
- Industry requires primes of some sizes. Some of them are: 384, 512, 1024, 2048, 3072, 4096 bits.



# Ulam's Spiral

We observe an interesting mathematical pattern - Ulam's Spiral has been excluded from popular crypto libraries. This project will only try to incorporate Ulam's Spiral with well-known library fucntions/implementations of primality testing. Doing this may make prime generation faster - who knows!


Would recommend you to watch [Youtube video on Ulam's Spiral](https://www.youtube.com/watch?v=iFuR97YcSLM) \
Ulam's Spiral is basically a distribution of numbers that have high chance of being prime.\
Golden Line is a curve. The y-coordinates of this curve have 20X more chance of being prime than other random numbers.\
Golden Line Equation: ```y = x^2 + x + 3399714628553118047```


This was presented as a Student Talk by me.\
Where: [Evariste (math club)](https://www.reddit.com/r/mathiiitd/wiki/index), IIIT Delhi\
When: January, 2019
