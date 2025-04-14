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

To further develop our intuition, let us address the following question. How do numbers that give remainder $1$ when divided by $7$ look like? These numbers have the form 

$a = 7q + 1$

where $q$ is any integer. For example, for $q = 0$ we have $a = 1$. For positive $q = 1, 2, 3, ...$, we get the sequence $a = 8, 15, 22, ...$. For negative $q = -1, -2, -3, ...$, we get the sequence $a = -6, -13, -20, ...$. Overall, we get the following picture.

![number line for a = 7q + 1](remainders-fig1.png)

We can observe that the distance between any two consecutive numbers is exactly 7 and thus, every 7-th number has the same remainder when divided by 7. Clearly, this analysis generalize to division by any number $b$ and any remainder $r$: each $b$-th number has the remainder $r$ when divided by $b$. 

In the definition above we have introduced division with remainder. The result of the division is given by the quotient and the remainder. But why do they actually exist? In other words, is division with remainder always possible?

Suppose we want to divide $a$ by $b$, where $b$ is positive. In other words, we want to find $q$ and $r$, such that $0 \leq r < b$ and $a = qb + r$. How would we do that? Let's start with a positive $a$. In this case, we can do it using the intuition we discussed. Let us consider $a$ objects and let us start forming groups of them of size $b$ one by one. Eventually, there will be not enough objects left for the next group. Then, the number of complete groups is $q$ and the number of remaining objects is $r$. It is easy to see that $0 \leq r < b$ and $a = qb + r$.

More formally, we repeatedly subtract $b$ from $a$ until the result is less than $b$. The result is the remainder $r$ and the number of subtractions is the quotient $q$.

Now, what if $a$ is negative? Then we can easily adapt the procedure above: we start adding $b$ to $a$ until we get a non-negative number.

We have shown that division with remainder is always possible, but is it unique?

__Problem.__ For given $a$ and $b > 0$, is the representation of the form $a = qb + r$ for $0 \leq r < b$ unique?

It turns out that this representation is indeed unique. To prove this, let us assume by contradiction that there are two representations

$a = q_1b + r_1$, $a = q_2b + r_2$

This gives us that $q_1b + r_1 = q_2b + r_2$. After rearranging the terms, we get

$(q_1 - q_2)b = r_2 - r_1$

Let us look at the right-hand side $r_2 - r_1$ of this equality. Here, $r_2$ is less then $b$ and $r_1$ is non-negative. If we subtract something non-negative from a number that is already less than $b$, the result is again less than $b$. On the other hand, $-r_1$ is greater than $-b$ and $r_2$ is non-negative. If we add something non-negative to the number that is greater than $-b$ the result is also greater than $-b$. Thus, we can conclude that

$-b < r_2 - r_1 < b$

Now, let us have a look at the left-hand side. If $q_1 - q_2 \ne 0$, then $\lvert q_1 - q_2 \rvert \geq 1$. If we multiply this by $b$, we get a number that is at least equal to $b$ in the absolute value. Thus, the left-hand side is of the absolute value at least $b$ and the right-hand side is of the absolute value less then $b$. Thus, we must have that $q_1 - q_2 = 0$ or, in other words, $q_1 = q_2$. From this we can also observe that $r_2 - r_1 = (q_1 - q_2)b = 0 \cdot b = 0$ and $r_1 = r_2$. We have considered two expressions for the division of $a$ by $b$ with remainder and have shown that they actually must be the same.

We have introduced the generalized version of division, division with remainder. It turns out, that this notion has important connection to the notion of divisibility we discussed before.

__Lemma.__ Integers $a_1$ and $a_2$ have the same remainder when divided by $b$ if and only if $a_1 - a_2$ is divisible by $b$.

__Proof.__ Suppose $a_1$ and $a_2$ have the same remainder $r$ when divided by $b$:

$a_1 = q_1b + r$, $a_2 = q_2b + r$

Then, 

$a_1 - a_2 = q_1b + r - (q_2b +r) = (q_1 - q_2)b$

Thus, $a_1 - a_2$ is divisible by $b$ and $(q_1 - q_2)$ plays the role of $k$ from the definition of divisibility.

In the other direction, suppose $b \mid (a_1 - a_2)$. Then $a_1 - a_2 = kb$. Let us divide $a_2$ by $b$ with the remainder:

$a_2 = q_2b + r$

for some $q_2$ and $0 \leq r < b$.

Then 

$a_1 = a_2 + kb = q_2b + r + kb = (q_2 + k)b + r$

Thus, $a_1$ has the same remainder as $a_2$ when divided by $b$.

## Problems
__Problem.__ Suppose $a$ is not divisible by $2$ ($a$ is odd). What possible remainders can $a$ have when divided by $4$?

There are four possible remainders when we divide by $4$: $0$, $1$, $2$, $3$. Clearly, the remainder $0$ is impossible: having remainder 0 means that $4 \mid a$, but then $a$ is even. Suppose now that the remainder is $2$, that is $a = 4q + 2$ for some $q$. But then $a$ is even again, thus the remainder $2$ is also not possible. There are two remaining remainders, $1$ and $3$. Both of these are actually possible, for example, with $a = 1$ and $a = 3$.

__Problem__. Is it true that for any four integers $a$, $b$, $c$, $d$ there are two of them whose difference is divisible by $3$? 

Consider the following four numbers: $1$, $100$, $27$, $5$. After some examination we notice that $100 - 1 = 99$ is divisible by $3$. If you try some other examples, you will also see that there is always a pair with a difference divisible by $3$. In fact, the statement is always true!

The key idea for the solution is that there are just three possible remainders when dividing by $3$: 0, 1, and 2. Since we have four numbers, there must be two of them that have the same remainder (this is an application of the pigeonhole principle we discussed in the first course of this specialization). Thus, the difference of these two numbers is divisible by $3$ (we have established this property above). 
