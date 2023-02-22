def gcd(a, b):
    """Return gcd(a,b), x, y: gcd(a,b)=ax+by."""
    assert a >= b and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)

def diophantine(a, b, c):
    d, _x, _y = gcd(a, b)
    assert c % d == 0

    k = c // d
    x = _x * k
    y = _y * k
    assert a * x + b * y == c
    # return (x, y) such that a * x + b * y = c
    return (x, y)

print(diophantine(4936, 1000, 728))
