## Remainders
We have seen that the division over integers is not always possible. But we can generalize it. 

__Definition (Division with remainder).__ Let $a$ be an integer and $b$ be a positive integer. The result of the division of $a$ by $b$ with a remainder is a pair of integers, $q$ called quotient and $r$ called remainder, such that 

$a = qb + r$

and $0 \leq r < b$.

Observe, that if $r = 0$, then $a$ is divisible by $b$.

The intuition behind this definition is simple. Assume that $a$ is positive. We would like to split $a$ objects into groups of size $b$. We form the groups one by one. In the end it might happen that there are some objects left and there are not enough of them for the new group. The number of the remaining objects is the remainder $r$ and the number of completed groups is the quotient $q$. 

Let us consider several examples.

* For $a = 15$ and $b = 4$, we have $15 = 3 \cdot 4 + 3$. Here $q = r = 3$.
* For $a = -13$ and $b = 3$, we have $-13 = (-5) \cdot 3 + 2$ and $q = -5$, $r = 2$.
* For $a = 12$ and $b = 4$, we have $12 = 3 \cdot 4 + 0$ and $q = 3$, $r = 0$.

In Python, one can compute the quotient and the remainder either directly or using a built-in method `divmod`.

```python
a, b = -13, 3
print(a // b, a % b)
print(divmod(a, b))
```

```python
-5 2
(-5, 2)
```
