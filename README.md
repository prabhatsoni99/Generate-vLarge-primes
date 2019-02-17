# Generate-vLarge-primes
Use Miller-Rabin + Ulam's Spiral to generate 500-1000 primes

<h2>Why generate large primes?</h2>
They are pretty important for cryptographic(cyberscurity) techniques like RSA, Diffie-Hellman<br>

<h5>Ulams Spiral<h5>
Link: https://www.youtube.com/watch?v=iFuR97YcSLM   Prime Spirals by Numberphile<br>
y = f(x)<br>
Golden line equation is: y = x^2 + x + 3399714628553118047 <br>
The values of y have 20X more chance of being prime than other numbers<br>

<h5>Miller-Rabin<h5>
This comes from Fermat's Little Theorem.<br>
Time complexity is: O(k  *  log^3 n), where k is number of tests for a single number<br>
For a plain single test, time complexity is O(log^3 n)<br>
This technique is efficient as the time it takes to test primality of a number [practically] doesn't increase with the length of the number<br>
This technique is non-deterministic or a pseudo-primality test<br>
