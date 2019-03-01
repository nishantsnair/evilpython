# Evil Python Lesson 9: Primes and Binary Search

[All Lessons](https://zsiegel92.github.io/evilpython/)

[TOC]

## Prime Numbers

**Question:** What is a prime number?

**Answer:** A prime number is a whole number greater than 1 whose only factors are 1 and itself

**Question:** How do we test whether a number, called $n$, is prime?

**Answer:** We *test* whether a number $n$ is prime by *testing* whether it is divisible by any of the integers between $1$ and $n$.

**Question:** Is there an easier test?

**Answer:** If we have a list of all the **prime numbers** less than $n$, we can test whether $n$ is divisible by any of those. If $n$ is divisible by any divisor $d$ between $1$ and itself ($1 < d < n$), then it is divisible by some prime number between $1$ and itself.

**Question:** Do we have to test whether $n$ is divisibleby **all** the primes less than $n$?

**Answer:** **NO!** We only have to test whether $n$ is divisible by primes less than $\sqrt{n}$.

> **Proof:** Suppose $n$ is not prime (meaning it is divisible by at least two prime numbers between $1$ and itself), but that none of those prime numbers are less than or equal to $\sqrt{n}$. Let $p$ and $q$ be prime divisors of $n$. By our assumption, we know $p > \sqrt{n}$ and $q > \sqrt{n}$, so $pq > \sqrt{n}\sqrt{n} = n$. We know that in the prime factorization of $n$, we have at least one $p$ and at least one $q$, so $pq \le n$. But we can't have $pq > n$ and $pq \le n$. So, if $n$ is not prime, then at least one prime factor of $p$ must be less than or equal to $\sqrt{n}$. $\square$

> The first $15$ prime numbers are $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47$.

### Prime Testing Example

**Question:** Is $407$ a prime number?

We could test whether $407$ is divisible by $1, 2, 3, 4, \ldots, 405, 406$, and if it's not, then it's prime! But that would be overkill.

To be more efficient, we could just test whether $407$ is divisible by any **primes** less than $407$. Those are $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401$. **Even that is too many!**

Note that $\sqrt{407} = 20.17424\ldots$. So, if $407$ is not prime, it must be divisible by some prime number less than $20$! That means we only have to test whether it is divisible by $2, 3, 5, 7, 11, 13, 17, 19$.

**Anwer:** So, is $407$ prime?

**Question:** Which of the following are prime?

* 403
* 851
* 953
* 827
* 1891

### A Lesson on Algorithms

[This lesson on algorithms](https://medium.com/@e.rajasekar/how-you-can-teach-computer-science-algorithms-to-middle-school-students-873310874c92) is great!

### Assignments

1. Write a function called `primetest` that tests whether numbers are prime. Maintain a list of prime numbers called `primes` that `primetest` uses, and each time you find a prime number, add it (in order!) to `primes`. Write code that finds the first 1000 prime numbers!

2. Write a Python `class` called `primer` that tells you the `n`'th prime number. Creating and using a `primer` object should look like this once you're done:
	```python
	p = primer()
	print(p.prime(15)) #prints 47
	```
	The `primer` class should have a dynamic field called `primes` that is a list containing primes (which gets updated), as in the previous problem.

	The `primer` class should also have a method called `primetest` that operates as above, as in
	```python
	p = primer()
	print(p.primetest(7))
	```


<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
