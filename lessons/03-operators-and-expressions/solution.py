"""Lesson 3: Operators and Expressions (Arithmetic, Comparison, Logic, Bitwise)

All runnable code from this lesson, combined in order.
"""

print(7 / 2, 7 // 2, 7 % 2, 2 ** 5)
print(-7 // 2, -7 % 2)          # floor rounds down
print(divmod(17, 5))            # quotient and remainder together
print(1 < 5 < 10)               # chained comparison
print(not (3 > 2 and 2 > 5))

x = 10
x += 5
x *= 2
print(x)

# short-circuit saves us from division by zero
d = 0
print(d != 0 and 10 / d > 1)


a, b = 6, 3          # 110 and 011
print(a & b, a | b, a ^ b)   # and, or, xor
print(a << 1, a >> 1)        # shift left = x2, right = //2
print(bin(a), bin(b))


lo, hi = 0, 9
mid = lo + (hi - lo) // 2
print(mid)


def free_orders(order_numbers):
    return [n for n in order_numbers if n % 5 == 0]

print(free_orders(range(1, 21)))


def is_even(n):
    return n % 2 == 0

print(is_even(10), is_even(7), is_even(-4))


def hm(total):
    h, m = divmod(total, 60)
    return f"{h}h {m}m"

print(hm(135))


def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print([n for n in range(1, 40) if is_power_of_two(n)])


def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

print([y for y in (1900, 2000, 2023, 2024)], [is_leap(y) for y in (1900, 2000, 2023, 2024)])
