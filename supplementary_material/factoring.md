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
