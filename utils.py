import math

def divisors(n: int):
    div = []
    for i in range(2, math.ceil(n / 2)):
        if n % i == 0:
            div.append(i)
    return div

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)

def euler_totient(n: int) -> int:
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count
