# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)
    total_amount = 0
    # 0.1 merge the v and w in the same list

    prices_weights = list(zip(prices, weights))

    # 0.2 sort values by v/w
    prices_weights.sort(key=lambda x: x[0]/x[1], reverse=True)
    #1)loop all items in the optimized
    for v, w in prices_weights:
        if capacity == 0:
            return total_amount
        # depend on the amount left
        amount = min(w,capacity)
        # this is needed in case we took part of the weight
        total_amount += amount* v/w
        capacity -= amount
    return total_amount


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
