# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10

def pisanoPeriod(m):
    prev, curr = 0, 1
    for i in range(m ** 2):
        prev, curr = curr, (prev + curr) % m

        if (prev == 0 and curr == 1):
            return i + 1

def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    pisano_period = pisanoPeriod(m)

    n = n % pisano_period

    prev, curr = 0, 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n - 1):
        prev, curr = curr, prev + curr

    return curr % m

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

def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if from_index == to_index:
        return last_digit_of_fibonacci_number(from_index)
    else:
        from_index %= 60
        to_index %= 60

        from_index = fibonacci_number_again(from_index + 1, 10) - 1
        to_index = fibonacci_number_again(to_index + 2, 10) - 1
    return (to_index - from_index) % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
