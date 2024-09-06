from utils import euler_totient

import math

def multiplicative_order(a: int, n: int) -> int:
    phi = euler_totient(n)

    order = None

    for i in range(1, phi + 1):
        if phi % i != 0:
            continue

        if math.pow(a, i) % n == 1:
            order = i
            break

    return order

print(multiplicative_order(7,10))