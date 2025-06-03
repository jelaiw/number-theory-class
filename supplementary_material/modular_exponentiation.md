## Modular Exponentiation
Our next results (Fermat's little theorem and its generalization, Euler's totient theorem) deal with modular exponentiation, i.e., with expressions of type $a^b\mod{c}$ where $a$,$b$,$c$ are integers. But before stating and proving this result, let us discuss the purely algorithmic question: how to compute $a^b\mod{c}$ reasonably fast?

__Stop and think!__ How would you compute $314^{271}\mod{123}$ and $314159265358^{2718281828}\mod{123456789}$?

Computing this in Python directly gives the following result:
```python
print((314 ** 271) % 123)
print((314159265358 ** 2718281828) % 123456789)
```
