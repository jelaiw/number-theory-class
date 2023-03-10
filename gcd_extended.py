def extended_gcd(a, b):
    """Return gcd(a,b), x, y: gcd(a,b)=ax+by."""
    assert a >= b and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)

# Try examples from lecture.
# https://www.coursera.org/learn/number-theory-cryptography/lecture/lT1cv/extended-euclids-algorithm.
print(extended_gcd(10, 6))
print(extended_gcd(7, 5))
print(extended_gcd(391, 299))
print(extended_gcd(239, 201))
