import math


def z(x, y):
    return 4.31 * math.log(2 * pow(x, 4)) + 0.05 * pow(math.cos(y), 2)


def b(x, y, a, k):
    c = pow(math.e, 2 * y) * math.sin(x) / math.sqrt(abs(pow(x, 3) - 1) - a * k)
    d = math.atan(2 * y) - k * math.log(pow(a, 3), 4)
    return c + d


print(z(2, 5))
print(b(5, 4, 3, 1))
