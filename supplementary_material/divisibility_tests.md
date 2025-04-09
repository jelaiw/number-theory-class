## Divisibility Tests
In some cases, one can check whether $a$ is divisible by $b$ without trying to divide by $b$.

__Problem.__ What is the remainder and the quotient of $3756$ when divided by $10$?

Decimal system is really convenient here. Note that

$3756 = 3750 + 6 = 375 \cdot 10 + 6$

Thus the quotient is $375$ and the remainder is $6$.

Clearly, this argument can be generalized to give the following. 

__Lemma.__ The remainder of an integer $a$ when divided by $10$ is the last digit of $a$, the quotient is an integer resulting from $a$ by dropping its last digit off. 

__Corollary.__ An integer $a$ is divisible by $10$ if and only if its last digit is $0$.

__Problem__. Is $7347$ divisible by $5$?

Let us try to use the same trick:

$7347 = 734 \cdot 10 + 7 = 734 \cdot 2 \cdot 5 + 5 + 2$

We see that the remainder of $7347$ when divided by $5$ is $2$ and thus $7347$ is not divisible by $5$.

We can generalize this to the following criteria for divisibility by $5$.

__Lemma.__ An integer $a$ is divisible by $5$ if and only if its last digit is either 0 or 5. 

Indeed, let us denote the last digit of $a$ by $b$. Then the last digit of $a−b$ is $0$. Thus, $a-b$ is divisible by 5. We have shown above that this means that $a$ and $b$ have the same remainder when divided by 5. This remainder is $0$ iff $b=0$ or $b=5$.

We can prove a similar statement for divisibility by $2$.

__Lemma.__ An integer $a$ is divisible by $2$ if and only if its last digit is either 0, 2, 4, 6, or 8. 
