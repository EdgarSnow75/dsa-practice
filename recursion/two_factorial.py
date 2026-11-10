# Factorial with loop
def fac_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Factorial with recursion
def fac_re(n):
    if n == 1:
        return 1
    return n * fac_re(n - 1)


def main():
    print(fac_loop(5))
    print(fac_loop(10))

    print(fac_re(5))
    print(fac_re(10))


if __name__ == "__main__":
    main()
