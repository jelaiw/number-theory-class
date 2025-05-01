## Applications
Now we will use this knowledge to solve several more advanced problems.

__Problem.__ What are the last two digits of the number $99^{99}$?

The number $99^{99}$ is huge, we do not want to compute it. Instead, we can use remainders. Note that the number consisting of the last two digits is just the remainder after the division by $100$. Thus, we are actually interested in the remainder of the number $99^{99}$ when divided by $100$. 

Note that $99 \equiv -1 \mod{100}$. This allows us to simplify the computation a lot:

$99^{99} \equiv (-1)^{99} \equiv -1 \equiv 99 \mod{100}$

Thus, the remainder of $99^{99}$ when divided by $100$ is $99$ and these are the two last digits of $99^{99}$.

In the computation above we used that $99^{99}$ is just $99$ multiplied by itself $99$ times. We then use that in the multiplication modulo some number we can substitute the numbers by their congruent. 

Note that one cannot just substitute any number in any expression by its congruent. For example, we cannot substitute $99^{99}$ by $(-1)^{-1}$. We have only proved that we can substitute numbers by their congruents in additions and multiplications, and we should be careful to use only these properties.

__Problem.__ Is the number $3475$ divisible by $3$?

To solve this problem it is enough to compute the remainder of the number after the division by $3$: the number is divisible by $3$ iff the remainder is $0$.

But how can we compute the remainder fast? We can try the same approach we used for divisibility tests. Observe that

$3475 = 3000 + 400 + 70 + 5 = 3 \cdot 10^3 + 4 \cdot 10^2 + 7 \cdot 10^1 + 5$

Now we represented our number as an arithmetic expression and we can use modular arithmetic. Note that 

$10 \equiv 1 \mod{3}$

Thus, for any positive $k$

$10^k \equiv 1^k \equiv 1 \mod{3}$

Applying this to our number, we get

$3475 \equiv 3 \cdot 10^3 + 4 \cdot 10^2 + 7 \cdot 10^1 + 5 \equiv 3 + 4 + 7 + 5 \mod{3}$

Now 

$3 + 4 + 7 + 5 \equiv 19 \equiv 1 \mod{3}$

Thus, the remainder of $3475$ when divided by $3$ is $1$ and $3475$ is not divisible by $3$.

Note, that the same argument can be applied in a general setting, giving the following lemma.

__Lemma.__ An integer $a$ is congruent modulo $3$ to the sum of its digits. In particular, $a$ is divisible by $3$ iff the sum of its digits is divisible by $3$.

Completely the same analysis applies to the remainders modulo $9$.

__Lemma.__ An integer $a$ is congruent modulo $9$ to the sum of its digits. In particular, $a$ is divisible by $9$ iff the sum of its digits is divisible by $3$.

## Remainders of Large Numbers
__Problem.__ What is the remainder of the number $762341$ when divided by $3$?

__Problem.__ What is the remainder of the number $12^{100}$ when divided by $11$?

__Problem.__ What is the remainder of the number $4632^{10}$ when divided by $10$?

