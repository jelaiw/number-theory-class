## Modular Exponentiation
Our next results (Fermat's little theorem and its generalization, Euler's totient theorem) deal with modular exponentiation, i.e., with expressions of type $a^b\mod{c}$ where $a$,$b$,$c$ are integers. But before stating and proving this result, let us discuss the purely algorithmic question: how to compute $a^b\mod{c}$ reasonably fast?

__Stop and think!__ How would you compute $314^{271}\mod{123}$ and $314159265358^{2718281828}\mod{123456789}$?

Computing this in Python directly gives the following result:
```python
print((314 ** 271) % 123)
print((314159265358 ** 2718281828) % 123456789)
```
__Stop and think!__ Do you see why python is not able to compute the second value?

The problem is that Python starts by computing the number $314159265358^{2718281828}$ that is huge. One can estimate its size as follows: $a^n$ has approximately $n$ times more digits than $a$, so the power in question has about $2718281828$ times the base size ($12$) digits and hardly fits into computer memory. 

__Stop and think!__ How can we do better?

The right way to compute modular exponentiation in python is to use the built-in `pow` method. The following code produces the result in the blink of an eye. We will learn what is going on under the hood below.

```python
print(pow(314, 271, 123))
print(pow(314159265358, 2718281828, 123456789))
```
To get a hint, you may think about the following problem.

__Problem__. Compute $8^{100}\mod{63}$

Of course, starting with computing $8^{100}$ is a bad idea. Note that $8^2 \equiv 64 \equiv 1\pmod{63}$ and

$8^{100} = 8^2 \cdot 8^2 \cdot ... \cdot 8^2 \equiv 1 \cdot 1 \cdot ... \cdot 1 \pmod{63}$,

hence the answer is $1$. 

Here, we use that the product does not change modulo $m$, when we replace the factors by equivalent (modulo $m$) ones. This (and the same property of sums) was discussed in the previous chapter. (When adding some multiple of $m$ to one of the summands or factors, we change the result by a multiple of $m$: indeed, $(u + km) + v = (u + v) + km$ and $(u + km)v = uv + kmv$.

__Problem__. Prove that $2^{1001} + 3^{1001}$ is divisible by $5$.

_Hint_: $3 \equiv -2\pmod{5}$

__Problem__. Prove that $a^n - b^n$ is divisible by $a - b$ for integers $a > b$.

_Hint_: $a \equiv b\pmod{d}$ for $d = a - b$.

__Problem__. Find $2^{1025}\mod{17}$.

__Solution__. Since $2^{1024} = 16^{256} \equiv (-1)^{256} \equiv 1 \pmod{17}$, the answer is $2$.

__Stop and think!__ Now we can compute $a\mod{c}$, $a^2\mod{c}$, $a^3\mod{c}$, ... sequentially, multiplying each time by $a$ and keeping only the remainder modulo $c$. In this way we do not need to store large numbers (only numbers smaller than $c$). Does this approach work for our example $314159265358^{2718281828}\mod{123456789}$?

The size of numbers is no more a problem, but we need to perform $2718281828$ multiplications --- too many. Can we do better? This is a _general question for computing powers_ (that makes sense not only for modular computations).

__Problem__. 
Let $x$ be some number. Can you compute $x^{64}$ in less than $63$ multiplications (that would be needed if we compute $x$,$x^2$,$x^3$, ... ,$x^{64}$ sequentially)?

For this problem the answer is especially easy to guess, since $64$ is a power of $2$ and repeated squaring helps:

$x^2 = x \cdot x$, $x^4 = x^2 \cdot x^2$, $x^8 = x^4 \cdot x^4$, $x^{16} = x^8 \cdot x^8$, $x^{32} = x^{16} \cdot x^{16}$, $x^{64} = x^{32} \cdot x^{32}$

In this way the exponents grow faster ($\times 2$ instead of $+1$ at every step), and we use only $6$ multiplications. 

In general, to compute $x^n$ for $n = 2^k$ we need $k = log_2{n}$ multiplications.

__Stop and think!__ Now we know how to compute $x^n$ fast if $n$ is a power of two. But what if not? How can we compute, say, $x^{65}$, or $x^{68}$, or $x^{77}$?

For $x^{65}$ we may multiply $x^{64}$ by $x$. Since we have also computed previous powers of $2$, we may use that

$x^{68} = x^{64} \cdot x^4$ and $x^{77} = x^{64} \cdot x^8 \cdot x^4 \cdot x$

(note that $77 = 64 + 8 + 4 + 1$).

Similar trick can be used in the general case, as the following problem shows:

__Problem.__
Prove that $x^n$ (for some $n > 1$) can be computed in at most $2log_2{n}$ multiplications.

If $n$ is not a power of $2$, the value of $log_2{n}$ is not an integer, but we may take the closest integer below $log_2{n}$.

__Solution.__
Indeed, we can compute by squaring all the powers $x^2$, $x^4$, ... ,$x^{2^k}$ where the exponent does not exceed $n$. There are at most $log_2{n}$ of them (again we may round $log_2{n}$). Then we represent $n$ as sum of powers of $2$ (why is it possible? this is what the binary system is about) and get $x^n$ as the product of corresponding powers.

For the practical viewpoint, it may make sense to implement essentially the same algorithm in the other direction, so to say: use formula

$x^n = (x^2)^{n/2}$

that reduces the exponent twice for even $n$ for the price of one multiplication ($x^2 = x \cdot x$), and use

$x^n = x^{n-1} \cdot x$

that uses one multiplication to reduce to the even case (if $n$ is odd, then $n-1$ is even). 

In this case, we reduce the exponent to $1$ (or $0$, if we do not treat separately the case of $x^1$) in about $2log_2{n}$ steps (in two steps we reduce the exponent at least twice).

```python
def fast_modular_exponentiation(b, e, m):
    assert m > 0 and e >= 0
    if e == 0:
        return 1
    if e == 1:
        return b
    if e % 2 == 0:
        return fast_modular_exponentiation((b * b) % m, e // 2, m)
    else:
        return (fast_modular_exponentiation(b, e - 1, m) * b) % m


print(fast_modular_exponentiation(314159265358, 2718281828, 123456789))
```

The program implementing this idea computes $314159265358^{2718281828}\mod{123456789}$ in a fraction of a second.

__Problem.__
Prove that the number of multiplications when computing $x^n$ (for $n \ge 1$) both in this program and in the method descibed above (using binary notation) is the same: 

_(number of bits in n) + (number of ones in n) - 2_

where counting the bits and ones in $n$ we use the binary representation of $n$.

It turns out that this is not exactly the minimal number of multiplications needed to compute $x^n$. For example, for $x^{15}$ we get $6$ multiplications with both our approaches, while one can compute it in $5$ multiplications:

$x^2 = x \cdot x; x^4 = x^2 \cdot x^2; x^5 = x^4 \cdot x; x^{10} = x^5 \cdot x^5; x^{15} = x^{10} \cdot x^5$.

See [Wikipedia article about addition chains](https://en.wikipedia.org/wiki/Addition-chain_exponentiation) that minimize the number of multiplications.
