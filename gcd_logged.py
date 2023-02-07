def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        print(f"gcd({a}, {b})")
        if a >= b:
            a = a % b
        else:
            b = b % a

    print(f"gcd({a}, {b})")
    return max(a, b)

print(gcd(790933790547, 1849639579327))
