import random as rd
import math


def get_factors(number):
    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:  # 防止重复添加平方数的因子
                factors.append(number // i)
    return sorted(factors)


def combination(n, m):
    """计算组合数 C(n, k)"""
    return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))


def permutation(n, m):
    """计算排列数 P(n, k)"""
    return math.factorial(n) // math.factorial(n - m)


def p(z, m):
    return rd.randint(1, m) <= z


def X(m):
    return rd.randint(1, m)


def GEN_oto():
    if p(9, 10):
        a = rd.randint(1, 9)
        b = rd.randint(1, 9)
        if p(2, 3):
            return (fr"{a} \times {b}", a * b)
        elif p(1, 2):
            return (fr"{a} + {b}", a + b)
        else:
            return (fr"{a} - {b}", a - b)
    else:
        c = rd.choice([4, 6, 8])
        d = rd.choice(get_factors(c))
        return (fr"{c} \div {d}", c // d)


def GEN_bignum():
    a = rd.randint(10001, 99999)
    b = rd.randint(10001, 99999)
    return (fr"{a} \times {b}", a * b)


def GEN_CA():
    if p(25, 30):
        a = rd.randint(2, 8)
        b = rd.randint(0, a)
        return (fr"C^{b}_{a}", combination(a, b))
    else:
        a = rd.randint(2, 4)
        b = rd.randint(1, a)
        return (fr"A^{b}_{a}", permutation(a, b))


# def GEN_frac():
#     a = rd.randint(2, 25)
#     b = rd.choice(get_factors(a))
#     return (fr"\dfrac{{{b}}}{{{a}}}", fr"\dfrac{{b}}{{a}}")
