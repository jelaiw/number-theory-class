## Modular Subtraction and Division
We have seen that any number is congruent to its remainder modulo $m$ and arithmetic operations preserve congruence. In particular, we can substitute all numbers by their remainders in arithmetic expressions if we are interested only in computations modulo $m$. Note, that we can do the same substitution by the remainder after each step of the calculation. This allows us to reduce all arithmetic operations to just remainders and to create arithmetic operations tables.

Consider $m=7$ and consider addition operation $a + b \mod{7}$, where $a$ and $b$ are two remainders modulo $7$. We get the following table:

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/x1x_Ck4HSESeI--EHXknxQ_c7659e6b978b4e5fb562ccd463ca12f1_Screen-Shot-2022-11-05-at-3.30.22-PM.png?expiry=1746662400000&hmac=hBl1zUk1D0D02Pc7rXwwe0TmfPtRjetuhIVcpDu3U0Y)

Here, the entry on the intersection of a row $a$ and a column $b$ contains $a + b \mod{7}$. For example, the entry on the intersection of the row $a=3$ and the column corresponds to $b=5$ contains $1$, which is the remainder of $a + b = 8$ when divided by $7$:

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/-hpcD-PxSOq87xxIkfeg-g_2170967c2c264025b87c6095edaccff1_Screen-Shot-2022-11-05-at-3.31.27-PM.png?expiry=1746662400000&hmac=bkKGnp54Zrkqvjuhr9zyYCBeKaVW5q4h2EjiNQFHZ2g)

We can create a similar table for the multiplication:

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/B0oPUjRXS7O0_39KOWRMzg_c67ddd0e3dc44080b9decfe6177ccff1_Screen-Shot-2022-11-05-at-3.32.02-PM.png?expiry=1746662400000&hmac=UtosIfJ_X7oKj3U0a9-uWrmcoYefc51eyU5A6UZfFPo)

Here, the entry on the intersection of row $a$ and a column $b$ contains $a \times b \mod{7}$. For example, that the first row and the first column consist of zeros. This is not surprising, each entry there contains some number multiplied by $0$.

We can use these tables to perform modular calculations. Given an arithmetic expression, we can substitute all numbers by their remainders and then perform arithmetic operations one by one using the tables.  

Tables are also convenient to study the properties of the operations.

__Problem.__ Suppose we have two numbers $a$ and $b$. Is there $x$ such that $a + x \equiv b \mod{7}$? 

To check this we can use the table for the addition above. Here, $a$ corresponds to the row of the table, $x$ correspond to the column and $b$ corresponds to the entry on the intersection. From the table we can see that the answer to the question is positive: each row contains all possible remainders.

Once we notice this property, we can ask whether it is true for any $m$.

__Problem.__ Let $a$, $b$ and $m>1$ be integers. Is there $x$ such that $a + x \equiv b \mod{m}$? 

It turns out that the answer is positive even for an arbitrary $m$. To see this, consider $b-a$ as an integer and consider its remainder $x$ modulo $m$. We know that $a + (b - a) \equiv b \mod{m}$ and the congruence remains true even if we substitute $b-a$ by its remainder.

The number $x$ in this problem plays a role of _modular subtraction_ $b-a$ in modular arithmetic. Thus, we have just checked that the subtraction is always possible in modular arithmetic.
