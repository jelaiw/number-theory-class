## Existence
In this section, we discuss the following (almost obvious) statement:

__Theorem__
Every integer $m > 1$ can be represented as the product of primes: there exists a positive integer $k$ and primes $p_1, ..., p_k$ such that $m = p_1 \times ... \times p_k$.

__Stop and think!__ What happens if $m$ is prime?

In this case, $k = 1$ and $p_1 = m$. So the phrase "product of primes" should not be taken too literally: in this case there is only one (prime) number in the "product" and the product is equal to this number. (One could even allow $m = 1$ by considering an "empty product" with no factors that is equal to $1$, but we will not go that far.)

Note also that we do not require the $p_1, ..., p_k$ to all be distinct: for example, $4 = 2 \cdot 2$ and $12 = 3 \cdot 2 \cdot 2$.

__Stop and think!__ Do you see how to prove the theorem?

Let us look at this statement from the algorithmic point of view: given some $m>1$, how can we find a prime decomposition (existence of which we want to prove)?

If $m$ is prime, we already know that this decomposition consists of $m$ only. What if $m$ is composite (not prime)? By definition then, $m=uv$ for some $u$, $v$ where $1 < u,v < m$. How can we then find the decomposition of $m$?  It is easy: just combine the decompositions of $u$ and $v$, forming a long product from the two shorter ones. Both $u$ and $v$ are smaller that $m$, so we may assume (by induction in our proof, or a recursive call in our algorithm) that for $u$ and $v$ the decompositions exist and can be found.

```python
# Finds the minimal divisor>1 of the given integer m>1
def min_divisor(m):
    for d in range(2, m + 1):
        if m % d == 0:
            return d
        # optimization:
        if d * d > m:
            return m


def is_prime(m):
    return m == min_divisor(m)


def factoring(m):
    if is_prime(m):
        return [m]
    else:
        divisor = min_divisor(m)
        factors = factoring(m // divisor)
        factors.append(divisor)
        return factors


for i in (7, 60, 1001, 2 ** 32 + 1, 2 ** 64 + 1):
    print(f'Factoring of {i}: {factoring(i)}')
```

```sh
Factoring of 7: [7]
Factoring of 60: [5, 3, 2, 2]
Factoring of 1001: [13, 11, 7]
Factoring of 4294967297: [6700417, 641]
Factoring of 18446744073709551617: [67280421310721, 274177]
```

__Stop and think!__ Examine the algorithm and compare it with the description above. What is the discrepancy and why is the algorithm correct?

The algorithm finds the smallest divisor $d$ and then decomposes $m$ into $d \cdot (m / d)$. If we followed our description literally, we should be applying the algorithm recursively to both $d$ and $m / d$ and concatenate the resulting lists. Instead, we just append $d$ to the decomposition of $m / d$.

__Stop and think!__ Why is it OK to do this?

In other words, why may we assume that the smallest divisor $d$ is a prime? The answer is in the word "smallest": if $d$ were not prime, then its divisors would be smaller divisors of $m$. (Recall that a divisor of a divisor is a divisor: $u \mid d$ and $d \mid m$ implies $u \mid m$, as we have seen.)

__Problem.__
Note that in our examples the factors go in the non-increasing order in the decomposition provided by our algorithm. Will it be always the case?

__Solution.__
In fact it will, and it is easy to see why, also using inductive (recursive) argument. In our algorithm, $d$ is the _smallest_ divisor of $m$, so all divisors of $m/d$ (being also divisors of $m$) are at least $d$. So appending $d$ to the ordered list for $m/d$ (induction assumption), we do not destroy the ordering.

__Problem.__
There is a funny trick for children that learn division. Take any three digit number, say $358$. Write it twice: $358358$. Then divide the resulting number by $74, then by $11$ and then by $13$. Miraculously all divisions do not give a remainder and the result is the original number $358$ (indeed, $358358/7=51194$, $51194/11=4654$ and $4654/13=358$). Can you explain why this trick always works?

__Hint__: look at the second line in our factorization examples.
