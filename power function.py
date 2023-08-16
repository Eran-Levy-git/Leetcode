def power1(base, pow):
    return base**pow


def power2(base, pow):
    result = 1
    for _ in range(pow):
        result *= base
    return result


def power3(base, pow):
    result = 1
    while pow > 0:
        if pow % 2 == 1:
            result *= base
            pow -= 1
        pow //= 2
        base *= base
    return result


def power4(base, pow):
    if pow == 0:
        return 1
    elif pow < 0:
        return 1 / power3(base, -pow)
    elif pow % 2 == 1:
        return base * power3(base, pow - 1)
    else:
        return power3(base * base, pow // 2)


b = 2
p = 3

result1 = power1(b, p)
result2 = power2(b, p)
result3 = power3(b, p)
result4 = power4(b, p)

print(f"Result 1 is: {result1}")
print(f"Result 2 is: {result2}")
print(f"Result 3 is: {result3}")
print(f"Result 4 is: {result4}")
