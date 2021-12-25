# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    n %= 60
    f0 = 0
    f1 = 1
    lst = [f0, f1]
    i = 2
    while i <= n:
        lst.append(lst[i-2] + lst[i-1])
        i += 1
    return lst[n] % 10

if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
