When is an integer $a$ is divisible by an integer $b$? A naive answer will be that we should consider the rational number $\frac{a}{b}$ and if it is an integer, then $a$ is divisible by $b$. However, this definition refers to a more complex concept of rational numbers. Let us unwrap this explanation and try to understand what we are actually trying to say. 

What does it mean that $\frac{a}{b}$ is integer? It means that the denominator cancels out. In other words, we can represent $a$ as a product of $b$ and some integer $k$: $a = bk$. Then we have $\frac{a}{b} = \frac{bk}{b} = k$. Now, this reformulation only uses a simple notion of multiplication and does not refer to rational numbers. As a result, we arrive at the following definition.

__Definition.__ An integer number $a$ is divisible by an integer number $b$ (or in other words, $b$ divides $a$), denoted by $b \mid a$, if there is an integer $k$ such that $a = bk$. If $a$ is not divisible by $b$, we denote this by $b \nmid a$.

The intuition behind this definition is simple (for positive $a$ and $b$). Suppose we have $a$ objects and we want to split them into equal groups of size $b$. This is possible if and only if $a$ is divisible by $b$, and $k$ is the number of the resulting groups. 

__Problem.__ Is $15$ divisible by $3$? Is it divisible by $4$? Is it divisible by $-5$?

__Problem.__ Is $-24$ divisible by $-6$? Is it divisible by $-5$?
