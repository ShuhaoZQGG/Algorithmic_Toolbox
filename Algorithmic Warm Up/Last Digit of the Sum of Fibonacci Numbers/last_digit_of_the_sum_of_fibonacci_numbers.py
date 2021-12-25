# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10

def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    f0 = 0
    f1 = 1
    lst = [f0, f1]
    i = 2
    while i <= n:
        lst.append(lst[i-2] + lst[i-1])
        i += 1
    return lst[n] % 10

def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    remainder = (n + 2) % 60
    last_digit = last_digit_of_fibonacci_number(remainder)
    if last_digit == 0:
        return 9
    else:
        return last_digit - 1


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
