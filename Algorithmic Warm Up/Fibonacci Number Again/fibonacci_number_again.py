# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    remainder = n % m
    f0 = 1
    f1 = 2
    lst = [f0, f1]
    i = 2
    while i <= remainder:
        lst.append(lst[i-2] + lst[i-1])
        i += 1
    return lst[remainder]

if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
