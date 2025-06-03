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
