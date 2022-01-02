# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    prices_per_weight = [prices[i]/weights[i] for i in range(len(weights))]

    prices = [price for _, price in sorted(zip(prices_per_weight, prices), reverse=True)]
    weights = [weight for _, weight in sorted(zip(prices_per_weight, weights), reverse=True)]
    prices_per_weight.sort(reverse=True)

    total = 0

    for i in range(len(prices_per_weight)):
        if capacity >= weights[i]:
            total += prices[i]
            capacity -= weights[i]
        else:
            total += prices_per_weight[i] * capacity
            capacity -= capacity
    return total

# print(maximum_loot_value(10, [30], [500]))
if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
