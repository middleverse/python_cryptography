# Euclid's algorithm for finding greatest common denominator
def gcd(a, b):
    while a != 0:
        a, b = b % a, a # swap values for a and b without temp variable
    return b

# Euclid's extended algorithms for finding mod inverse
def findModInverse(a, m):
    # if a and m aren't relatively prime, then no inverse exists
    if gcd(a, m) != 1:
        return None 
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # (a / m)taper off the floating point
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m