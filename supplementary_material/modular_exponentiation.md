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
