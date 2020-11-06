def gcd(a, b):
    while a != 0:
        a, b = b % a, b # swap values for a and b without temp variable
    return b


def main():
    print(gcd(7, 12))

main()