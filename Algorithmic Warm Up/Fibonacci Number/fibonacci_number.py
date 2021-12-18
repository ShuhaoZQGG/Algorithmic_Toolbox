# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    lst = [0, 1]
    i = 2
    while i <= n:
        lst.append(lst[i - 1] + lst[i - 2])
        i += 1
    return lst[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
